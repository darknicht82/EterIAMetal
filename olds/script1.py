# Crear una base de datos completa con todas las etiquetas de voces para Suno v5 basada en la investigación
vocal_tags_data = {
    "Género Vocal": {
        "Male Vocal/Singer": "Especifica voces masculinas",
        "Female Vocal/Singer": "Especifica voces femeninas", 
        "Duet": "Indica un dúo",
        "Choir/Gospel Choir": "Añade coros",
        "Children Voice": "Voz de niño/niña",
        "Toddler Voice": "Voz de bebé/infante"
    },
    
    "Rangos Vocales": {
        "Tenor": "Rango vocal masculino agudo (no confirmado oficialmente)",
        "Baritone/Bass Male Vocal": "Rango vocal masculino grave",
        "Soprano": "Rango vocal femenino agudo (no confirmado oficialmente)", 
        "Alto": "Rango vocal femenino grave (no confirmado oficialmente)",
        "Contralto": "Rango vocal femenino más grave",
        "Operatic Soprano": "Soprano operística",
        "Operatic Contralto": "Contralto operática"
    },

    "Estilos Vocales Rock/Metal": {
        "Clean Vocals": "Voces limpias melódicas",
        "Growling": "Técnica gutural grave (death metal)",
        "Screaming": "Gritos agudos intensos",
        "Fry Screaming": "Gritos ásperos y distorsionados",
        "Pig Squeals": "Chillidos extremos (brutal death metal)",
        "Harsh Vocals": "Voces duras/ásperas", 
        "Raw Vocals": "Voces crudas",
        "Primal Scream": "Grito primitivo",
        "Infernal Scream": "Grito infernal",
        "Yell Chorus": "Coro gritado",
        "Power Vocals": "Voces poderosas",
        "Aggressive Vocals": "Voces agresivas",
        "Brutal Vocals": "Voces brutales",
        "Death Growls": "Gruñidos de death metal",
        "Black Metal Screams": "Gritos de black metal",
        "Metalcore Vocals": "Voces de metalcore",
        "Melodic Harsh Vocals": "Voces duras melódicas"
    },

    "Técnicas Vocales Específicas": {
        "Belting": "Técnica de canto potente",
        "Whisper": "Susurros",
        "Spoken Word": "Palabra hablada",
        "Rap Verse": "Verso de rap",
        "Gregorian Chant": "Canto gregoriano",
        "Melismatic": "Ornamentación vocal",
        "Sprechgesang": "Medio hablar medio cantar",
        "Vocaloid": "Estilo sintético",
        "Narration": "Narración",
        "Female Narrator": "Narradora femenina",
        "Male Narrator": "Narrador masculino"
    },

    "Efectos y Texturas Vocales": {
        "Reverb": "Reverberación",
        "Echo/Delay": "Eco/Delay",
        "Distorted Vocals": "Voces distorsionadas",
        "Autotuned": "Con autotune",
        "Harmonized Chorus": "Coro armonizado",
        "Stacked Harmonies": "Armonías apiladas",
        "Echoing Vocals": "Voces con eco",
        "Sultry": "Seductor",
        "Resonant": "Resonante",
        "Ethereal": "Etéreo",
        "Lounge Singer": "Cantante de lounge",
        "Emotional": "Emocional",
        "Breathy": "Con aire/respiración",
        "Vibrato": "Con vibrato",
        "Raspy": "Áspero",
        "Gritty": "Arenoso/rugoso"
    },

    "Géneros Específicos Rock/Metal": {
        "Hard Rock Vocals": "Voces de hard rock",
        "Heavy Metal Vocals": "Voces de heavy metal", 
        "Power Metal Vocals": "Voces de power metal",
        "Gothic Metal Vocals": "Voces de gothic metal",
        "Doom Metal Vocals": "Voces de doom metal",
        "Death Metal Vocals": "Voces de death metal",
        "Black Metal Vocals": "Voces de black metal",
        "Thrash Metal Vocals": "Voces de thrash metal",
        "Progressive Metal Vocals": "Voces de metal progresivo",
        "Symphonic Metal Vocals": "Voces de metal sinfónico",
        "Folk Metal Vocals": "Voces de folk metal",
        "Industrial Metal Vocals": "Voces de metal industrial",
        "Nu Metal Vocals": "Voces de nu metal",
        "Alternative Metal Vocals": "Voces de metal alternativo",
        "Melodic Death Metal Vocals": "Voces de death metal melódico",
        "Metalcore Vocals": "Voces de metalcore",
        "Deathcore Vocals": "Voces de deathcore",
        "Post-Metal Vocals": "Voces de post-metal"
    },

    "Etiquetas de Sección para Voces": {
        "[Vocal Solo]": "Solo vocal",
        "[Diva Solo]": "Solo de diva",
        "[Gospel Choir]": "Coro gospel",
        "[Anthem Chorus]": "Coro himno",
        "[Harmonized Verse]": "Verso armonizado",
        "[Scream Section]": "Sección de gritos",
        "[Clean Chorus]": "Coro limpio",
        "[Harsh Verse]": "Verso duro",
        "[Vocal Break]": "Pausa vocal",
        "[A Cappella]": "A cappella"
    }
}

# Crear CSV con todas las etiquetas
import pandas as pd

# Preparar datos para CSV
csv_data = []
for categoria, tags in vocal_tags_data.items():
    for tag, descripcion in tags.items():
        csv_data.append({
            'Categoría': categoria,
            'Etiqueta': tag,
            'Descripción': descripcion,
            'Uso en Prompt': f'Se puede usar en el estilo o como [{tag}]'
        })

df = pd.DataFrame(csv_data)

# Guardar CSV
df.to_csv('suno_v5_vocal_tags_completas.csv', index=False, encoding='utf-8')

print("CSV creado exitosamente con", len(csv_data), "etiquetas vocales")
print("\nPrimeras 10 filas del CSV:")
print(df.head(10))