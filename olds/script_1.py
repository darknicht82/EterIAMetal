
# Crear estructura detallada de metaetiquetas para SUNO V5
metatags_data = """
GUÍA COMPLETA DE METAETIQUETAS SUNO V5 - METAL
================================================================

1. ETIQUETAS DE ESTRUCTURA (Obligatorias en Lyrics)
   [Intro] - Introducción instrumental o atmosférica
   [Verse] - Verso principal, desarrollo narrativo
   [Pre-Chorus] - Construcción de tensión hacia el coro
   [Chorus] - Gancho principal, sección memorable
   [Bridge] - Contraste musical, cambio de perspectiva
   [Guitar Solo] - Solo de guitarra instrumental
   [Breakdown] - Sección pesada, tempo reducido (metalcore)
   [Instrumental] - Pasaje completamente instrumental
   [Outro] - Cierre, conclusión de la canción

2. ETIQUETAS VOCALES (Colocar al inicio de sección)
   GÉNERO/ESTILO:
   - [Male Vocalist] / [Female Vocalist]
   - [High Male Vocals] / [Deep Male Vocals]
   - [Operatic Female Vocals] / [Alto Female Vocals]
   - [Soprano Vocals] / [Baritone Vocals]
   
   TÉCNICA METAL:
   - [Gritty Vocals] - Voz áspera, rockera
   - [Screaming Vocals] - Gritos metalcore
   - [Growling Vocals] - Guturales death metal
   - [Clean Vocals] - Voz limpia
   - [Raspy Vocals] - Voz ronca
   - [Powerful Vocals] - Voz potente
   
   EFECTOS:
   - [Harmonized Chorus] - Coro armonizado
   - [Layered Vocals] - Voces en capas
   - [Group Chant] - Coro grupal
   - [Cinematic Choirs] - Coros cinematográficos
   - [Whispered Vocals] - Susurros
   - [Spoken Word] - Palabra hablada

3. ETIQUETAS INSTRUMENTALES (En Style o Lyrics)
   GUITARRA:
   - [Shredding Electric Guitar Solo] - Solo virtuoso
   - [Palm-Muted Guitar Riff] - Riff con palm mute
   - [Heavy Slow Riffing] - Riffs lentos pesados
   - [Distorted Electric Guitar] - Guitarra distorsionada
   - [Classical Guitar Arpeggios] - Arpegios clásicos
   - [Acoustic Guitar] - Guitarra acústica
   
   BATERÍA:
   - [Fast-Paced Drumming] - Batería rápida
   - [Double Bass Drum] - Doble bombo
   - [Tribal Drums] - Percusión tribal
   - [Slow Tempo Drums] - Batería tempo lento
   
   TECLADOS/ORQUESTA:
   - [Epic Cinematic Orchestra] - Orquesta cinematográfica
   - [Orchestral Strings] - Cuerdas orquestales
   - [Heavy Organ] - Órgano pesado
   - [Hammond Organ] - Órgano Hammond
   - [Synth Pads] - Pads de sintetizador
   - [Harpsichord] - Clavecín
   
   OTROS:
   - [Fuzzy Bass] - Bajo con fuzz
   - [Heavy Bass Drop] - Caída de bajo pesado
   - [Bagpipes] / [Fiddle] - Instrumentos folk
   - [Atmospheric Soundscape] - Paisaje atmosférico

4. ETIQUETAS DE DINÁMICA Y ENERGÍA
   - [Building Intensity] - Incremento de intensidad
   - [Climactic] - Clímax
   - [Powerful Outro] - Final poderoso
   - [Soft Intro] - Intro suave
   - [Emotional Build-up] - Construcción emocional
   - [Anthemic Chorus] - Coro himno

5. ETIQUETAS DE PRODUCCIÓN/EFECTOS
   - [Reverb Heavy] - Mucha reverberación
   - [Guitars with Heavy Reverb] - Guitarras con reverb
   - [Atmospheric] - Atmosférico
   - [Cinematic] - Cinematográfico
   - [Raw] - Crudo, sin procesar
   - [Polished] - Pulido, producción limpia
"""

print(metatags_data)

# Crear tabla de exclude styles comunes
exclude_data = {
    'Subgénero Metal': [
        'Power Metal',
        'Metal Sinfónico',
        'Goth/Doom Metal',
        'Metalcore',
        'Folk Metal'
    ],
    'Exclude Styles Recomendados': [
        'pop vocals, electronic beats, light drums, soft vocals',
        'harsh vocals, screaming, raw production',
        'upbeat, cheerful, pop vocals, electronic',
        'soft vocals, acoustic, mellow',
        'electronic, synth-heavy, urban'
    ],
    'Razón': [
        'Evitar sonidos pop/comerciales que reduzcan el impacto épico',
        'Mantener elegancia y limpieza vocal operática',
        'Preservar atmósfera oscura y melancólica',
        'Conservar agresividad y energía moderna',
        'Mantener autenticidad orgánica de instrumentos tradicionales'
    ]
}

df_exclude = pd.DataFrame(exclude_data)
print("\n\nEXCLUDE STYLES - GUÍA DE EXCLUSIONES POR SUBGÉNERO")
print("="*120)
print(df_exclude.to_string(index=False))
