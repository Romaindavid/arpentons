export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email } = req.body || {};
  if (!email || typeof email !== 'string') {
    return res.status(400).json({ error: 'Email requis' });
  }

  const brevoRes = await fetch('https://api.brevo.com/v3/contacts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'api-key': process.env.BREVO_API_KEY
    },
    body: JSON.stringify({ email, listIds: [2], updateEnabled: true })
  });

  if (brevoRes.ok || brevoRes.status === 204) {
    return res.status(200).json({ ok: true });
  }

  const data = await brevoRes.json().catch(() => ({}));
  if (data.code === 'duplicate_parameter') {
    return res.status(200).json({ ok: true, duplicate: true });
  }

  return res.status(brevoRes.status).json({ error: data.message || 'Erreur Brevo' });
}
