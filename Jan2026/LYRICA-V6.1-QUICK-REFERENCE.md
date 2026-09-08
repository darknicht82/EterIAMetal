# ⚡ LYRICA V6.1 - QUICK REFERENCE CARD (SUNO V5.5)

## One-Page Implementation Guide for Sliders, Personas/Voices & Timing

Uso: esta tarjeta es tu vista rápida para:
- Consultar **sliders V6.1** por subgénero.
- Recordar **reglas globales W/SI/AI**.
- Aplicar **EXTEND / REPLACE** sin drift.
- Usar **Personas / Voices** y presets básicos de loops.
- Ver **timing windows** sin abrir los documentos largos.

---

## 🎚️ SLIDER TABLE – SUBGÉNEROS (V6.1)

**SUNO V5.5 – Parámetros base por subgénero** (para canción completa).

```text
SUBGÉNERO        Weirdness   Style Infl.   Audio Infl.
------------------------------------------------------
POWER METAL      12 %        75 %          35 % (si ref.)
DOOM METAL       45 %        72 %          50 %
SYMPHONIC METAL  28 %        75 %          40 %
GOTHIC METAL     33 %        76 %          45 %
METALCORE        52 %        70 %          55 %   ← CRITICAL FIX
FOLK METAL       35 %        76 %          35 %
NEOCLASSICAL     18 %        78 %          60 %   ← CRITICAL FIX
```

**CRITICAL FIXES:**
- **Metalcore:** W 60 → **52 %** para evitar drift en EXTEND.  
- **Neoclassical:** SI 90 → **78 %** para eliminar voz robótica.  
- **TODOS:** SI entre **70–78 %**, nunca > 80 %.

---

## 🎛️ SLIDERS – REGLAS POR ESCENARIO

```text
Escenario             Weirdness         Style Infl.     Audio Infl.
--------------------------------------------------------------------
Normal (solo texto)   Base (tabla)      Base (tabla)    OFF
Con ref. vocal/Voice  Base − 2          Base (tabla)    45–60 %
Con ref. instrumental Base + 3          Base (tabla)    35–50 %
EXTEND                Base − 12         Base (tabla)    OFF
REPLACE SECTION       Base − 8          Base + 2        OFF
```

**Notas rápidas:**
- **SI > 80 % = antipatrón** → voz plana/robótica (mantén 70–78 %).  
- **Weirdness alto en EXTEND = drift** → siempre aplica “Base − 12”.  
- **Audio Influence** solo cuando haya **upload de audio** o estés usando **Voice/Custom Model**.

---

## 🧬 PERSONAS / VOICES – LOCK RÁPIDO

**Objetivo:** misma voz a través de secciones y canciones (álbum conceptual, proyectos tipo “Rey Vampiro”).

```text
1) Genera canción con sliders V6.1.
2) Si la voz es perfecta → guarda como Persona / Voice.
   Naming: [SUBGÉNERO]_[PROYECTO]_[CARÁCTER]
   Ej: POWER_ETERIA_HEROIC_TENOR

3) Para nuevas secciones/canciones:
   - Selecciona esa Persona / Voice en Suno.
   - Weirdness = W_base − 2
   - Style Influence = valor de tabla
   - Audio Influence = OFF (salvo caso puntual)

Resultado: misma identidad vocal en todo el universo del proyecto.
```

---

## 🔁 MODO LOOP / SOUNDS – PRESETS RÁPIDOS

Cuando el objetivo no es una canción completa, sino:
- **Loop**, **breakdown**, **intro corta**, **impacto**, **sound design**, etc.

Aplica:

```text
POWER:       8–16 compases, riff anthemic, tileable, sin final duro.
DOOM:        4–8 compases, riff lento + órgano, muy denso.
SYMPHONIC:   4–8 compases, strings + choir cinematic swell.
GOTHIC:      4–8 compases, pad + órgano, atmósfera oscura.
METALCORE:   8–16 compases, breakdown chugga + double bass.
FOLK:        8–16 compases, groove tribal + acordeón/pipes.
NEOCLASSICAL:8–16 compases, arpegios shred + pedal tone.
```

**Reglas:**
- Usa **los mismos sliders de tabla** por subgénero.  
- En STYLES, indica: “**seamless loop, tileable, no hard ending**”.  
- Timing en compases, NO en segundos exactos.

---

## ⏱️ TIMING WINDOWS – CANCIONES (RESUMEN)

*(Detalles completos siguen en `LYRICA-V6.1-VOCAL-TAGS.md`; aquí van solo los patrones.)*

```text
POWER (4:30 target)
- Intro:        25–30 s
- Verse 1:      38–42 s
- Pre-Chorus:   16–20 s
- Chorus:       33–37 s
- Verse 2:      38–42 s
- Bridge:       26–30 s
- Solo:         28–32 s
- Final Chorus: 38–42 s
- Outro:        12–14 s
Tol: ±8 s sobre 270 s

METALCORE (4:30 target)
- Intro:        20–25 s
- Verse 1:      35–40 s
- Pre-Chorus:   18–22 s
- Chorus:       32–37 s
- Verse 2:      35–40 s
- Bridge:       28–35 s
- Break:        25–30 s
- Final Chorus: 35–40 s
- Outro:        10–15 s
Tol: ±8–10 s

NEOCLASSICAL (5:00 target)
- Intro:        28–35 s
- Verse 1:      42–48 s
- Pre-Chorus:   20–25 s
- Chorus:       38–43 s
- Verse 2:      42–48 s
- Bridge:       32–40 s
- Solo (tech):  40–50 s
- Final Chorus: 42–48 s
- Outro:        16–20 s
Tol: ±12 s
```

*(Puedes seguir usando las ventanas completas originales para Doom, Symphonic, Gothic y Folk, solo recuerda que son **rangos**, no valores rígidos.)*  

---

## ✅ PRE-GENERATION CHECKLIST (FLASH)

```text
[ ] Subgénero detectado + título épico generados.
[ ] Sliders = tabla por subgénero (W, SI, AI).
[ ] SI en rango 70–78 % (nunca > 80 %).
[ ] EXTEND/REPLACE usan reglas Base−12 / Base−8.
[ ] Audio Influence: OFF / vocal 45–60 % / inst. 35–50 %.
[ ] Exclude Styles = 37 items completos pegados.
[ ] Vocal Tags correctos (registro, carácter, técnica).
[ ] Timing = rangos (no segundos fijos).
[ ] STYLES incluye DAC/audio de estudio + acento LATINO.
[ ] Lyrics Mode = Manual (ON).
[ ] Persona / Voice seleccionada si aplica.
```

---

## 🧠 KEY RULES (MEMORIA MUSCULAR)

```text
1) SI nunca > 80 %  → plateau + voz robótica.
2) W en EXTEND = Base − 12 → sin drift.
3) W en REPLACE = Base − 8, SI + 2 → cohesión.
4) AI 45–60 % para voces; 35–50 % para instrumentos.
5) Personas/Voices se usan SIEMPRE con W_base − 2.
```

---

**LYRICA V6.1 – QUICK REFERENCE (SUNO V5.5)**  
**Status: READY FOR IMMEDIATE USE** ⚡
