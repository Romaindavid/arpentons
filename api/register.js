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
  const attributes = { PRENOM: prenom, NOM: nom, SMS: phone };

  const brevoRes = await fetch('https://api.brevo.com/v3/contacts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'api-key': process.env.BREVO_API_KEY
    },
    body: JSON.stringify({ email, attributes, listIds: [17], updateEnabled: true })
  });

  if (brevoRes.ok || brevoRes.status === 204) {
    fetch('https://api.brevo.com/v3/smtp/email', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'api-key': process.env.BREVO_API_KEY
      },
      body: JSON.stringify({
        templateId: 5,
        to: [{ email, name: `${prenom} ${nom}` }]
      })
    }).catch(() => {});

    return res.status(200).json({ ok: true });
  }

  const data = await brevoRes.json().catch(() => ({}));
  if (data.code === 'duplicate_parameter') {
    return res.status(200).json({ ok: true, duplicate: true });
  }

  return res.status(brevoRes.status).json({ error: data.message || 'Erreur Brevo' });
}
