# 📋 LYRICA V6.1 - IMPLEMENTATION GUIDE (STEP-BY-STEP, SUNO V5.5)

## How to Integrate V6.1 into Your System (Sliders, GEM, Voices & Loops)

---

## 📍 STEP 1: Update `LYRICA-V6-VOCAL-TAGS.md` (30 minutes)

### What to do:

1. Open your current `LYRICA-V6-VOCAL-TAGS.md`.
2. Find section: `SUNO V5 PARÁMETROS VALIDADOS` (or similar).
3. Replace ALL slider values with this table:

```markdown
### SUNO V5.5 – PARÁMETROS POR SUBGÉNERO (LYRICA V6.1)

| Subgénero          | Weirdness | Style Influence | Audio Influence (si ref.) |
|--------------------|-----------|-----------------|---------------------------|
| POWER METAL        | 12 %      | 75 %            | 35 %                      |
| DOOM METAL         | 45 %      | 72 %            | 50 %                      |
| SYMPHONIC METAL    | 28 %      | 75 %            | 40 %                      |
| GOTHIC METAL       | 33 %      | 76 %            | 45 %                      |
| METALCORE          | 52 %      | 70 %            | 55 %                      |
| FOLK METAL         | 35 %      | 76 %            | 35 %                      |
| NEOCLASSICAL METAL | 18 %      | 78 %            | 60 %                      |
```

4. Add/update section: `REGLAS GLOBALES SLIDERS – V6.1`:

```markdown
### REGLAS GLOBALES SLIDERS – V6.1 (Suno V5.5)

**Style Influence (SI):**
- NUNCA usar > 80 % (plateau + reduced vocal phrasing).
- Rango LYRICA: 70–78 % según subgénero.
- Uso: mantiene claridad de género sin sacrificar fraseo vocal.

**Weirdness (W):**
- Generación normal: usar valor de tabla por subgénero.
- EXTEND: usar W_base − 12 (CRITICAL: previene style drift).
- REPLACE SECTION: usar W_base − 8 (cohesión local).
- Con referencia vocal / Voice / Custom Model: usar W_base − 2.
- Con referencia instrumental: usar W_base + 3.

**Audio Influence (AI):**
- Solo cuando hay upload de audio o se usa Voice/Custom Model.
- Vocal / Voice: 45–60 % (anclaje fuerte).
- Instrumental: 35–50 % (guía sin encadenar).
- Texture/ambience: 20–30 % (influencia sutil).
```

5. Replace EXCLUDE STYLES section con la lista V6.1 completa:

```markdown
### EXCLUDE STYLES – V6.1 (37 items)

harsh digital artifacts, clipping, bright highs, digital clicking,
square wave artifacts, harsh treble, rough transients, metallic tone,
thin production, amateur quality, synthetic tone, robotic vocals,
digital harshness, white noise, shimmer, residual noise, latent artifacts,
muddy mix, poor separation, compressed sound, flat dynamics,
poor voice leading, muddled harmonies, unclear chord progression,
forced vibrato, unnatural breathiness, inconsistent tone, vocal strain
artifacts, autotune artifacts, amateur mastering, insufficient stereo
separation, phase issues in mix, Spanish Spain accent, Castilian
pronunciation, theta sound, Spanish lisp pronunciation, European Spanish,
Spain dialect, European accent
```

6. Save file.

---

## 📍 STEP 2: Copy V6.1 GEM Instructions (15 minutes)

### What to do:

1. Copy entire content of **`LYRICA-V6.1-INSTRUCCIONES-GEM.md` (SUNO V5.5)**.
2. Go to your **Google Gemini / Gem Custom Instructions** settings.
3. Replace or UPDATE your current LYRICA METAL prompt with the **new V6.1 PRO (V5.5)** version.
4. Key sections to verify are present:

   - ✅ Sección **“🎛️ SLIDERS SUNO V5.5 – POLÍTICA LYRICA V6.1”**.  
   - ✅ Sección **“FASE 7B: PERSONAS / VOICES – CONSISTENCIA DE VOZ”**.  
   - ✅ Bloque **“MODO LOOP / SOUNDS”** para cuando pidas loops.  
   - ✅ Valores de sliders V6.1 en FASE 6 (Weirdness, Style Influence, Audio Influence).  

5. Save in GEM.

---

## 📍 STEP 3: Test Generation (2–3 hours)

Objetivo: comprobar que V6.1 + V5.5 funcionan como esperas en 5 escenarios clave:
- Power “heroico”.
- Neoclassical “no robótico”.
- Metalcore con EXTEND sin drift.
- Voces propias (Voice / Custom Model).
- Modo Loop/Sounds.

---

### Test #1: POWER METAL (Sliders base)

**Input:**
- Letra de power metal (puede ser una que ya usaste en V6).
- Subgénero detectado: POWER.

**Expected Sliders in output:**
```text
Weirdness:       12 %
Style Influence: 75 %
Audio Influence: 35 % (si usas referencia); N/A si no.
```

**Evaluation:**
- ✓ ¿Las voces suenan más heroicas y menos planas que en V6?
- ✓ ¿Hay más variación de fraseo (no todo pegado en el grid)?
- ✓ ¿La mezcla se siente limpia, sin artefactos raros?

**Document:**
- Screenshot de sliders de Suno V5.5.
- Rating de calidad (1–10).
- Notas: diferencias clave vs V6.

---

### Test #2: NEOCLASSICAL (CRITICAL FIX – Anti-robótico)

**Input:**
- Letra de neoclassical metal (idealmente una usada en V6).
- Subgénero: NEOCLASSICAL.

**Critical Change to Verify:**
```text
OLD (V6):   W 20 % | SI 90 %  → ROBOTIC
NEW (V6.1): W 18 % | SI 78 %  → ELEGANT
```

**Evaluation:**
- ✓ ¿Dejó de sonar robótico (menos “ceiling” en fraseo)?
- ✓ ¿El vibrato suena natural, no hiper-cuantizado?
- ✓ ¿Se mantiene la precisión técnica y claridad clásica?

**Document:**
- Comparar audio V6 vs V6.1.
- Elegance rating (1–10).
- Comentario: “qué cambió exactamente” (timbre, fraseo, sensación).

---

### Test #3: METALCORE con EXTEND (Drift Fix)

**Input:**
- Letra de metalcore.
- Genera un bridge y luego usa **EXTEND** para alargarlo (ej. “extend the bridge by 8 seconds”).

**Critical Change to Verify:**
```text
OLD (V6):   W 60 %  → EXTEND → STYLE DRIFT
NEW (V6.1): W 52 %  → EXTEND (W_base − 12 = 40 %) → COHESIVE
```

**Evaluation:**
- ✓ ¿La sección extendida suena como parte de la misma canción?
- ✓ ¿No cambia de género/feel de forma brusca?
- ✓ ¿La voz se mantiene consistente (mismo carácter)?

**Document:**
- Comparar original vs extendido.
- Cohesion rating (1–10).
- Nota: “¿todavía notas algún micro-drift?”.

---

### Test #4: VOICES / CUSTOM MODEL (Tu voz o voz fija)

**Input:**
- Letra para el subgénero donde quieras fijar una identidad vocal (ej. Symphonic, Doom o “Rey Vampiro”).
- Usa **Voice propia** o un **Custom Model** en Suno V5.5.

**Setup esperado:**
```text
Subgénero (ej.):    SYMPHONIC
Weirdness (tabla):  28 %
Style Influence:    75 %
Audio Influence:    50 % (Voice / Vocal upload)
```

**Evaluation:**
- ✓ ¿El timbre respeta la Voice/Custom Model?
- ✓ ¿La variación melódica sigue sonando natural (no copia 1:1 tu demo)?
- ✓ ¿Hay coherencia al generar una segunda canción con la misma Voice?

**Document:**
- Voice/Custom Model usado.
- Sliders reales que Suno aplicó.
- Consistency rating (1–10) entre temas.

---

### Test #5: LOOP / SOUNDS MODE (Short form)

**Input:**
- Prompt claro para un loop (ej. “16‑bar breakdown loop in metalcore” o “8‑bar cinematic symphonic intro loop”).
- Misma lógica de subgénero.

**Setup esperado (ej. Metalcore):**
```text
Weirdness:       52 % (o 50 % si quieres algo más controlado)
Style Influence: 70 %
Audio Influence: OFF (a menos que haya loop de referencia)
Timing:          8–16 compases, tileable
```

**Evaluation:**
- ✓ ¿El loop se puede ciclar sin cortes bruscos?
- ✓ ¿Mantiene el carácter del subgénero?
- ✓ ¿Los sliders responden igual de bien que en canción completa?

**Document:**
- Tipo de loop (subgénero + compases).
- Uso posterior (reel, intro, etc.).
- Loop quality (1–10) y si hay pops/glitches al ciclar.

---

## 📍 STEP 4: Document Results (30–45 minutes)

Crea o actualiza archivo: `V6.1-TEST-RESULTS.md`.

```markdown
# V6.1 Implementation Test Results (Suno V5.5)

## Test 1: Power Metal (Base sliders)
- Date:
- Input (song / prompt):
- Sliders: W/SI/AI usados:
- Audio Quality (1–10):
- Phrasing Variation (1–10):
- Notes:
- vs V6 Improvement (% or comments):

## Test 2: Neoclassical (Anti-robótico)
- Date:
- Input:
- Sliders:
- Vocal Elegance (1–10):
- Before (V6) Robotic? Yes/No
- After (V6.1) Robotic? Yes/No
- SI Change Impact (texto corto):

## Test 3: Metalcore EXTEND
- Date:
- Input:
- Sliders:
- Original→Extended Cohesion (1–10):
- Drift detected? Yes/No
- W reduction (60→52→40) Impact:

## Test 4: Voice / Custom Model
- Date:
- Voice/Model used:
- Subgenre:
- Sliders:
- Identity Consistency across songs (1–10):
- Notes (qué hace bien / qué hay que ajustar):

## Test 5: Loop / Sounds
- Date:
- Loop type (subgenre + bars):
- Sliders:
- Seamless Loop Quality (1–10):
- Use case (intro, reel, breakdown, etc.):
- Notes:

## SUMMARY
- Implementation time total:
- Success rate perceived:
- Most improved subgenre:
- Next steps (ajustes finos, nuevos tests):
```

---

## 📍 STEP 5: Train on New Workflow (2–3 hours)

### Create practice songs & loops:

**Song 1 – Power Metal (canción completa):**
- Objetivo: confirmar sliders V6.1 + Exclude Styles + análisis completo.
- Tareas:
  - Revisión de voz, mezcla, sensación general.
  - Ajustar pequeños matices de tags si hace falta.

**Song 2 – Gothic Metal (con referencia vocal / Voice):**
- Objetivo: probar Audio Influence + Voice/Persona.
- Tareas:
  - Generar con y sin ref. vocal.
  - Evaluar cuánto respeta el carácter y cuánto añade creatividad.

**Song 3 – Neoclassical (EXTEND + solo):**
- Objetivo: test crítico SI 78 % y EXTEND en secciones técnicas.
- Tareas:
  - Ver si el solo extendido mantiene la misma lógica melódica.

**Song 4 – Metalcore LOOP (8–16 compases):**
- Objetivo: validar MODO LOOP/Sounds.
- Tareas:
  - Reproducir en loop y comprobar que no hay salto audible.
  - Exportar y usar en un DAW para prueba externa.

### Document each practice:

- Sliders usados (W/SI/AI).
- Modo (song vs loop).
- Tiempo invertido.
- Rating (1–10).
- Problemas encontrados y soluciones.

---

## 📍 STEP 6: Build Personas / Voices Library (2–3 hours)

### For each subgénero, generate 1–2 base tracks y guarda:

```text
POWER_ETERIA_HEROIC_TENOR
├─ Generated with W 12 %, SI 75 %
├─ Saved as Persona / Voice in Suno
└─ Ready for reuse (songs + loops)

DOOM_ETERIA_BARITONE_DARK
├─ Generated with W 45 %, SI 72 %
├─ Persona / Voice
└─ Ready for reuse

SYMPHONIC_ETERIA_SOPRANO_EPIC
├─ Generated with W 28 %, SI 75 %
├─ Persona / Voice
└─ Ready for reuse

... etc. para todos los subgéneros clave (incluyendo proyectos especiales como "Rey Vampiro").
```

**Benefit:**
- Una vez que tienes 1–2 Voices sólidas por subgénero, todo el futuro catálogo
  (álbumes, concept stories, loops, colaboraciones) hereda la misma identidad vocal.

---

## 📍 STEP 7: Update Knowledge Base Docs (Optional but recommended)

Si usas una Knowledge Base tipo Notion/MD para LYRICA:

### `LYRICA-V6-SUBGENEROS.md`
- Actualiza sliders (W/SI/AI) a V6.1.
- Añade nota: “Optimizado para Suno V5.5 (2026)”.

### `LYRICA-V6-MELODY-HARMONIC.md`
- Asegúrate de que los ejemplos de Melody Guide son **descriptivos** (no notas literales).
- Nota breve: “Suno V5.x tiende a interpretar literalmente notas exactas; mejor trabajar con descripciones de registro y tensión”.

### `LYRICA-V6-VOCAL-TAGS.md`
- Confirma que:
  - Sliders = tabla V6.1.
  - EXCLUDE STYLES = 37 ítems.
  - Personas / Voices protocol incluido.
  - Timing windows están como rangos.

---

## 📍 TIMELINE SUMMARY

```text
Phase                                  Time
--------------------------------------------
Step 1 – Update VOCAL-TAGS.md         ~30 min
Step 2 – Update GEM instructions      ~15 min
Step 3 – 5 core tests (songs+loops)   ~2–3 h
Step 4 – Document results             ~30–45 min
Step 5 – Train on workflow            ~2 h
Step 6 – Build Personas/Voices lib    ~2 h
Step 7 – Update KB docs (optional)    ~30 min
--------------------------------------------
TOTAL (full implementation)           ~7–8 h
```

---

## 🎯 EXPECTED OUTCOMES (V6 → V6.1 + V5.5)

- +20–30 % en variación de fraseo vocal (menos robótico).  
- +15–20 % en éxito de EXTEND (menos style drift).  
- +10–20 % en elegancia de Neoclassical y coherencia en Metalcore.  
- Identidad vocal consistente gracias a Personas/Voices.  
- Loops y Sounds listos para uso profesional sin romper el framework LYRICA.

---

**LYRICA V6.1 – IMPLEMENTATION GUIDE (SUNO V5.5)**  
**Status: READY FOR EXECUTION** ✅
