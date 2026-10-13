export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email, prenom, nom, tel } = req.body || {};
  if (!email || !prenom || !nom || !tel) {
    return res.status(400).json({ error: 'Champs requis manquants' });
  }

  let phone = tel.replace(/[\s.\-()]/g, '');
  if (phone.startsWith('0')) phone = '+33' + phone.slice(1);
  else if (!phone.startsWith('+')) phone = '+33' + phone;

  const addContact = (attributes) => fetch('https://api.brevo.com/v3/contacts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'api-key': process.env.BREVO_API_KEY
    },
    body: JSON.stringify({ email, attributes, listIds: [17], updateEnabled: true })
  });

  let brevoRes = await addContact({ PRENOM: prenom, NOM: nom, SMS: phone });

  // Brevo refuse un numéro SMS déjà associé à un autre contact :
  // on inscrit quand même la personne, avec le numéro dans un attribut non unique.
  if (!brevoRes.ok) {
    const data = await brevoRes.json().catch(() => ({}));
    if (data.code !== 'duplicate_parameter') {
      return res.status(brevoRes.status).json({ error: data.message || 'Erreur Brevo' });
    }
    brevoRes = await addContact({ PRENOM: prenom, NOM: nom, TELEPHONE: phone });
    if (!brevoRes.ok) {
      const retry = await brevoRes.json().catch(() => ({}));
      return res.status(brevoRes.status).json({ error: retry.message || 'Erreur Brevo' });
    }
  }

  // Attendre l'envoi : sur Vercel, la fonction est figée dès que la réponse part,
  // un fetch non attendu n'atteint jamais Brevo. Un échec ne bloque pas l'inscription.
  try {
    await fetch('https://api.brevo.com/v3/smtp/email', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'api-key': process.env.BREVO_API_KEY
      },
      body: JSON.stringify({
        templateId: 5,
        to: [{ email, name: `${prenom} ${nom}` }]
      })
    });
  } catch {}

  return res.status(200).json({ ok: true });
}
