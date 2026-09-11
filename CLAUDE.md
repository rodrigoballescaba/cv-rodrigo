# rodrigoballescaba.app

Web personal de Rodrigo (portfolio + CV). Estática, en Firebase Hosting, proyecto `cv-rodrigo-b28a1`.
Repo `rodrigoballescaba/cv-rodrigo` (público: no subir nada privado).

## Estructura

- `build.py`: todo el texto (ES y EN) en `CONTENT`. Genera `public/index.html`, `public/en/index.html` y `public/404.html`.
  Nunca editar esos HTML a mano: cambiar `build.py` y regenerar.
- `public/assets/site.css` y `site.js`: estilos y la animación del chat del hero.
- `public/img/`: foto e iconos ya redimensionados. `public/cv/`: el PDF del CV.
- El CV editable está fuera del repo, en `Desktop/2026/RODRIGO/CV/cv.html`. Al cambiarlo, exportar el PDF y copiarlo a `public/cv/rodrigo-ballesteros-cv.pdf`.

## Comandos

```bash
python build.py
firebase deploy --only hosting --project cv-rodrigo-b28a1   # con la cuenta rodrigoballescaba@gmail.com
git add -A && git commit && git push
```

## Reglas

- La demo del chat solo muestra lo que el bot de Renacia hace de verdad (consultar huecos, reservar en Google Calendar, pedir el nombre).
- Sin cookies ni analítica (el pie lo dice).
- Títulos de 60 caracteres como máximo.
