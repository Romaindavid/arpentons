import json

FONTS = "https://fonts.googleapis.com/css2?family=Libre+Caslon+Text:wght@400;700&family=Hanken+Grotesk:wght@300;400;600;700&display=swap"

# Couleurs
C = {
    "bg": "#fbf9f4",
    "primary": "#182232",
    "secondary": "#9d4400",
    "secondary_fixed": "#ffdbca",
    "surface": "#f0eee9",
    "outline": "#c5c6cd",
    "muted": "#45474c",
    "white": "#ffffff",
}

HEADER = f"""
<tr>
  <td align="center" style="padding:40px 24px 32px; background:{C['primary']}; border-bottom:3px solid {C['secondary']};">
    <p style="margin:0 0 8px; font-family:'Libre Caslon Text',Georgia,serif; font-size:28px; font-weight:700; letter-spacing:-0.5px; color:{C['white']};">ARPENTONS !</p>
    <span style="display:inline-block; background:{C['secondary']}; color:{C['white']}; font-family:'Hanken Grotesk',Arial,sans-serif; font-size:11px; font-weight:600; letter-spacing:0.12em; text-transform:uppercase; padding:4px 12px;">La Rochelle</span>
  </td>
</tr>"""

FOOTER = f"""
<tr>
  <td align="center" style="padding:28px 24px; background:{C['primary']};">
    <p style="margin:0 0 8px; font-family:'Libre Caslon Text',Georgia,serif; font-size:16px; color:{C['white']}; font-weight:700;">Arpentons !</p>
    <p style="margin:0; font-family:'Hanken Grotesk',Arial,sans-serif; font-size:12px; color:{C['secondary_fixed']}; opacity:0.8;">
      <a href="https://arpentons.fr" style="color:{C['secondary_fixed']}; text-decoration:none;">www.arpentons.fr</a>
      &nbsp;·&nbsp; contact@arpentons.fr
    </p>
  </td>
</tr>"""

def wrap(body_rows):
    return f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <link href="{FONTS}" rel="stylesheet">
  <style>
    body,table,td {{ font-family:'Hanken Grotesk',Arial,sans-serif; }}
    a {{ color:{C['secondary']}; }}
  </style>
</head>
<body style="margin:0;padding:0;background:{C['bg']};">
<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="{C['bg']}">
  <tr><td align="center" style="padding:24px 0;">
    <table width="600" border="0" cellspacing="0" cellpadding="0" style="background:{C['white']};border:1px solid {C['outline']};border-collapse:collapse;">
      {HEADER}
      {body_rows}
      {FOOTER}
    </table>
  </td></tr>
</table>
</body>
</html>"""

# ── TEMPLATE CONFIRMATION ────────────────────────────────────────────────────

confirmation_body = f"""
<tr>
  <td style="padding:40px 36px 32px;">

    <!-- Titre -->
    <p style="margin:0 0 6px; font-family:'Hanken Grotesk',Arial,sans-serif; font-size:11px; font-weight:600; letter-spacing:0.12em; text-transform:uppercase; color:{C['secondary']};">Inscription confirmée</p>
    <p style="margin:0 0 24px; font-family:'Libre Caslon Text',Georgia,serif; font-size:26px; font-weight:700; color:{C['primary']}; line-height:1.2;">C'est confirmé !</p>

    <p style="margin:0 0 28px; font-size:15px; line-height:1.7; color:{C['muted']};">
      Bonjour,<br><br>
      Ton inscription pour la prochaine session d'arpentage est bien enregistrée. On a hâte de partager ce moment de lecture collective avec toi !
    </p>

    <!-- Infos pratiques -->
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:24px;">
      <tr>
        <td style="background:{C['surface']};border:1px solid {C['outline']};padding:20px 24px;">
          <p style="margin:0; font-size:15px; line-height:1.9; color:{C['primary']};">
            📍 <strong>Lieu :</strong> Collectif Actions Solidaires, 21 Rue Sardinerie, La Rochelle.<br>
            📅 <strong>Date :</strong> Lundi 15 juin 2026.<br>
            🕒 <strong>Horaires :</strong> 18h00 (accueil/apéro) — 18h30 (début de l'atelier).
          </p>
        </td>
      </tr>
    </table>

    <!-- Livre -->
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:24px;">
      <tr>
        <td style="background:{C['bg']};border-left:4px solid {C['secondary_fixed']};padding:20px 24px;">
          <p style="margin:0 0 4px; font-family:'Hanken Grotesk',Arial,sans-serif; font-size:11px; font-weight:600; letter-spacing:0.12em; text-transform:uppercase; color:{C['secondary']};">Le livre à l'honneur</p>
          <p style="margin:0 0 8px; font-family:'Libre Caslon Text',Georgia,serif; font-size:17px; font-weight:700; color:{C['primary']}; font-style:italic;">« État de droit, ordre bourgeois » — Elsa Marcel</p>
          <p style="margin:0; font-size:14px; line-height:1.6; color:{C['muted']};">
            Face aux gouvernements liberticides et aux violences policières, se défendre en justice devient à la fois plus nécessaire et plus difficile. Elsa Marcel invite à renouer avec la défense politique des grands procès militants pour repenser aujourd'hui les pratiques judiciaires au service des luttes.
          </p>
        </td>
      </tr>
    </table>

    <!-- Note livre -->
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:24px;">
      <tr>
        <td style="background:{C['surface']};border:1px solid {C['outline']};padding:20px 24px;">
          <p style="margin:0; font-size:14px; line-height:1.6; color:{C['muted']};">
            <strong style="color:{C['primary']};">Note sur le livre :</strong> Le collectif se charge de l'achat du livre pour toutes les sessions. Le jour J, une cagnotte sera disponible pour une contribution libre et consciente (entre une dizaine et une vingtaine d'euros).
          </p>
        </td>
      </tr>
    </table>

    <!-- Programme -->
    <p style="margin:0 0 12px; font-family:'Libre Caslon Text',Georgia,serif; font-size:17px; font-weight:700; color:{C['primary']};">Au programme</p>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:28px;">
      <tr><td style="padding:8px 0; border-bottom:1px solid {C['outline']}; font-size:14px; color:{C['muted']}; line-height:1.5;">
        <strong style="color:{C['primary']};">18h00 — Accueil &amp; Apéro</strong><br>
        On grignote, on discute. N'hésite pas à apporter un petit truc à partager !
      </td></tr>
      <tr><td style="padding:8px 0; border-bottom:1px solid {C['outline']}; font-size:14px; color:{C['muted']}; line-height:1.5;">
        <strong style="color:{C['primary']};">18h30 — Démarrage</strong><br>
        Début de la lecture (merci d'être ponctuel·le).
      </td></tr>
      <tr><td style="padding:8px 0; font-size:14px; color:{C['muted']}; line-height:1.5;">
        <strong style="color:{C['primary']};">21h30 — Fin</strong><br>
        Clôture de l'atelier.
      </td></tr>
    </table>

    <!-- Alerte -->
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:32px;">
      <tr>
        <td style="background:{C['secondary']};padding:20px 24px;">
          <p style="margin:0; font-size:14px; line-height:1.6; color:{C['white']};">
            <strong>⚠️ Important :</strong> L'arpentage est un puzzle humain. Si tu manques à l'appel, ta partie du livre manquera à tout le groupe !<br><br>
            <strong>En cas de retard ou d'annulation de dernière minute :</strong><br>
            Prévenir Coralie au <strong>06 50 68 61 89</strong>.
          </p>
        </td>
      </tr>
    </table>

    <p style="margin:0; font-size:15px; line-height:1.7; color:{C['muted']}; font-style:italic;">
      À très vite,<br>
      <strong style="font-style:normal; color:{C['primary']};">L'équipe Arpentons !</strong>
    </p>

  </td>
</tr>"""

# ── TEMPLATE INVITATION ──────────────────────────────────────────────────────

invitation_body = f"""
<tr>
  <td style="padding:40px 36px 32px;">

    <!-- Accroche -->
    <p style="margin:0 0 6px; font-family:'Hanken Grotesk',Arial,sans-serif; font-size:11px; font-weight:600; letter-spacing:0.12em; text-transform:uppercase; color:{C['secondary']};">Prochain rendez-vous</p>
    <p style="margin:0 0 24px; font-family:'Libre Caslon Text',Georgia,serif; font-size:26px; font-weight:700; color:{C['primary']}; line-height:1.2;">Le prochain arpentage arrive...</p>

    <p style="margin:0 0 28px; font-size:15px; line-height:1.7; color:{C['muted']};">
      Salut !<br><br>
      C'est l'heure de se retrouver pour une nouvelle session de lecture collective.
    </p>

    <!-- Livre -->
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:24px;">
      <tr>
        <td style="background:{C['bg']};border-left:4px solid {C['secondary_fixed']};padding:20px 24px;">
          <p style="margin:0 0 4px; font-family:'Hanken Grotesk',Arial,sans-serif; font-size:11px; font-weight:600; letter-spacing:0.12em; text-transform:uppercase; color:{C['secondary']};">Le livre à l'honneur</p>
          <p style="margin:0 0 8px; font-family:'Libre Caslon Text',Georgia,serif; font-size:17px; font-weight:700; color:{C['primary']}; font-style:italic;">« État de droit, ordre bourgeois » — Elsa Marcel</p>
          <p style="margin:0; font-size:14px; line-height:1.6; color:{C['muted']}; font-style:italic;">
            Face aux gouvernements liberticides et aux violences policières, se défendre en justice devient à la fois plus nécessaire et plus difficile. Elsa Marcel montre comment garde des Sceaux, parquet et juges font bloc derrière le régime. Elle invite à renouer avec la défense politique des grands procès militants — FLN, Rosa Luxemburg, Tribunal Russell — pour repenser aujourd'hui les pratiques judiciaires au service des luttes.
          </p>
        </td>
      </tr>
    </table>

    <!-- Infos pratiques -->
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:28px;">
      <tr>
        <td style="background:{C['surface']};border:1px solid {C['outline']};padding:20px 24px;">
          <p style="margin:0; font-size:15px; line-height:1.9; color:{C['primary']};">
            📍 <strong>Lieu :</strong> Collectif Actions Solidaires, 21 Rue Sardinerie, La Rochelle.<br>
            📅 <strong>Date :</strong> Lundi 15 juin 2026.<br>
            🕒 <strong>Horaires :</strong> 18h30 — 21h30 (accueil dès 18h).
          </p>
        </td>
      </tr>
    </table>

    <!-- CTA -->
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:32px;">
      <tr>
        <td align="center">
          <a href="https://arpentons.fr" style="display:inline-block; background:{C['secondary']}; color:{C['white']}; font-family:'Hanken Grotesk',Arial,sans-serif; font-size:13px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; text-decoration:none; padding:14px 32px; border:2px solid {C['primary']};">
            JE M'INSCRIS À LA SESSION
          </a>
        </td>
      </tr>
    </table>

    <!-- Méthode -->
    <p style="margin:0 0 12px; font-family:'Libre Caslon Text',Georgia,serif; font-size:17px; font-weight:700; color:{C['primary']};">Rappel de la méthode</p>
    <p style="margin:0 0 28px; font-size:14px; line-height:1.7; color:{C['muted']};">
      Pas besoin d'avoir lu le livre ! On le déchire sur place, on se partage les pages, on lit un peu et on met tout en commun. C'est simple, c'est convivial et on en ressort toujours moins bête.
    </p>

    <!-- Alerte -->
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:32px;">
      <tr>
        <td style="background:{C['secondary']};padding:20px 24px;">
          <p style="margin:0; font-size:14px; line-height:1.6; color:{C['white']};">
            <strong>⚠️ Important :</strong> L'arpentage est un puzzle humain. Si tu t'inscris, on compte vraiment sur toi car chaque partie du livre compte pour le groupe !
          </p>
        </td>
      </tr>
    </table>

    <p style="margin:0; font-size:15px; line-height:1.7; color:{C['muted']}; font-style:italic;">
      À très vite,<br>
      <strong style="font-style:normal; color:{C['primary']};">Le collectif Arpentons !</strong>
    </p>

  </td>
</tr>"""

html_confirmation = wrap(confirmation_body)
html_invitation = wrap(invitation_body)

with open('/tmp/template_confirmation_new.html', 'w') as f:
    f.write(html_confirmation)

with open('/tmp/template_invitation_new.html', 'w') as f:
    f.write(html_invitation)

# Payloads API
payload_confirmation = json.dumps({
    "htmlContent": html_confirmation,
    "subject": "Confirmation de ton inscription — Arpentons !",
    "sender": {"name": "Collectif Arpentons !", "email": "collectif@arpentons.fr"}
})

payload_invitation = json.dumps({
    "name": "Invitation - arpentage du 15 juin",
    "subject": "Le prochain arpentage — 15 juin !",
    "previewText": "Inscris-toi à la prochaine session — lundi 15 juin à La Rochelle.",
    "sender": {"name": "Collectif Arpentons !", "email": "collectif@arpentons.fr"},
    "htmlContent": html_invitation,
    "recipients": {"listIds": [2]}
})

with open('/tmp/payload_confirmation.json', 'w') as f:
    f.write(payload_confirmation)

with open('/tmp/payload_invitation.json', 'w') as f:
    f.write(payload_invitation)

print("OK — fichiers prêts")
