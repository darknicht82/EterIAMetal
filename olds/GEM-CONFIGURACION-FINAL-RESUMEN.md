# 📦 CONFIGURACIÓN FINAL GEM - INSTRUCCIONES + DOCUMENTOS

## Para implementar LYRICA METAL V5.1 PRO en Google Gemini Gems

───────────────────────────────────────────────────────────────────────────────

## ✅ CAMPO 1: INSTRUCCIONES (Principal)

**Archivo:** [218] GEM-LYRICA-INSTRUCCIONES-V5.1-FINAL-COMPLETA.md

**Qué va aquí:** TODO - Las instrucciones completas con:
- Persona
- Objetivo Principal
- Contexto (subgéneros, parámetros SUNO)
- Formato de Entrega (3 módulos)
- Flujo de Operación (5 fases)
- Palabras Clave (referencia rápida)
- Override Manual
- Checklist Validación
- Reglas Inviolables

**Tamaño:** Cabe completamente en instrucciones (sin límite efectivo)

---

## ✅ CAMPO 2: DESCRIPCIÓN

**Archivo:** [135] LYRICA-V5-DESCRIPCIÓN (que ya tienes)

**Qué va aquí:** Descripción breve (~100 caracteres)

```
Lyrica Metal V5.1 Pro es tu ingeniero de prompts especializado en metal épico para SUNO V5. 
Transforma letras en bloques técnicos optimizados con acento latino neutral.
```

---

## 📚 SECCIÓN 3: CONOCIMIENTO (Referencias Externas)

Aquí va TODO lo que GEM consulta como referencia. Adjunta ESTOS documentos:

### Documento 1: [201] LYRICA-V5.1-CONOCIMIENTO-PURO.md
**Contenido:** Parámetros técnicos SUNO V5
- Exclude Styles efectivos
- Sonic Profile estructura
- Características técnicas SUNO V5
- Recomendaciones por subgénero
- Palabras clave indicadores
- Checklist interno
- Troubleshooting rápido
- Formato bloque SUNO

**Función:** GEM consulta esto cuando necesita valores exactos

---

### Documento 2: [204] ETIQUETAS-VOCALES-ETEARIA-METAL.md
**Contenido:** ~60 etiquetas vocales filtradas (NO 500+)
- Etiquetas por subgénero
- Rango/registro universal
- Efectos/texturas
- Fórmula para bloque LYRICA
- Tabla rápida elecciones críticas
- Reglas etiquetas

**Función:** GEM consulta esto para etiquetar voces correctamente

---

### Documento 3: [206] SUNO-V5-MODULOS-EXACTO.md
**Contenido:** Instrucciones exactas por módulo SUNO
- MÓDULO 1: LYRICS - qué va, dónde, cómo
- MÓDULO 2: STYLES - qué va, dónde, cómo
- MÓDULO 3: ADVANCED - todos los campos
- Mapeo completo dónde va cada elemento
- Flujo exacto en SUNO
- Fórmula simplificada
- Errores comunes que evitar
- Validación final

**Función:** GEM consulta esto cuando estructura bloque para SUNO

---

### Documento 4: [216] SUNO-V5-TEMPO-KEY-BPM-CORRECTO.md
**Contenido:** Cómo usar Tempo, Key, BPM exactos
- Parámetro 1: Tempo/BPM
- Parámetro 2: Key (tonalidad)
- Parámetro 3: Time Signature
- Estructura completa corregida
- Mapeo exacto corregido
- Validación final
- Ejemplo completo funcional

**Función:** GEM consulta esto para saber dónde meter Key/Tempo/BPM

---

### Documento 5: [217] SUNO-V5-MULTIPLES-GENEROS.md
**Contenido:** Cómo usar múltiples géneros
- Opción 1: Género principal + tags secundarios
- Opción 2: Múltiples en descripción
- Estrategia para cada caso
- Combinaciones recomendadas
- Mapeo final corregido
- Validación corregida
- Ejemplo completo final

**Función:** GEM consulta esto cuando maneja múltiples géneros

---

## 📋 RESUMEN: QUÉ ADJUNTAS EN GEM

```
INSTRUCCIONES (Principal):
└─ [218] GEM-LYRICA-INSTRUCCIONES-V5.1-FINAL-COMPLETA.md

DESCRIPCIÓN:
└─ [135] LYRICA-V5-DESCRIPCIÓN (existente)

CONOCIMIENTO (5 documentos):
├─ [201] LYRICA-V5.1-CONOCIMIENTO-PURO.md
├─ [204] ETIQUETAS-VOCALES-ETEARIA-METAL.md
├─ [206] SUNO-V5-MODULOS-EXACTO.md
├─ [216] SUNO-V5-TEMPO-KEY-BPM-CORRECTO.md
└─ [217] SUNO-V5-MULTIPLES-GENEROS.md
```

---

## 🚀 FLUJO DE USO EN GEM

1. **Usuario trae letra metal** → GEM recibe en conversación
2. **GEM lee instrucciones [218]** → Sabe qué hacer
3. **GEM consulta documentos de conocimiento** → [201], [204], [206], [216], [217]
4. **GEM genera análisis** → Detecta subgénero, optimiza
5. **GEM genera bloque en 3 módulos** → Listo para SUNO
6. **Usuario copia a SUNO V5 Pro** → Genera canción perfecta

---

## 📝 CONFIGURACIÓN EN GOOGLE GEMINI:

### Paso 1: Crear nuevo Gem
- Click "Create custom gem"
- Nombre: "LYRICA METAL V5.1 PRO"

### Paso 2: Instrucciones
- Pega TODO [218]

### Paso 3: Descripción
- Pega [135]

### Paso 4: Conocimiento
- Adjunta archivo [201]
- Adjunta archivo [204]
- Adjunta archivo [206]
- Adjunta archivo [216]
- Adjunta archivo [217]

### Paso 5: Configuración Avanzada
- Temperature: 0.8 (creativo pero consistente)
- Max Output: 2000+ caracteres

### Paso 6: Guardar y Publicar

---

## ✅ VALIDACIÓN FINAL

Antes de ir a producción:

- ☑ [218] en Instrucciones
- ☑ [135] en Descripción
- ☑ [201], [204], [206], [216], [217] en Conocimiento
- ☑ GEM puede generar bloque ejemplo
- ☑ Bloque se distribuye en 3 módulos correctamente
- ☑ Etiquetas vocales son correctas
- ☑ Key/Tempo en STYLES
- ☑ Exclude Styles completo en ADVANCED

---

## 📱 LISTA DE CHEQUEO - DOCUMENTOS A USAR

**Para GEM INSTRUCCIONES:**
- [218] ✅

**Para GEM CONOCIMIENTO:**
- [201] ✅
- [204] ✅
- [206] ✅
- [216] ✅
- [217] ✅

**Para GEM DESCRIPCIÓN:**
- [135] ✅

**NO NECESARIOS (son informativos para ti):**
- [196] (versión anterior - reemplazada por [218])
- [200] (extensiones - no va en GEM)
- [205] (corrección - integrada en [218])

---

## 🎤 RESUMEN FINAL

**LYRICA METAL V5.1 PRO está completo con:**

1. ✅ Instrucción principal robusta [218]
2. ✅ 5 documentos de conocimiento específicos [201, 204, 206, 216, 217]
3. ✅ Descripción [135]
4. ✅ Integración total con SUNO V5 Pro
5. ✅ Acento LATINO forzado
6. ✅ Múltiples géneros soportados
7. ✅ Key + Tempo + BPM correctos
8. ✅ Distribución correcta 3 módulos SUNO

**Listo para subir a Google Gemini.** 🎤⚡🤘

═════════════════════════════════════════════════════════════════════════════
