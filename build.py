"""Genera la web en español (public/index.html) e inglés (public/en/index.html).

Todo el texto está en CONTENT. Cambia lo que quieras aquí y ejecuta:  python build.py
"""
from html import escape
from pathlib import Path
import json

SITE_URL = "https://rodrigoballescaba.app"
PUBLIC = Path(__file__).parent / "public"

EMAIL = "rodrigoballescaba@gmail.com"
PHONE = "+34 695 361 678"
LINKEDIN = "https://www.linkedin.com/in/rodrigo-ballesteros-caba%C3%B1as-163853165/"
GITHUB = "https://github.com/rodrigoballescaba"
CV_PDF = "cv/rodrigo-ballesteros-cv.pdf"

APPS = [
    ("Druni", "druni.png",
     "https://apps.apple.com/es/app/perfumerias-druni/id1592321069",
     "https://play.google.com/store/apps/details?id=es.druni.druni_app"),
    ("Zummo Cloud", "zummo-cloud.png",
     "https://apps.apple.com/es/app/zummo-cloud/id6444164141",
     "https://play.google.com/store/apps/details?id=com.zummo.zummocloud"),
    ("Alicante Bus", "alicante-bus.png",
     "https://apps.apple.com/es/app/alicante-bus/id1040157627",
     "https://play.google.com/store/apps/details?id=com.cuatroochenta.subusalicante"),
    ("HiBeats", "hibeats.png",
     "https://apps.apple.com/es/app/hibeats/id1563711761",
     "https://play.google.com/store/apps/details?id=com.darkan.hibeats.app"),
    ("Novaconnect", "novaconnect.png",
     "https://apps.apple.com/es/app/novaconnect/id1614666977",
     "https://play.google.com/store/apps/details?id=com.darkan.nova.app"),
]

CLIENTS = "Allfunds, BNP Paribas, Druni, Zummo, Gibson, Hoomvip, Molo, La Fàbrica del Sol y el bus urbano de Alicante"

CONTENT = {
    "es": {
        "path": "",
        "title": "Rodrigo Ballesteros · Tech Lead Flutter e IA",
        "description": "Tech Lead con 9 años de experiencia en Flutter, React y Google Cloud. "
                       "Llevo IA generativa a producto real: agentes, asistentes y LLMs en producción.",
        "og_locale": "es_ES",
        "skip": "Saltar al contenido",
        "nav": [("#ia", "IA"), ("#proyectos", "Proyectos"), ("#experiencia", "Experiencia"), ("#contacto", "Contacto")],
        "lang_switch": ("en/", "EN", "Read in English"),
        "cv_btn": "CV en PDF",
        "role": "Tech Lead en Flutter e IA aplicada, Valencia",
        "h1": "Apps en Flutter y producto con IA que llegan a producción.",
        "lead": "Llevo 9 años construyendo apps móviles y web, con más de 30 publicadas en App Store y Google Play. "
                "Hoy me centro en meter agentes y LLMs en productos reales, desde la arquitectura en Google Cloud "
                "y Firebase hasta la tienda.",
        "cta_mail": "Escríbeme",
        "cta_cv": "Descargar CV",
        "availability": "Disponible para proyectos freelance y puestos de Tech Lead.",
        "chat_name": "Renacia Clinic's",
        "chat_status": "Asistente con IA",
        "chat": [
            ("user", "Hola, ¿tenéis hueco el jueves por la tarde para la consulta de valoración?"),
            ("tool", "get_available_slots"),
            ("bot", "¡Hola! El jueves por la tarde tengo libre a las 17:00 y a las 18:30. ¿Cuál te viene mejor?"),
            ("user", "A las 18:30, porfa"),
            ("tool", "book_appointment"),
            ("bot", "Hecho, te he reservado el jueves a las 18:30. ¿Me dices tu nombre para la ficha?"),
        ],
        "chat_caption": "Conversación de ejemplo con el asistente de WhatsApp que he construido para una clínica: "
                        "el agente consulta la agenda y reserva en Google Calendar.",
        "replay": "Ver otra vez",
        "ai_h": "IA aplicada",
        "ai_intro": "Uso la IA en dos frentes: dentro del producto, para que haga trabajo real, y en cómo lo construyo.",
        "ai_cols": [
            ("En el producto", True, [
                ("Agentes con tool calling", "que consultan y actúan sobre sistemas reales: agenda, CRM, pagos."),
                ("Asistentes conversacionales", "en WhatsApp, con traspaso a una persona cuando hace falta."),
                ("Varios proveedores de LLM", "Claude, GPT, Gemini o DeepSeek, intercambiables sin tocar el código."),
                ("RAG y salidas estructuradas", "embeddings, búsqueda semántica y respuestas validadas con Zod."),
                ("Prompts y evaluación", "diseño de prompts y pruebas de calidad de las respuestas."),
            ]),
            ("En el desarrollo", False, [
                ("Claude Code, Cursor y Copilot", "en el día a día, con criterio para revisar lo que generan."),
                ("Agentes y MCP", "para automatizar tareas repetitivas del equipo."),
                ("Python", "para scripts, datos y automatizaciones."),
                ("Equipos que usan IA", "flujos y buenas prácticas para que el equipo gane velocidad sin perder calidad."),
            ]),
        ],
        "projects_h": "Proyectos",
        "projects_intro": "Lo último que he construido, y algunas de las apps que he publicado en las tiendas.",
        "feature_kicker": "Proyecto freelance, 2026",
        "feature_title": "Renacia Clinic's",
        "feature_text": "Web, asistente de WhatsApp con IA y panel de gestión para una clínica de micropigmentación capilar. "
                        "Todo en producción y mantenido por mí.",
        "feature_points": [
            "El asistente responde por WhatsApp, consulta huecos y reserva la cita en Google Calendar.",
            "El proveedor de IA se elige por configuración: Claude hoy, otro modelo mañana si sale más barato.",
            "Panel para la clínica con fichas de clientes, retoques, gastos, objetivos y KPIs.",
            "Web pública rápida, con blog y SEO, en Firebase Hosting.",
        ],
        "feature_link": "Ver la web",
        "apps_h": "Apps publicadas",
        "clients_label": "También he trabajado para",
        "exp_h": "Experiencia",
        "stack_h": "Stack",
        "edu_h": "Formación",
        "contact_h": "Contacto",
        "contact_intro": "¿Tienes un proyecto, un equipo que liderar o una idea con IA? Cuéntamela.",
        "call": "Llamar",
        "footer": "Esta web no usa cookies ni analítica.",
        "stack": [
            ("Móvil", "Flutter, Dart, Android (Kotlin, Java), iOS (Swift), plugins nativos, App Store y Google Play"),
            ("Web", "React, Next.js, TypeScript, Angular, Node.js, HTML y CSS"),
            ("Cloud", "Google Cloud, Firebase (Firestore, Auth, Functions, App Hosting), AWS (Lambda, DynamoDB, Cognito, S3)"),
            ("Lenguajes", "Dart, TypeScript, Python, Kotlin, Swift, C# y SQL"),
            ("Equipo", "CI/CD, Git, arquitectura limpia, Scrum y revisión de código"),
        ],
        "edu": [
            ("Grado en Ingeniería Informática", "Universitat Politècnica de València, 2012 – 2016"),
            ("Máster en Desarrollo de Aplicaciones Multiplataforma", "UPV, campus de Gandia, 2016 – 2017"),
            ("Máster en Desarrollo de Aplicaciones Android", "UPV, campus de Gandia, 2017 – 2018"),
            ("Idiomas", "Español nativo e inglés intermedio"),
        ],
        "jobs": [
            ("Desarrollador freelance, producto e IA", "Renacia Clinic's", "", "2026 – actualidad", True, [
                "Web, bot de WhatsApp con IA y panel de gestión en producción: Next.js, React y TypeScript sobre Firebase y Google Cloud.",
                "Agente con Vercel AI SDK y tool calling sobre la API de WhatsApp Cloud, con proveedor de LLM intercambiable.",
            ]),
            ("Tech Lead", "We Are Cactus", "", "abr. 2025 – ago. 2026", False, [
                "Liderazgo técnico del equipo: arquitectura, estimaciones, revisión de código y mentoring, en contacto directo con cliente.",
                "Apps multiplataforma en Flutter y web en React, con backend en Firebase y Google Cloud.",
                "Integración de IA generativa en producto y en el día a día del equipo.",
            ]),
            ("Tech Lead Flutter", "Cuatroochenta", "Castellón", "feb. 2023 – abr. 2025", False, [
                "Dirección del equipo Flutter: arquitectura, revisión de código, CI/CD y publicación en App Store y Google Play.",
            ]),
            ("CTO", "Darkan Technologies", "Madrid", "mar. 2021 – feb. 2023", False, [
                "Responsable de toda la tecnología de la startup: app en Flutter, backend en AWS y Firebase, y web.",
                "Captación de usuarios con campañas en Google Ads y Meta Ads.",
            ]),
            ("Senior Frontend Developer", "Epigram", "Valencia", "abr. 2019 – mar. 2021", False, [
                "Apps en Flutter y desarrollo de plugins nativos para iOS.",
            ]),
            ("Junior Frontend Developer", "Mobilendo", "Valencia", "sept. 2017 – abr. 2019", False, [
                "Apps híbridas con Ionic, experiencias de realidad virtual en Unity y servicios en AWS.",
            ]),
        ],
    },
    "en": {
        "path": "en/",
        "title": "Rodrigo Ballesteros · Flutter & AI Tech Lead",
        "description": "Tech Lead with 9 years of experience in Flutter, React and Google Cloud. "
                       "I bring generative AI into real products: agents, assistants and LLMs in production.",
        "og_locale": "en_GB",
        "skip": "Skip to content",
        "nav": [("#ai", "AI"), ("#projects", "Projects"), ("#experience", "Experience"), ("#contact", "Contact")],
        "lang_switch": ("../", "ES", "Leer en español"),
        "cv_btn": "CV (PDF)",
        "role": "Flutter & applied AI Tech Lead, Valencia, Spain",
        "h1": "Flutter apps and AI products that ship to production.",
        "lead": "I've spent 9 years building mobile and web apps, with more than 30 published on the App Store and "
                "Google Play. Today I focus on putting agents and LLMs into real products, from the architecture on "
                "Google Cloud and Firebase to the store release.",
        "cta_mail": "Email me",
        "cta_cv": "Download CV",
        "availability": "Available for freelance projects and Tech Lead roles, remote or in Valencia.",
        "chat_name": "Renacia Clinic's",
        "chat_status": "AI assistant",
        "chat": [
            ("user", "Hi, do you have a slot on Thursday afternoon for the first consultation?"),
            ("tool", "get_available_slots"),
            ("bot", "Hi! On Thursday afternoon I have 5:00 pm and 6:30 pm free. Which one suits you?"),
            ("user", "6:30 please"),
            ("tool", "book_appointment"),
            ("bot", "Done, you're booked for Thursday at 6:30 pm. What name should I put on the file?"),
        ],
        "chat_caption": "Sample conversation with the WhatsApp assistant I built for a clinic: the agent checks the "
                        "calendar and books the slot in Google Calendar.",
        "replay": "Play again",
        "ai_h": "Applied AI",
        "ai_intro": "I use AI on two fronts: inside the product, doing real work, and in the way I build it.",
        "ai_cols": [
            ("Inside the product", True, [
                ("Tool-calling agents", "that query and act on real systems: calendars, CRM, payments."),
                ("Conversational assistants", "on WhatsApp, handing over to a person when needed."),
                ("Multiple LLM providers", "Claude, GPT, Gemini or DeepSeek, swappable without code changes."),
                ("RAG and structured output", "embeddings, semantic search and responses validated with Zod."),
                ("Prompts and evaluation", "prompt design and quality checks on the answers."),
            ]),
            ("In how I build", False, [
                ("Claude Code, Cursor and Copilot", "every day, with the judgement to review what they generate."),
                ("Agents and MCP", "to automate the team's repetitive work."),
                ("Python", "for scripts, data and automation."),
                ("AI-enabled teams", "workflows and practices so the team moves faster without losing quality."),
            ]),
        ],
        "projects_h": "Projects",
        "projects_intro": "The latest thing I've built, and some of the apps I've shipped to the stores.",
        "feature_kicker": "Freelance project, 2026",
        "feature_title": "Renacia Clinic's",
        "feature_text": "Website, AI WhatsApp assistant and management dashboard for a scalp micropigmentation clinic. "
                        "All in production and maintained by me.",
        "feature_points": [
            "The assistant answers on WhatsApp, checks availability and books the appointment in Google Calendar.",
            "The AI provider is picked by configuration: Claude today, another model tomorrow if it's cheaper.",
            "Dashboard for the clinic with client records, touch-ups, expenses, goals and KPIs.",
            "Fast public website with a blog and SEO, on Firebase Hosting.",
        ],
        "feature_link": "Visit the website",
        "apps_h": "Published apps",
        "clients_label": "I've also worked for",
        "exp_h": "Experience",
        "stack_h": "Stack",
        "edu_h": "Education",
        "contact_h": "Contact",
        "contact_intro": "Got a project, a team to lead or an AI idea? Tell me about it.",
        "call": "Call",
        "footer": "This site uses no cookies or analytics.",
        "stack": [
            ("Mobile", "Flutter, Dart, Android (Kotlin, Java), iOS (Swift), native plugins, App Store and Google Play"),
            ("Web", "React, Next.js, TypeScript, Angular, Node.js, HTML and CSS"),
            ("Cloud", "Google Cloud, Firebase (Firestore, Auth, Functions, App Hosting), AWS (Lambda, DynamoDB, Cognito, S3)"),
            ("Languages", "Dart, TypeScript, Python, Kotlin, Swift, C# and SQL"),
            ("Team", "CI/CD, Git, clean architecture, Scrum and code review"),
        ],
        "edu": [
            ("BSc in Computer Engineering", "Universitat Politècnica de València, 2012 – 2016"),
            ("MSc in Multiplatform App Development", "UPV, Gandia campus, 2016 – 2017"),
            ("MSc in Android App Development", "UPV, Gandia campus, 2017 – 2018"),
            ("Languages", "Spanish (native) and English (intermediate)"),
        ],
        "jobs": [
            ("Freelance developer, product and AI", "Renacia Clinic's", "", "2026 – present", True, [
                "Website, AI WhatsApp bot and management dashboard in production: Next.js, React and TypeScript on Firebase and Google Cloud.",
                "Agent built with the Vercel AI SDK and tool calling on the WhatsApp Cloud API, with a swappable LLM provider.",
            ]),
            ("Tech Lead", "We Are Cactus", "", "Apr 2025 – Aug 2026", False, [
                "Technical lead for the team: architecture, estimates, code review and mentoring, working directly with clients.",
                "Cross-platform apps in Flutter and web in React, backed by Firebase and Google Cloud.",
                "Brought generative AI into the product and into the team's daily workflow.",
            ]),
            ("Flutter Tech Lead", "Cuatroochenta", "Castellón", "Feb 2023 – Apr 2025", False, [
                "Led the Flutter team: architecture, code review, CI/CD and releases to the App Store and Google Play.",
            ]),
            ("CTO", "Darkan Technologies", "Madrid", "Mar 2021 – Feb 2023", False, [
                "Owned all of the startup's technology: Flutter app, AWS and Firebase backend, and website.",
                "User acquisition through Google Ads and Meta Ads campaigns.",
            ]),
            ("Senior Frontend Developer", "Epigram", "Valencia", "Apr 2019 – Mar 2021", False, [
                "Flutter apps and native iOS plugin development.",
            ]),
            ("Junior Frontend Developer", "Mobilendo", "Valencia", "Sep 2017 – Apr 2019", False, [
                "Hybrid apps with Ionic, virtual reality experiences in Unity and AWS services.",
            ]),
        ],
    },
}

# Ids de sección por idioma (anclas del menú)
IDS = {
    "es": {"ai": "ia", "projects": "proyectos", "exp": "experiencia", "contact": "contacto"},
    "en": {"ai": "ai", "projects": "projects", "exp": "experience", "contact": "contact"},
}

e = escape


def render(lang: str) -> str:
    c = CONTENT[lang]
    ids = IDS[lang]
    p = "../" if c["path"] else ""  # prefijo de rutas relativas
    url = f"{SITE_URL}/{c['path']}"
    other = "en" if lang == "es" else "es"
    other_url = f"{SITE_URL}/{CONTENT[other]['path']}"

    nav = "".join(f'<a href="{h}">{e(t)}</a>' for h, t in c["nav"])

    chat = "".join(
        f'<li class="msg {kind}">{e(text)}</li>' for kind, text in c["chat"]
    ) + '<li class="msg typing" aria-hidden="true"><i></i><i></i><i></i></li>'

    ai_cols = ""
    for title, primary, items in c["ai_cols"]:
        lis = "".join(f"<li><b>{e(b)}</b><span>{e(s)}</span></li>" for b, s in items)
        ai_cols += f'<div class="ai-col{" primary" if primary else ""}"><h3>{e(title)}</h3><ul>{lis}</ul></div>'

    points = "".join(f"<li>{e(x)}</li>" for x in c["feature_points"])
    tags = "".join(f"<li>{t}</li>" for t in
                   ["Next.js", "React", "TypeScript", "Firebase", "Google Cloud", "Vercel AI SDK", "Claude", "WhatsApp Cloud API"])

    apps = ""
    for name, img, ios, android in APPS:
        apps += (f'<li class="app"><img src="{p}img/{img}" alt="" width="56" height="56" loading="lazy">'
                 f'<b>{e(name)}</b><a href="{ios}" target="_blank" rel="noopener">App Store</a> '
                 f'<a href="{android}" target="_blank" rel="noopener">Google Play</a></li>')

    clients = CLIENTS if lang == "es" else CLIENTS.replace(" y el bus urbano de Alicante", " and Alicante's city buses")

    jobs = ""
    for role, org, place, when, now, bullets in c["jobs"]:
        place_html = f" <span>{e(place)}</span>" if place else ""
        lis = "".join(f"<li>{e(b)}</li>" for b in bullets)
        jobs += (f'<li{" class=\"now\"" if now else ""}><div class="job-head"><h3>{e(role)}</h3>'
                 f'<span class="job-when">{e(when)}</span></div>'
                 f'<p class="job-org">{e(org)}{place_html}</p><ul>{lis}</ul></li>')

    stack = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in c["stack"])
    edu = "".join(f"<li><b>{e(k)}</b><span>{e(v)}</span></li>" for k, v in c["edu"])

    person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Rodrigo Ballesteros Cabañas",
        "jobTitle": "Tech Lead",
        "url": url,
        "image": f"{SITE_URL}/img/rodrigo.jpg",
        "email": f"mailto:{EMAIL}",
        "address": {"@type": "PostalAddress", "addressLocality": "Utiel", "addressRegion": "Valencia", "addressCountry": "ES"},
        "sameAs": [LINKEDIN, GITHUB],
        "knowsAbout": ["Flutter", "Generative AI", "LLM agents", "React", "Next.js", "Firebase", "Google Cloud", "Python"],
        "alumniOf": "Universitat Politècnica de València",
    }

    lang_href, lang_label, lang_title = c["lang_switch"]

    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(c["title"])}</title>
<meta name="description" content="{e(c["description"])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="{lang}" href="{url}">
<link rel="alternate" hreflang="{other}" href="{other_url}">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}/">
<meta property="og:type" content="profile">
<meta property="og:title" content="{e(c["title"])}">
<meta property="og:description" content="{e(c["description"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/img/og.jpg">
<meta property="og:locale" content="{c["og_locale"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1b56c8">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/site.css">
<script>document.documentElement.classList.add("js")</script>
<script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">{e(c["skip"])}</a>

<header class="top">
  <div class="wrap">
    <a class="brand" href="./">Rodrigo Ballesteros</a>
    <nav class="nav" aria-label="Secciones">{nav}</nav>
    <div class="top-actions">
      <a class="lang" href="{lang_href}" hreflang="{other}" title="{e(lang_title)}">{lang_label}</a>
      <a class="btn btn-ghost btn-sm" href="{p}{CV_PDF}" download>{e(c["cv_btn"])}</a>
    </div>
  </div>
</header>

<main id="main">
  <section class="hero">
    <div class="wrap">
      <div>
        <div class="who">
          <img src="{p}img/rodrigo.jpg" alt="Rodrigo Ballesteros Cabañas" width="56" height="56">
          <div><strong>Rodrigo Ballesteros Cabañas</strong><span>{e(c["role"])}</span></div>
        </div>
        <h1>{e(c["h1"])}</h1>
        <p class="lead">{e(c["lead"])}</p>
        <div class="cta">
          <a class="btn btn-primary" href="mailto:{EMAIL}">{e(c["cta_mail"])}</a>
          <a class="btn btn-ghost" href="{p}{CV_PDF}" download>{e(c["cta_cv"])}</a>
        </div>
        <p class="availability">{e(c["availability"])}</p>
      </div>
      <figure style="margin:0">
        <div class="phone">
          <div class="phone-bar"><span class="dot">R</span><div><b>{e(c["chat_name"])}</b><small>{e(c["chat_status"])}</small></div></div>
          <ul class="chat" aria-label="{e(c["chat_caption"])}">{chat}</ul>
        </div>
        <figcaption class="phone-caption">{e(c["chat_caption"])} <button class="replay" type="button">{e(c["replay"])}</button></figcaption>
      </figure>
    </div>
  </section>

  <section class="block" id="{ids["ai"]}">
    <div class="wrap">
      <h2>{e(c["ai_h"])}</h2>
      <p class="intro">{e(c["ai_intro"])}</p>
      <div class="ai-grid">{ai_cols}</div>
    </div>
  </section>

  <section class="block" id="{ids["projects"]}">
    <div class="wrap">
      <h2>{e(c["projects_h"])}</h2>
      <p class="intro">{e(c["projects_intro"])}</p>
      <article class="feature">
        <div>
          <p class="kicker">{e(c["feature_kicker"])}</p>
          <h3>{e(c["feature_title"])}</h3>
          <p>{e(c["feature_text"])}</p>
          <ul class="tags">{tags}</ul>
          <a class="btn btn-ghost btn-sm" href="https://renacia-clinic-s.web.app" target="_blank" rel="noopener">{e(c["feature_link"])}</a>
        </div>
        <ul>{points}</ul>
      </article>
      <h3 class="apps-title">{e(c["apps_h"])}</h3>
      <ul class="apps">{apps}</ul>
      <p class="clients"><b>{e(c["clients_label"])}:</b> {e(clients)}.</p>
    </div>
  </section>

  <section class="block" id="{ids["exp"]}">
    <div class="wrap">
      <h2>{e(c["exp_h"])}</h2>
      <ol class="timeline" reversed>{jobs}</ol>
    </div>
  </section>

  <section class="block">
    <div class="wrap two">
      <div><h2>{e(c["stack_h"])}</h2><dl class="stack">{stack}</dl></div>
      <div><h2>{e(c["edu_h"])}</h2><ul class="edu">{edu}</ul></div>
    </div>
  </section>

  <section class="block" id="{ids["contact"]}">
    <div class="wrap">
      <h2>{e(c["contact_h"])}</h2>
      <p class="intro">{e(c["contact_intro"])}</p>
      <a class="contact-mail" href="mailto:{EMAIL}">{EMAIL}</a>
      <div class="contact-links">
        <a class="btn btn-ghost btn-sm" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
        <a class="btn btn-ghost btn-sm" href="{GITHUB}" target="_blank" rel="noopener">GitHub</a>
        <a class="btn btn-ghost btn-sm" href="tel:{PHONE.replace(' ', '')}">{e(c["call"])} {PHONE}</a>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap"><span>© 2026 Rodrigo Ballesteros Cabañas</span><span>{e(c["footer"])}</span></div>
</footer>
<script src="{p}assets/site.js" defer></script>
</body>
</html>
"""


NOT_FOUND = """<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Página no encontrada · Rodrigo Ballesteros</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Source+Sans+3:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css"></head>
<body><main class="wrap" style="padding-block:18vh">
<h1>Esta página no existe.</h1>
<p class="lead">Puede que el enlace sea antiguo. This page doesn't exist.</p>
<div class="cta"><a class="btn btn-primary" href="/">Ir al inicio</a><a class="btn btn-ghost" href="/en/">English</a></div>
</main></body></html>
"""


def main() -> None:
    (PUBLIC / "en").mkdir(parents=True, exist_ok=True)
    (PUBLIC / "index.html").write_text(render("es"), encoding="utf-8")
    (PUBLIC / "en" / "index.html").write_text(render("en"), encoding="utf-8")
    (PUBLIC / "404.html").write_text(NOT_FOUND, encoding="utf-8")
    print("OK: public/index.html, public/en/index.html, public/404.html")


if __name__ == "__main__":
    main()
