# DIAGRAMA

> Atlas de representación visual, semántica y contextual para sistemas de observación.

Este repositorio reúne maneras de **representar valor, cambio, estructura, relaciones, contexto, incertidumbre y significado oculto**. No está limitado a gráficas de líneas: incluye representaciones lineales, circulares, radiales, hexagonales, vectoriales, topológicas, tridimensionales, jerárquicas y simbólicas.

La idea central es simple:

> **Elegir la geometría según la pregunta que queremos responder.**

---

## 1. Qué es cada cosa

| Familia | Pregunta principal | Ejemplos |
|---|---|---|
| **Gráfica** | ¿Cuánto? ¿Cómo cambia? | línea, barras, área, velas |
| **Diagrama** | ¿Cómo se relaciona o funciona? | flujo, bloques, Sankey, red |
| **Esquema** | ¿Cómo está organizado? | arquitectura, capas, blueprint |
| **Mapa** | ¿Dónde está o cómo se distribuye? | heatmap, geográfico, topológico |
| **Infografía** | ¿Cómo cuento una historia visual? | composición de texto + gráficas + símbolos |
| **Notación visual** | ¿Qué significa este estado? | iconos, colores, glifos, badges |

---

# 2. Taxonomía maestra

## A — Tendencia y tiempo

- **Línea** — evolución temporal, picos, tendencia.
- **Área** — volumen acumulado o intensidad.
- **Velas / candlestick** — apertura, cierre, máximos, mínimos, volatilidad.
- **Sparkline** — microtendencia compacta.
- **Timeline** — secuencia de eventos e hitos.
- **Slope chart** — comparación de cambio entre dos momentos.

## B — Comparación

- **Barras** — comparación directa entre categorías.
- **Barras apiladas** — total + composición interna.
- **Lollipop** — comparación ligera y elegante.
- **Dot plot** — diferencias precisas con poco ruido visual.
- **Bullet chart** — valor actual contra objetivo o benchmark.

## C — Proporción y composición

- **Pie / pastel** — partes de un todo, pocas categorías.
- **Donut** — proporción con espacio central para score/estado.
- **Treemap** — magnitud jerárquica por áreas.
- **Waffle** — porcentajes discretizados.
- **Mosaic** — composición cruzada entre categorías.

## D — Circular, radial y orbital

- **Radar / spider** — perfil multidimensional.
- **Radial bar** — magnitudes alrededor de un centro.
- **Sunburst** — jerarquía concéntrica.
- **Anillos concéntricos** — capas de significado o profundidad.
- **Chord diagram** — relaciones entre categorías alrededor de un círculo.
- **Órbitas** — centralidad, dependencia, ecosistemas.
- **Polar chart** — variables definidas por ángulo y magnitud.

## E — Vectorial y direccional

- **Vector** — dirección + magnitud.
- **Campo vectorial** — comportamiento distribuido.
- **Quiver plot** — conjunto de flechas sobre un plano.
- **Streamlines** — trayectorias de flujo continuo.
- **Phase portrait** — estado dinámico y evolución de un sistema.

## F — Redes y relaciones

- **Network graph** — nodos y conexiones.
- **Force-directed graph** — comunidades emergentes por proximidad.
- **Mapa conceptual** — relaciones semánticas.
- **Mapa mental** — expansión radial de ideas.
- **Adjacency matrix** — relaciones entre muchos elementos sin cruces visuales.
- **Bipartite graph** — conexiones entre dos conjuntos distintos.

## G — Flujo y proceso

- **Flowchart** — pasos y decisiones.
- **Sankey** — flujo con grosor proporcional.
- **Alluvial** — migración de categorías a través del tiempo.
- **Swimlanes** — procesos separados por actor o subsistema.
- **State machine** — estados y transiciones.
- **Funnel** — conversión o pérdida progresiva.

## H — Densidad, intensidad y patrones escondidos

- **Heatmap** — intensidad por color.
- **Calendar heatmap** — actividad temporal por día.
- **Hexbin** — densidad agrupada en celdas hexagonales.
- **Contour / isolines** — zonas de igual intensidad.
- **Density plot** — concentración probabilística.
- **Ridgeline** — distribución comparada de múltiples grupos.
- **Spectrogram** — energía/frecuencia a través del tiempo.

## I — Topología y territorio semántico

- **Topografía semántica** — montañas y valles de relevancia/intensidad.
- **Voronoi** — territorio asignado por proximidad.
- **Delaunay** — conectividad espacial entre puntos próximos.
- **Isosurfaces** — superficies de igual valor en 3D.
- **Elevation map** — valor convertido en altura.
- **Manifold projection** — espacio complejo reducido a 2D/3D.

## J — Jerarquía

- **Árbol** — padre → hijos.
- **Dendrograma** — similitud y clustering.
- **Icicle** — jerarquía rectangular por profundidad.
- **Treemap** — jerarquía por área.
- **Sunburst** — jerarquía radial.
- **Pirámide** — niveles o prioridad.

## K — 3D y multidimensional

- **Scatter 3D** — tres variables espaciales.
- **Surface 3D** — picos, valles y gradientes.
- **Mesh** — geometría discreta de una superficie.
- **Volume rendering** — densidad interna de un volumen.
- **Point cloud** — estructura emergente a partir de puntos.
- **Capas 3D / estratos** — dimensiones superpuestas.
- **Burbujas 3D** — magnitud + posición + agrupación.

## L — Simbólica y semántica

- **Iconografía** — símbolos asociados a estados.
- **Badges** — etiquetas de clasificación rápida.
- **Semáforos** — estado por color.
- **Glifos** — una sola figura codifica varias variables.
- **Forma** — círculo, triángulo, cuadrado, hexágono como categoría.
- **Tamaño** — magnitud.
- **Color** — estado o intensidad.
- **Brillo** — relevancia / energía.
- **Borde** — confianza, riesgo o anomalía.
- **Movimiento** — velocidad, dirección, urgencia.
- **Textura** — incertidumbre, densidad o clase.

---

# 3. Diccionario visual BlackMamba Watchdog

| Símbolo | Estado | Semántica visual |
|---|---|---|
| 🟢 **▲** | crecimiento | verde, ascenso |
| 🔴 **▼** | caída | rojo, descenso |
| ⚖️ / ☯️ | estable | equilibrio / neutralidad |
| ⚡ | aceleración | aumento de velocidad |
| 🔥 | breakout | ruptura de baseline |
| 🚀 | viralidad | propagación sostenida |
| 🟣 **✦** | actividad extraordinaria | evento raro de alto valor |
| ⚠️ | anomalía | desviación a investigar |
| 💎 | engagement excepcional | interacción de alta calidad |
| ☠️ | pérdida de momentum | desaceleración / agotamiento |

> Un símbolo representa **estado**. Una gráfica representa **comportamiento**. Una geometría representa **estructura**. Varias capas combinadas representan **contexto**.

---

# 4. Selección por pregunta

| Quiero entender… | Representaciones recomendadas |
|---|---|
| cuánto | barras, línea, dot plot |
| cambio | línea, velas, slope, timeline |
| velocidad | línea derivada, vector, sparkline |
| aceleración | segunda derivada, vector, phase portrait |
| proporción | donut, treemap, waffle |
| relación | network, matrix, chord |
| flujo | Sankey, alluvial, streamlines |
| jerarquía | árbol, sunburst, treemap |
| densidad | heatmap, hexbin, contours |
| multidimensión | radar, glyph, scatter 3D |
| ciclos | radial, polar, órbitas |
| geografía | mapa, hexbin, choropleth |
| significado oculto | capas, glifos, topografía, anillos |
| cambio de paradigma | before/after + cambio de geometría/base |
| incertidumbre | bandas, error bars, transparencia, textura |

---

# 5. Dimensiones visuales disponibles

Un dato no tiene que representarse únicamente con la posición de una línea.

Podemos codificar información mediante:

1. **posición X**
2. **posición Y**
3. **posición Z**
4. **ángulo**
5. **distancia al centro**
6. **dirección**
7. **longitud**
8. **área**
9. **volumen**
10. **tamaño**
11. **forma**
12. **color**
13. **saturación**
14. **luminosidad**
15. **transparencia**
16. **textura**
17. **grosor de línea**
18. **tipo de línea**
19. **borde**
20. **conectividad**
21. **densidad**
22. **proximidad**
23. **movimiento**
24. **velocidad**
25. **aceleración**
26. **frecuencia de pulso**
27. **rotación**
28. **profundidad**
29. **oclusión**
30. **capa / estrato**

Estas variables pueden combinarse. Ejemplo de un glifo de track:

```text
posición   = contexto
radio      = plays
color      = crecimiento
brillo     = engagement
borde      = anomalía
giro        = velocidad
pulso      = aceleración
satélite   = mercado geográfico emergente
```

---

# 6. Regla de oro

**No elegir una gráfica porque “se ve bonita”.**

Elegirla según la estructura real de la información:

```text
Dato → Pregunta → Relación → Geometría → Codificación → Lectura
```

Y cuando una sola geometría no alcanza:

```text
CAPA 1  magnitud
CAPA 2  tendencia
CAPA 3  velocidad
CAPA 4  anomalía
CAPA 5  contexto
CAPA 6  significado
```

Eso convierte una gráfica en un **sistema de observación**.

---

# 7. Aplicación inmediata al Watchdog

Para métricas musicales:

- **Sparkline** → tendencia instantánea por track.
- **Candlestick** → volatilidad por intervalo.
- **Radar** → huella multidimensional del track.
- **Heatmap** → hora × día × actividad.
- **Hexbin** → densidad geográfica o de usuarios.
- **Sankey** → fuente → track → engagement.
- **Network** → ciudades / tracks / audiencias conectadas.
- **Sunburst** → catálogo → género → release → track.
- **Vector field** → dirección del momentum entre segmentos.
- **Topografía** → paisaje de actividad del catálogo.
- **Glifos** → resumen compacto de múltiples métricas.
- **3D layers** → dimensiones ocultas superpuestas.

---

## Objetivo del repositorio

Construir un **lenguaje visual reusable** para que cualquier sistema de BlackMamba pueda elegir automáticamente la representación adecuada según el tipo de información observada.

No solo mostrar datos.

**Mostrar estructura, dinámica, contexto y significado.**
