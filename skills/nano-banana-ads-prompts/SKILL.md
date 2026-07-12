---
name: nano-banana-ads-prompts
description: Generador de prompts publicitarios de calidad agencia para Nano Banana Pro (Gemini 3 Pro Image), optimizados para Meta Ads, TikTok Ads y display de e-commerce de moda. Úsala SIEMPRE que el usuario quiera crear, redactar, optimizar o iterar prompts para imágenes publicitarias, creativos estáticos, hero shots, flat lays, UGC simulado, editoriales o cualquier creativo visual destinado a campañas de performance — incluso si no menciona "Nano Banana" explícitamente. Cubre los 10 formatos canónicos de creativos de moda DTC, integra arquitectura de conversión, fidelidad forense al producto, simulación de cámara/lente, dirección de iluminación, tipografía con renderizado literal de texto en español, color grading editorial y psicología de venta. Se integra con skills de avatares y dolores para producir briefs de producción completos.
---

# Generador de Prompts de Anuncios para Nano Banana Pro

## Propósito

Esta skill convierte un input mínimo (producto + avatar + ángulo) en un prompt de producción completo para Nano Banana Pro, listo para copiar y pegar. Cada prompt debe ser indistinguible del brief que un director creativo entregaría a un fotógrafo comercial de €15.000/mes para una marca DTC de moda que factura €2M/año en Meta Ads.

No generes prompts genéricos. No omitas bloques. Cada decisión creativa debe estar justificada por su impacto en conversión.

## Particularidades de Nano Banana Pro (Gemini 3 Pro Image)

Nano Banana Pro tiene fortalezas y limitaciones específicas que cambian cómo se debe escribir el prompt. Adáptate a estas reglas:

### Lo que Nano Banana Pro hace mejor que otros modelos

1. **Renderizado de texto literal**: cualquier texto entre comillas dobles `"..."` se renderiza casi exactamente. Esto es crítico para anuncios con headline + precio + CTA en español. Otros modelos inventan tipografía rota; NBP no.
2. **Hasta 14 imágenes de referencia**: puede combinar producto real + modelo de referencia + fondo + paleta de color simultáneamente, manteniendo coherencia.
3. **Fidelidad a producto**: cuando se le pasa una foto del producto como referencia, replica colores, costuras, texturas y detalles constructivos con precisión superior a otros modelos.
4. **Resoluciones nativas 2K y 4K**: pide explícitamente `2K resolution` o `4K resolution` para creativos de feed; `1K` suele bastar para stories.
5. **Prompts narrativos largos**: rinde mejor con descripciones largas en prosa que con listas de keywords. Escribe como brief, no como tags.
6. **Multilingüe en texto generado**: maneja español, francés e italiano sin problemas.

### Reglas de sintaxis específicas de Nano Banana Pro

- **No uses parámetros tipo `--ar 1:1`, `--v 6`, `::` o weights**. NBP no los entiende; especifica todo en lenguaje natural.
- **Aspect ratio en lenguaje natural**: `square 1:1 format`, `vertical 4:5 format for Meta feed`, `vertical 9:16 format for stories and reels`, `horizontal 16:9 format`.
- **Texto en comillas siempre**: cualquier palabra que deba aparecer en la imagen va entre comillas dobles. Sin comillas, NBP lo interpretará como instrucción y no lo renderizará.
- **Color hex sin almohadilla**: NBP entiende mejor `deep burgundy color, hex 6B1D2A` que `#6B1D2A`.
- **Posición del texto en el frame**: especifica zona (`upper third`, `lower 15%`, `centered`, `top-left corner`) en lugar de coordenadas pixel.
- **Cierra siempre con bloque técnico**: `photorealistic, ultra high resolution, 2K, professional commercial photography, zero AI artifacts, indistinguishable from real photograph`.

### Cuando se trabaja con imagen de referencia del producto

Si el usuario adjunta foto del producto, el prompt debe contener una frase explícita al principio:

> Use the attached product image as the absolute reference. Replicate the garment with forensic precision — exact color, exact construction details, exact proportions. Do not invent details.

## Inputs que necesitas del usuario

Antes de generar un prompt, asegúrate de tener:

1. **Imagen de referencia del producto** idealmente, o descripción muy detallada.
2. **Avatar / cliente ideal**: edad, geografía, contexto socioeconómico, estilo de vida.
3. **Dolor o ángulo específico a atacar**: transparencia, hueco en cintura, comodidad vs elegancia, versatilidad, ad fatigue, etc.
4. **Datos comerciales** opcionales pero ideales: precio antes/ahora, porcentaje de descuento, urgencia, garantías.
5. **Tipo de creativo deseado**. Si no lo dice, elígelo según el dolor usando la tabla de mapeo.
6. **Formato**. Si no lo dice, elige 1:1 para feed cold, 4:5 para feed mid-funnel o 9:16 para stories/reels.

Si falta alguno de los primeros 3, pídelo antes de generar. No inventes el avatar ni el dolor: son la diferencia entre un creativo que convierte y uno que se quema en una semana.

Si ya hay un avatar generado por `avatar-dolores-moda.md` en la conversación, reutilízalo directamente sin volver a preguntar.

## Proceso de generación

### Paso 1 — Analiza el producto

- Extrae todos los detalles constructivos visibles en la referencia: color exacto con subtono y temperatura, corte, silueta, botones, cremalleras, costuras, pinzas, bolsillos, acabados, tipo de tejido, peso, caída y opacidad.
- Identifica los **selling details visuales**: los 2-3 detalles que demuestran calidad o el beneficio principal y que pueden fotografiarse para venderlos.
- Define el color con precisión obsesiva. `Crema` no sirve; `Cream with warm yellow undertone, the shade of fresh heavy cream, not white, not beige, not yellowed` sí.

### Paso 2 — Mapea dolor a formato

| Dolor del avatar | Formato recomendado |
| --- | --- |
| Comodidad vs elegancia | Tipo A (Social Proof Hero) o Tipo I (UGC Simulation) |
| Fit / silueta / cintura | Tipo C (Transformation) o Tipo E (Confidence Close-Up) |
| Versatilidad / "no sé con qué combinarlo" | Tipo D (Flat Lay Premium) o Tipo F (Triple Life) |
| Objeción concreta: transparenta, se encoge, calidad | Tipo H (Objection Killer) |
| Necesita prueba social masiva | Tipo G (Testimonial Wall) |
| Necesitas anclar precio alto y revelar descuento | Tipo B (Price Architecture) |
| Top of funnel / branding + conversión | Tipo J (Editorial Aspiracional) |

### Paso 3 — Construye el prompt con los 10 bloques obligatorios

Usa siempre los bloques definidos en la sección siguiente, en el mismo orden y sin excepciones.

### Paso 4 — Revisa contra el checklist

Antes de entregar, verifica el checklist final.

## Los 10 bloques obligatorios del prompt

Cada prompt que generes debe tener estos bloques en este orden. Sin excepciones. Mínimo 400 palabras de longitud final.

### Bloque 1 — Cabecera técnica

Define formato, dimensiones y propósito en una frase de apertura.

Ejemplo: `Premium product advertising photograph engineered for maximum conversion on Meta Ads feed, vertical 4:5 format, 2K resolution output, optimized for thumb-stop scrolling.`

### Bloque 2 — Simulación de cámara y lente

Especifica equipo simulado. Incluye apertura, plano de enfoque y ángulo de cámara.

| Situación | Cámara + lente | Justificación |
| --- | --- | --- |
| Retrato / UGC cercano | Sony A7IV + 85mm f/1.8 | Bokeh cremoso, proporciones naturales, sensación íntima |
| Editorial full-body | Hasselblad X2D + 80mm f/1.9 | Medium format, profundidad 3D, texturas extraordinarias |
| Flat lay producto | Phase One IQ4 + 120mm macro | Resolución extrema, nitidez borde a borde, detalle de fibra |
| Escena ambiental | Canon R5 + 35mm f/1.4 | Gran angular suave, contexto, sensación de presencia |
| Silueta / cuerpo / body confidence | Nikon Z9 + 50mm f/1.2 | Zero distorsión, proporciones honestas |
| Composite multi-panel | Fujifilm GFX100S + 80mm f/1.7 | Medium format consistente entre paneles |
| Close-up textura | Canon R5 II + 100mm f/2.8L macro | Detalle a nivel de fibra |

### Bloque 3 — Fidelidad al producto

Este es el bloque más importante. Hazlo extenso y forense. Si hay imagen adjunta, ábrelo con: `Use the attached product image as the absolute reference. Replicate with forensic precision.` Luego enumera detalles aunque la imagen los muestre:

- Color exacto + subtono + qué no es.
- Corte y silueta con proporciones relativas.
- Cada elemento constructivo: botones, cremalleras, costuras, pinzas, trabillas, bolsillos; tipo, posición y tamaño.
- Tejido: peso, caída, brillo, opacidad y textura.
- Acabados internos visibles si aplica.

### Bloque 4 — Escena y composición

Describe el entorno y diseña el **eye path** explícitamente:

> The viewer's eye must follow: (1) headline → scroll-stop, (2) product → desire, (3) detail → proof, (4) price/CTA → action.

Posiciona elementos usando regla de tercios o golden ratio en lenguaje natural.

### Bloque 5 — Modelo y dirección de pose

Si hay modelo:

- Describe físico realista alineado al avatar; no uses ultradelgada por defecto. Ejemplo: `real woman's body, healthy, natural curves at hips, soft midsection, 30-40 years old appearance`.
- Etnia/rasgos coherentes con el mercado. Para España: Mediterranean features, warm skin tone, natural makeup.
- Pose específica con gestos y dirección de mirada.
- Si no muestras la cara, indícalo explícitamente: `face cropped at chin level`, `back to camera` o `shot from below the shoulders`.

### Bloque 6 — Estilismo completo

Describe cómo va vestida y qué accesorios lleva. Vende el **outfit completo**, no solo el producto. Incluye calzado, joyería y bolso si suma.

### Bloque 7 — Arquitectura de iluminación

Nunca digas solo `buena luz`. Define:

- **Key light**: tipo de fuente, posición, ángulo, altura, temperatura de color en Kelvin.
- **Fill**: bounce o flash secundario, stops por debajo del key.
- **Rim / accent**: luz de separación detrás del sujeto.
- **Practical** si hay: lámparas, ventanas, velas visibles en escena.
- **Calidad de sombra**: suave/dura, dirección, falloff.

### Bloque 8 — Arquitectura de texto

Este bloque aprovecha la fortaleza de NBP. Para cada zona de texto especifica:

- Contenido exacto entre comillas dobles.
- Posición: `upper 18%`, `lower 12%`, `centered`, etc.
- Tipografía: `Helvetica Neue Bold aesthetic`, `Playfair Display aesthetic`, `Didot aesthetic`.
- Color en hex, por ejemplo `color hex 1A1A1A`.
- Tamaño relativo: `largest element`, `50% of headline`, etc.
- Tracking / letter-spacing si aplica.
- Caso: uppercase, sentence case, title case.

Estructura mínima de un creativo de performance:

1. **Headline** en zona superior: gancho, pattern interrupt o pregunta-dolor.
2. **Subheadline** debajo: refuerzo o testimonio.
3. **Conversion strip** en el 10-15% inferior: precio antes/ahora, descuento, urgencia, garantías.

### Bloque 9 — Color grading y mood

Define sombras, midtones y highlights por separado:

- Sombras: temperatura, por ejemplo warm amber bias o cool blue bias.
- Midtones: naturalidad y sesgo.
- Highlights: rolloff, por ejemplo creamy soft o clipped harsh.
- Contraste: medio, alto o cinemático.
- Saturación: producto vs entorno. Truco: ambiente desaturado + producto a saturación natural = el producto destaca.
- Temperatura general en Kelvin.
- Mood en una frase, por ejemplo `aspirational but attainable`, `cold Vogue editorial`, `warm Reformation lookbook`, `Massimo Dutti campaign`.

### Bloque 10 — Psicología de conversión + cierre técnico

Explica la arquitectura psicológica: qué dolor ataca, qué sesgo activa, secuencia de respuesta esperada y posición en funnel. Cierra con:

> Photorealistic. Ultra high resolution. 2K output. Professional commercial photography quality. Zero AI artifacts. No uncanny valley on faces, hands, or fabric. Indistinguishable from a real photograph shot by a top commercial photographer for a premium Spanish fashion brand.

## Los 10 tipos de creativos

### Tipo A — Social Proof Hero (1:1)

Producto centrado como héroe, estrellas + review, testimonial con nombre/ciudad/edad, banner de urgencia abajo. Para prospección fría.

### Tipo B — Price Architecture (1:1)

Producto en contexto lifestyle aspiracional, headline que ancla precio alto, reveal de descuento dramático, badge de porcentaje. Para mid-funnel y consideración.

### Tipo C — Transformation (4:5)

Antes/después en un frame continuo. Contraste emocional > visual. El producto resuelve el antes. Para pain points de inseguridad corporal.

### Tipo D — Flat Lay Premium (1:1)

Cenital, superficie de lujo, props con intención. Cada prop refuerza un ángulo de venta. Para versatilidad y calidad percibida.

### Tipo E — Confidence Close-Up (4:5)

Crop ajustado a la zona problema: cintura, abdomen o escote. Demuestra fit. Callouts técnicos estilo Apple. Para pain points de fit.

### Tipo F — Triple Life / Multi-Outfit (1:1)

3 paneles, mismo producto, 3 contextos: lunes oficina, sábado brunch, domingo cita. Headline de contraste. Para versatilidad.

### Tipo G — Testimonial Wall (4:5)

Producto centrado rodeado de reviews. Cada review ataca un dolor diferente. Número de compradores como headline. Para retargeting y cierre.

### Tipo H — Objection Killer (1:1)

Confronta directamente el miedo. Prueba visual del claim, por ejemplo `Mira a contraluz: NO transparenta`. Tono casi desafiante. Para retargeting de audiencias tibias.

### Tipo I — UGC Simulation (4:5 o 9:16)

Parece contenido orgánico. Estética smartphone, luz natural, entorno real, espejo/baño/coche. Texto estilo stories. Para bypass de ad fatigue.

### Tipo J — Editorial Aspiracional (4:5)

Fotografía de moda editorial pura. Mínimo texto, máximo impacto visual. El producto en un entorno soñado. Para branding + top of funnel.

## Reglas específicas para texto en Nano Banana Pro

1. **Siempre entre comillas dobles**: `"LA CHAQUETA DE 200€ QUE NO CUESTA 200€"`. Sin comillas, lo trata como instrucción.
2. **El símbolo del euro funciona**: `€89,95` se renderiza correctamente. Usa coma decimal en formato europeo.
3. **Caracteres especiales españoles**: ñ, tildes, ¿¡ se renderizan bien. No los evites.
4. **Limita texto por imagen**: máximo 3 bloques de texto: headline + subhead + conversion strip.
5. **Headlines cortos**: máximo 8-10 palabras. NBP los renderiza más limpios.
6. **Especifica jerarquía**: `primary, largest text element`, `secondary, 50% size of primary`, `tertiary, smallest`.
7. **Define el contraste fondo-texto**: si el headline va sobre fondo claro, especifica color oscuro y viceversa.
8. **Evita scripts manuscritos complejos**: NBP los suele romper. Sans-serif y serif clásicos son seguros.

## Checklist final

Revisa cada prompt antes de entregar:

- [ ] ¿El producto está descrito con precisión forense?
- [ ] ¿La cámara/lente está especificada con justificación?
- [ ] ¿La iluminación tiene key, fill y accent definidos con Kelvin y stops?
- [ ] ¿El eye path está diseñado explícitamente?
- [ ] ¿Cada texto está entre comillas dobles, con contenido exacto, posición, color hex y tipografía?
- [ ] ¿El headline ataca directamente un dolor del avatar?
- [ ] ¿Hay urgencia/escasez/garantías?
- [ ] ¿Hay precio con anchor + descuento si aplica?
- [ ] ¿El color grading define sombras, medios, luces por separado?
- [ ] ¿El bloque psicológico explica la secuencia de conversión y posición en funnel?
- [ ] ¿El prompt cierra con especificaciones técnicas de calidad?
- [ ] ¿El prompt tiene mínimo 400 palabras?
- [ ] ¿Si hay imagen de referencia adjunta, hay frase explícita de `use as absolute reference`?

## Notas finales

- Si el usuario pide varios prompts, varía el tipo de creativo, el ángulo de dolor o el headline; no cambies solo cosméticos.
- Si el usuario pide adaptar un prompt a otro formato, reescribe la composición y reposiciona el texto; no cambies solo la línea de aspect ratio.
- Si no hay datos comerciales, omite el conversion strip y usa el espacio inferior para un CTA simple como `"DESCUBRIR"` o testimonial corto.
- Recuerda: estás compitiendo en el feed contra contenido orgánico de amigos y familia. El primer segundo decide todo. Si el creativo no para el scroll en la primera mirada, el resto no importa.
