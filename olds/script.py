
# Crear una tabla resumida de configuraciones óptimas para SUNO V5 basada en la investigación
import pandas as pd

# Datos de configuración para cada subgénero de metal
metal_config = {
    'Subgénero': [
        'Power Metal',
        'Metal Sinfónico',
        'Goth Metal',
        'Doom Metal',
        'Metalcore Melódico',
        'Folk Metal',
        'Neoclassical Metal',
        'Heavy Metal Clásico'
    ],
    'Género/Era Suno': [
        '80s melodic power metal',
        'epic symphonic metal',
        'dark gothic metal',
        'traditional doom metal',
        'melodic metalcore, modern',
        'celtic folk metal',
        'neoclassical power metal',
        'classic heavy metal, 80s'
    ],
    'Tempo BPM': [
        '145-180',
        '130-160',
        '90-120',
        '60-80',
        '160-190',
        '130-160',
        '140-170',
        '110-140'
    ],
    'Voces Prioritarias': [
        '[high male vocals, melodic range], [harmonized chorus]',
        '[high female vocals, operatic style], [cinematic choirs]',
        '[deep male vocals, low range], [melancholic tone]',
        '[deep male vocals, powerful], [clean male vocals, dark tone]',
        '[screaming vocals], [clean male vocals, aggressive]',
        '[powerful male vocals], [group chant chorus]',
        '[virtuoso vocals], [high range], [classical precision]',
        '[gritty vocals], [strong], [dynamic range]'
    ],
    'Instrumentación Clave': [
        '[fast-paced drumming], [shredding electric guitar solo], [heavy organ]',
        '[epic cinematic orchestra], [double bass drum], [orchestral strings]',
        '[heavy slow riffing], [guitars with heavy reverb], [synth pads]',
        '[slow tempo], [heavy slow riffing], [fuzzy bass], [atmospheric soundscape]',
        '[fast-paced drumming], [palm-muted guitar riff], [heavy bass drop]',
        '[bagpipes/fiddle], [acoustic guitar], [tribal drums]',
        '[classical guitar arpeggios], [harpsichord], [virtuoso guitar solos]',
        '[electric guitar, overdrive], [hammond organ], [powerful drums]'
    ]
}

df_config = pd.DataFrame(metal_config)
print("TABLA DE CONFIGURACIONES ÓPTIMAS PARA SUNO V5 - METAL")
print("="*120)
print(df_config.to_string(index=False))
print("\n")

# Datos de Advanced Options
advanced_options = {
    'Parámetro': ['Weirdness', 'Style Influence', 'Audio Influence (con Persona)'],
    'Rango': ['0-100%', '0-100%', '0-100%'],
    'Default': ['50%', '50%', '50%'],
    'Recomendación Metal': ['50-70%', '80-100%', '70-100%'],
    'Descripción': [
        'Controla la variación creativa. 50% = normal, >70% = experimental, <50% = conservador',
        'Adhesión al estilo definido. Alto = sigue género estrictamente, Bajo = interpretación libre',
        'Solo con Persona. Controla fidelidad a la canción original de referencia'
    ]
}

df_advanced = pd.DataFrame(advanced_options)
print("\nADVANCED OPTIONS - CONFIGURACIÓN RECOMENDADA")
print("="*120)
print(df_advanced.to_string(index=False))
print("\n")

# Guía de conteo de sílabas
syllable_guide = {
    'Sección': ['Verso', 'Pre-Coro', 'Coro', 'Puente', 'Breakdown/Solo'],
    'Sílabas por Línea': ['6-10', '8-12', '6-8', '8-12', '0 (instrumental)'],
    'Patrón de Rima': ['ABAB o AABB', 'ABAB', 'AABB (pegadizo)', 'Flexible', 'N/A'],
    'Características': [
        'Narrativo, establece historia',
        'Construcción de tensión',
        'Memorable, repetitivo, gancho principal',
        'Contraste, momento de reflexión',
        'Momento técnico instrumental'
    ]
}

df_syllables = pd.DataFrame(syllable_guide)
print("\nGUÍA DE ESTRUCTURA LÍRICA - CONTEO DE SÍLABAS Y RIMAS")
print("="*120)
print(df_syllables.to_string(index=False))
