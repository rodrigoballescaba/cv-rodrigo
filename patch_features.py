#!/usr/bin/env python3
"""Patch build.py: single featured project -> features list (16 projects), ES+EN."""
import io

P = '/home/hatch/workspace/cv/build.py'
src = open(P, encoding='utf-8').read()

ES_FEATURES = '''\
        "features": [
            {"kicker": "Proyecto freelance, 2026", "title": "Renacia Clinic's",
             "text": "Web, asistente de WhatsApp con IA y panel de gestión para una clínica de micropigmentación capilar. Todo en producción y mantenido por mí.",
             "tags": ["Next.js", "React", "TypeScript", "Firebase", "Google Cloud", "Vercel AI SDK", "Claude", "WhatsApp Cloud API"],
             "url": "https://renaciaclinics.com", "link": "Ver la web",
             "points": [
                 "El asistente responde por WhatsApp, consulta huecos y reserva la cita en Google Calendar.",
                 "El proveedor de IA se elige por configuración: Claude hoy, otro modelo mañana si sale más barato.",
                 "Panel para la clínica con fichas de clientes, retoques, gastos, objetivos y KPIs.",
                 "Web pública rápida, con blog y SEO, en Firebase Hosting."]},
            {"kicker": "Proyecto freelance, 2026", "title": "Club Natación Utiel",
             "text": "App móvil y panel web para un club de natación: inscripciones, cuotas y libro de movimientos con pagos online.",
             "tags": ["Flutter", "Firebase", "Cloud Functions", "Stripe"],
             "url": "https://cnu-utiel.web.app", "link": "Ver el panel",
             "points": [
                 "App y panel con autenticación, roles y datos en tiempo real sobre Firestore.",
                 "Cobros con Stripe y libro de movimientos con importes exactos."]},
            {"kicker": "Proyecto freelance, 2026", "title": "La Capitana",
             "text": "Juego de dados multijugador en tiempo real, con economía interna, tienda y mercado entre jugadores.",
             "tags": ["Flutter", "Firebase", "Cloud Functions"],
             "url": "https://la-capitana-c5b09.web.app", "link": "Ver el juego",
             "points": [
                 "Partidas multijugador con emparejamiento y validación de turnos en servidor.",
                 "Economía con recompensas, tienda y mercado P2P con custodia."]},
            {"kicker": "Proyecto propio, 2026", "title": "70casos.com — «Dale el trabajo a la IA»",
             "text": "Web y libro sobre IA aplicada a negocios reales: 70 casos documentados, publicado en Amazon.",
             "tags": ["Web", "Firebase", "SEO", "Amazon KDP"],
             "url": "https://70casos.com", "link": "Ver la web",
             "points": [
                 "Web rápida con 70 casos, blog y analítica propia sin cookies.",
                 "Libro publicado en Amazon (tapa blanda, tapa dura y Kindle)."]},
            {"kicker": "Proyecto freelance, 2026", "title": "Núcleo · Pack inmobiliario con IA",
             "text": "Plataforma que convierte tours virtuales Matterport en vídeos promocionales generados con IA para inmobiliarias.",
             "tags": ["Python", "IA generativa", "Vídeo", "Firebase"],
             "url": "https://nucleo-pack-demo.web.app", "link": "Ver la demo",
             "points": [
                 "Extracción de datos 3D de tours Matterport y generación de vídeo automatizada.",
                 "Demos interactivas por vertical: inmobiliaria, clínica, taller y restauración."]},
            {"kicker": "Proyecto freelance, 2025", "title": "Les Coves del Xuquer",
             "text": "Web y sistema de asistencia para el alojamiento Les Coves del Xuquer.",
             "tags": ["Web", "Firebase"],
             "url": None, "link": "Ver la web",
             "points": ["Web del alojamiento con reservas y atención al huésped."]},
            {"kicker": "Proyecto freelance, 2026", "title": "Garzarón",
             "text": "Web y app para el restaurante Garzarón: digitalización para hostelería local.",
             "tags": ["TypeScript", "Firebase"],
             "url": None, "link": "Ver la web",
             "points": ["Carta digital, reservas y panel de gestión."]},
            {"kicker": "Proyecto freelance, 2026", "title": "Karamelos",
             "text": "Digitalización para Karamelos (hostelería).",
             "tags": ["TypeScript", "Firebase"],
             "url": None, "link": "Ver la web",
             "points": ["Web y herramientas digitales para el negocio."]},
            {"kicker": "Proyecto freelance, 2026", "title": "Canaima VIP",
             "text": "Panel de gestión para el restaurante: caja diaria, turnos, cuadre y reparto por trabajador.",
             "tags": ["TypeScript", "Firebase"],
             "url": None, "link": "Ver el panel",
             "points": ["Resumen del día, movimientos con filtros y cierre de turno con diferencias."]},
            {"kicker": "Proyecto freelance, 2025", "title": "Doctor Shoes Phone",
             "text": "Web y sistema digital para el negocio de reparaciones.",
             "tags": ["JavaScript", "Firebase"],
             "url": None, "link": "Ver la web",
             "points": ["Digitalización de un taller de reparaciones local."]},
            {"kicker": "Proyecto freelance, 2026", "title": "Ruta 66",
             "text": "Web y digitalización para Ruta 66.",
             "tags": ["Web", "Firebase"],
             "url": None, "link": "Ver la web",
             "points": ["Presencia digital y herramientas para el negocio."]},
            {"kicker": "Proyecto freelance, 2026", "title": "Gruterval",
             "text": "App del proyecto GRUT.",
             "tags": ["Flutter", "Firebase"],
             "url": None, "link": "Ver la app",
             "points": ["App multiplataforma con backend en Firebase."]},
            {"kicker": "Proyecto freelance, 2026", "title": "tomasviana.es",
             "text": "Web del artista Tomás Viana: se actualiza sola y trabaja el SEO.",
             "tags": ["Web", "SEO"],
             "url": "https://tomasviana.es", "link": "Ver la web",
             "points": ["Web autogestionada con posicionamiento en Google."]},
            {"kicker": "Proyecto freelance, 2026", "title": "Llevant Patrimonial",
             "text": "Web inmobiliaria multiidioma con captación de propiedades y tasación.",
             "tags": ["Web", "Firebase"],
             "url": None, "link": "Ver la web",
             "points": ["Portal en 9 idiomas con proceso de venta en 4 pasos."]},
            {"kicker": "Proyecto freelance, 2026", "title": "Jeván Patrimonial",
             "text": "Web corporativa de Jeván Patrimonial, empresa de limpieza en Cullera (Valencia).",
             "tags": ["Web"],
             "url": None, "link": "Ver la web",
             "points": ["Web corporativa con presencia local."]},
            {"kicker": "Proyecto propio, en curso", "title": "Sereno · AI Work OS",
             "text": "Plataforma de orquestación de agentes de IA para negocios.",
             "tags": ["TypeScript", "Agentes IA"],
             "url": None, "link": "Ver el proyecto",
             "points": ["Agentes que automatizan procesos de negocio por WhatsApp."]},
        ],
'''

EN_FEATURES = '''\
        "features": [
            {"kicker": "Freelance project, 2026", "title": "Renacia Clinic's",
             "text": "Website, AI WhatsApp assistant and management dashboard for a scalp micropigmentation clinic. All in production and maintained by me.",
             "tags": ["Next.js", "React", "TypeScript", "Firebase", "Google Cloud", "Vercel AI SDK", "Claude", "WhatsApp Cloud API"],
             "url": "https://renaciaclinics.com", "link": "Visit the website",
             "points": [
                 "The assistant answers on WhatsApp, checks availability and books the appointment in Google Calendar.",
                 "The AI provider is picked by configuration: Claude today, another model tomorrow if it's cheaper.",
                 "Dashboard for the clinic with client records, touch-ups, expenses, goals and KPIs.",
                 "Fast public website with a blog and SEO, on Firebase Hosting."]},
            {"kicker": "Freelance project, 2026", "title": "Club Natación Utiel",
             "text": "Mobile app and web dashboard for a swimming club: registrations, fees and a ledger with online payments.",
             "tags": ["Flutter", "Firebase", "Cloud Functions", "Stripe"],
             "url": "https://cnu-utiel.web.app", "link": "View the dashboard",
             "points": [
                 "App and dashboard with auth, roles and realtime data on Firestore.",
                 "Stripe payments and a ledger with exact amounts."]},
            {"kicker": "Freelance project, 2026", "title": "La Capitana",
             "text": "Realtime multiplayer dice game, with an internal economy, shop and player market.",
             "tags": ["Flutter", "Firebase", "Cloud Functions"],
             "url": "https://la-capitana-c5b09.web.app", "link": "View the game",
             "points": [
                 "Multiplayer matches with matchmaking and server-side turn validation.",
                 "Economy with rewards, a shop and a P2P market with escrow."]},
            {"kicker": "Own project, 2026", "title": "70casos.com — AI at work",
             "text": "Website and book on applied AI for real businesses: 70 documented cases, published on Amazon.",
             "tags": ["Web", "Firebase", "SEO", "Amazon KDP"],
             "url": "https://70casos.com", "link": "Visit the website",
             "points": [
                 "Fast website with 70 cases, a blog and cookie-free analytics.",
                 "Book published on Amazon (paperback, hardcover and Kindle)."]},
            {"kicker": "Freelance project, 2026", "title": "Núcleo · AI real-estate pack",
             "text": "Platform that turns Matterport virtual tours into AI-generated promo videos for estate agents.",
             "tags": ["Python", "Generative AI", "Video", "Firebase"],
             "url": "https://nucleo-pack-demo.web.app", "link": "View the demo",
             "points": [
                 "3D data extraction from Matterport tours and automated video generation.",
                 "Interactive demos per vertical: real estate, clinic, workshop and restaurants."]},
            {"kicker": "Freelance project, 2025", "title": "Les Coves del Xuquer",
             "text": "Website and assistance system for the Les Coves del Xuquer accommodation.",
             "tags": ["Web", "Firebase"],
             "url": None, "link": "Visit the website",
             "points": ["Accommodation website with bookings and guest support."]},
            {"kicker": "Freelance project, 2026", "title": "Garzarón",
             "text": "Website and app for the Garzarón restaurant: digitalisation for local hospitality.",
             "tags": ["TypeScript", "Firebase"],
             "url": None, "link": "Visit the website",
             "points": ["Digital menu, bookings and a management dashboard."]},
            {"kicker": "Freelance project, 2026", "title": "Karamelos",
             "text": "Digitalisation for Karamelos (hospitality).",
             "tags": ["TypeScript", "Firebase"],
             "url": None, "link": "Visit the website",
             "points": ["Website and digital tools for the business."]},
            {"kicker": "Freelance project, 2026", "title": "Canaima VIP",
             "text": "Management dashboard for the restaurant: daily cash, shifts, balancing and payout per worker.",
             "tags": ["TypeScript", "Firebase"],
             "url": None, "link": "View the dashboard",
             "points": ["Day summary, filtered movements and shift closing with differences."]},
            {"kicker": "Freelance project, 2025", "title": "Doctor Shoes Phone",
             "text": "Website and digital system for the repair shop.",
             "tags": ["JavaScript", "Firebase"],
             "url": None, "link": "Visit the website",
             "points": ["Digitalisation of a local repair business."]},
            {"kicker": "Freelance project, 2026", "title": "Ruta 66",
             "text": "Website and digitalisation for Ruta 66.",
             "tags": ["Web", "Firebase"],
             "url": None, "link": "Visit the website",
             "points": ["Digital presence and tools for the business."]},
            {"kicker": "Freelance project, 2026", "title": "Gruterval",
             "text": "App for the GRUT project.",
             "tags": ["Flutter", "Firebase"],
             "url": None, "link": "View the app",
             "points": ["Cross-platform app with a Firebase backend."]},
            {"kicker": "Freelance project, 2026", "title": "tomasviana.es",
             "text": "Website for the artist Tomás Viana: self-updating, with SEO work.",
             "tags": ["Web", "SEO"],
             "url": "https://tomasviana.es", "link": "Visit the website",
             "points": ["Self-managed website ranking on Google."]},
            {"kicker": "Freelance project, 2026", "title": "Llevant Patrimonial",
             "text": "Multi-language real-estate website with property intake and valuations.",
             "tags": ["Web", "Firebase"],
             "url": None, "link": "Visit the website",
             "points": ["Portal in 9 languages with a 4-step selling process."]},
            {"kicker": "Freelance project, 2026", "title": "Jeván Patrimonial",
             "text": "Corporate website for Jeván Patrimonial, a cleaning company in Cullera (Valencia).",
             "tags": ["Web"],
             "url": None, "link": "Visit the website",
             "points": ["Corporate website with a local presence."]},
            {"kicker": "Own project, in progress", "title": "Sereno · AI Work OS",
             "text": "Agent orchestration platform: AI agents for businesses.",
             "tags": ["TypeScript", "AI agents"],
             "url": None, "link": "View the project",
             "points": ["Agents that automate business processes over WhatsApp."]},
        ],
'''

# --- replace ES data block ---
old_es = '''\
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
'''
assert old_es in src, "ES block not found"
src = src.replace(old_es, ES_FEATURES)

old_en = '''\
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
'''
assert old_en in src, "EN block not found"
src = src.replace(old_en, EN_FEATURES)

# --- replace render code ---
old_render = '''\
    points = "".join(f"<li>{e(x)}</li>" for x in c["feature_points"])
    tags = "".join(f"<li>{t}</li>" for t in
                   ["Next.js", "React", "TypeScript", "Firebase", "Google Cloud", "Vercel AI SDK", "Claude", "WhatsApp Cloud API"])
'''
new_render = '''\
    features_html = ""
    for f in c["features"]:
        f_tags = "".join(f"<li>{e(t)}</li>" for t in f["tags"])
        f_points = "".join(f"<li>{e(x)}</li>" for x in f["points"])
        f_link = (f'<a class="btn btn-ghost btn-sm" href="{f["url"]}" target="_blank" rel="noopener">{e(f["link"])}</a>'
                  if f.get("url") else "")
        features_html += (
            '<article class="feature"><div>'
            f'<p class="kicker">{e(f["kicker"])}</p><h3>{e(f["title"])}</h3><p>{e(f["text"])}</p>'
            f'<ul class="tags">{f_tags}</ul>{f_link}'
            f'</div><ul>{f_points}</ul></article>'
        )
'''
assert old_render in src, "render block not found"
src = src.replace(old_render, new_render)

old_article = '''\
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
'''
assert old_article in src, "article template not found"
src = src.replace(old_article, '      {features_html}\n')

open(P, 'w', encoding='utf-8').write(src)
print("patched OK")
