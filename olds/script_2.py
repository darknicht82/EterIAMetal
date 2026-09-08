
# Crear un resumen ejecutivo con los hallazgos clave de la investigación
resumen = """
╔══════════════════════════════════════════════════════════════════════════════╗
║          RESUMEN EJECUTIVO - INVESTIGACIÓN SUNO V5 PARA METAL                ║
╚══════════════════════════════════════════════════════════════════════════════╝

📊 HALLAZGOS CLAVE DE LA INVESTIGACIÓN (36 fuentes analizadas):

1. ADVANCED OPTIONS - SLIDERS (Fuentes: web:1, web:4, web:7, web:13)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ✓ Los sliders NO necesitan sumar 100% - son independientes
   ✓ Weirdness: 50% = normal, >70% = experimental/caótico
   ✓ Style Influence: Alto (80-100%) = adhesión estricta al género
   ✓ Audio Influence: Solo aparece con Personas, controla fidelidad al original
   ✓ Para metal: Weirdness 50-70%, Style Influence 90%, Audio Inf. 70-100%

2. METAETIQUETAS V5 (Fuentes: web:2, web:3, web:5, web:8, web:19)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ✓ V5 respeta mejor las etiquetas que V4.5
   ✓ Colocar etiquetas en los primeros 20-30 palabras del prompt
   ✓ Etiquetas de estructura: [Intro], [Verse], [Chorus], [Bridge], [Outro]
   ✓ Etiquetas vocales: [Male Vocals], [Female Vocals], [Operatic], [Screaming]
   ✓ Etiquetas instrumentales: [Guitar Solo], [Fast Drumming], [Orchestra]
   ✓ Stackear etiquetas con "|": [Chorus | Anthemic | Harmonized Vocals]

3. TEMPO Y BPM (Fuentes: web:21, web:26, web:30, web:33)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ✓ PROBLEMA REPORTADO: V5 tiende a reducir BPM solicitado
   ✓ Power Metal: 145-180 BPM (puede salir 120-140 en V5)
   ✓ Doom/Goth: 60-120 BPM (funciona mejor)
   ✓ Metalcore: 160-190 BPM (verificar con [Tempo: XXX BPM] explícito)
   ✓ SOLUCIÓN: Especificar BPM múltiples veces en prompt y lyrics

4. VOCES MASCULINAS VS FEMENINAS (Fuentes: web:22, web:24, web:31, web:36)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ✓ PROBLEMA: V5 tiende a generar voces femeninas por defecto
   ✓ SOLUCIÓN 1: Especificar [Male Vocals] en Style Y en cada sección de Lyrics
   ✓ SOLUCIÓN 2: Usar descriptores específicos: [Deep Male Vocals], [Baritone]
   ✓ SOLUCIÓN 3: Usar Advanced Options > Vocal Gender selector
   ✓ Para Power Metal femenino estilo Dio: [Female Vocalist, Powerful, Gritty]

5. METAETIQUETAS ESPECÍFICAS DE METAL (Fuentes: web:23, web:25, web:28, web:32)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ✓ Guitarra: [Shredding Guitar Solo], [Palm-Muted Riff], [Distorted Guitar]
   ✓ Batería: [Fast-Paced Drumming], [Double Bass Drum], [Tribal Drums]
   ✓ Voces: [Gritty], [Screaming], [Growling], [Operatic], [Harmonized]
   ✓ Efectos: [Reverb Heavy], [Atmospheric], [Cinematic], [Raw]
   ✓ Dinámica: [Building Intensity], [Climactic], [Anthemic Chorus]

6. SUBGÉNEROS ESPECÍFICOS (Fuentes: web:37, web:38, web:40, web:41)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ✓ Goth Metal: "dark gothic metal", tempo lento, [melancholic tone]
   ✓ Doom Metal: "traditional doom metal", 60-80 BPM, [slow crushing riffs]
   ✓ Symphonic: "epic symphonic metal", [orchestral strings], [opera vocals]
   ✓ Neoclassical: "neoclassical power metal", [classical guitar], [harpsichord]
   ✓ Folk Metal: "celtic folk metal", [bagpipes], [fiddle], [tribal drums]

7. ESTRUCTURA LÍRICA (Fuentes: web:39, web:42, web:51, web:53)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ✓ Conteo de sílabas: 6-10 por línea (rango seguro)
   ✓ Verso: 6-10 sílabas, narrativo, ABAB o AABB
   ✓ Coro: 6-8 sílabas, pegadizo, AABB preferido
   ✓ Pre-Coro: 8-12 sílabas, construcción de tensión
   ✓ Rima multisílaba: Mejora musicalidad (ej: "conquistar" / "dominar")
   ✓ Acentos naturales: Sílabas fuertes en tiempos fuertes

8. MEJORES PRÁCTICAS V5 (Fuentes: web:3, web:4, web:11, web:19)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ✓ Front-load control: Etiquetas principales en primeras 3-5 líneas
   ✓ Concisión: 1-2 géneros + 1 mood + instrumentos opcionales
   ✓ Callbacks: "continue with same vibe as chorus" funciona en V5
   ✓ Exclude Styles: Filtros negativos funcionan mejor en V5
   ✓ Personas: Mantienen timbre vocal consistente a través de la canción
   ✓ Studio Timeline: Permite editar secciones con Replace/Extend

9. PROBLEMAS COMUNES V5 Y SOLUCIONES (Fuentes: web:9, web:30, web:33)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ✗ PROBLEMA: Metal pierde agresividad, se convierte en mid-tempo rock
     ✓ SOLUCIÓN: Especificar "aggressive", "heavy", BPM exacto múltiples veces
   
   ✗ PROBLEMA: BPM ignorado (ej: pides 180, obtienes 110)
     ✓ SOLUCIÓN: [Tempo: 180 BPM] en parámetros Y en descripción style
   
   ✗ PROBLEMA: Voces incorrectas (femeninas cuando pides masculinas)
     ✓ SOLUCIÓN: [Male Vocals] en CADA sección de lyrics
   
   ✗ PROBLEMA: Melisma excesivo en voces
     ✓ SOLUCIÓN: Añadir "straight delivery", "no runs", "direct vocals"

10. EXCLUDE STYLES (Nuevo en V5) (Fuentes: web:3, web:8, web:19)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ✓ Power Metal: Exclude "pop vocals, electronic beats, soft vocals"
    ✓ Symphonic: Exclude "harsh vocals, screaming, raw production"
    ✓ Goth/Doom: Exclude "upbeat, cheerful, pop vocals"
    ✓ Metalcore: Exclude "soft vocals, acoustic, mellow"
    ✓ Folk Metal: Exclude "electronic, synth-heavy, urban"

╔══════════════════════════════════════════════════════════════════════════════╗
║                      CONFIGURACIÓN ÓPTIMA GENERAL                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

Advanced Options:
  Weirdness:        60% (variación creativa moderada)
  Style Influence:  90% (adhesión fuerte al género)
  Audio Influence:  80% (si usas Persona)

Estructura Lyrics:
  Sílabas/línea:    6-10 (verso), 6-8 (coro), 8-12 (puente)
  Patrón rima:      ABAB (verso), AABB (coro)
  Etiquetas:        Al inicio de CADA sección

Parámetros Globales:
  [Title: "..."]
  [Genre: específico según subgénero]
  [Tempo: XXX BPM] (repetir en style description)
  [Key: E Minor, D Minor, etc.]
  Exclude Styles: (filtros negativos)

╔══════════════════════════════════════════════════════════════════════════════╗
║                           FUENTES CONSULTADAS                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Total de fuentes web analizadas: 36
- Documentación oficial Suno AI
- Tutoriales especializados en metal (Jack Righteous, Suno Wiki)
- Guías de metaetiquetas y prompting
- Comunidades Reddit (r/SunoAI)
- Reportes de usuarios sobre V5 vs V4.5
- Guías de escritura lírica para metal
"""

print(resumen)
