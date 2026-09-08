# Prompts para Análisis Estadístico - Capítulo 2

## Prompts Básicos

### 1. Resumen Estadístico
```
Actúa como un científico de datos escéptico. Analiza el dataset de ventas y proporciona un resumen estadístico completo que incluya:
- Medidas de tendencia central (media, mediana, moda)
- Medidas de dispersión (desviación estándar, IQR, rango)
- Coeficiente de variación para cada variable
- Análisis de sesgo (skewness)
- Identificación de outliers con método IQR

No confíes en la media sin verificar la distribución.
```

### 2. Análisis de Distribuciones
```
Explora las distribuciones de las variables numéricas del dataset. Para cada variable:
1. Genera histogramas con KDE
2. Identifica si la distribución es simétrica, sesgada a la derecha o izquierda
3. Detecta si hay múltiples modas (indicando subgrupos)
4. Compara media vs mediana para detectar sesgo
5. Sugiere transformaciones si es necesario

Recuerda: los histogramas son las huellas dactilares de tus datos.
```

### 3. Detección de Outliers
```
Identifica outliers en el dataset usando el método IQR. Para cada outlier encontrado:
1. ¿Es un error de datos o un valor legítimo?
2. ¿Qué impacto tiene en las estadísticas resumidas?
3. ¿Debería eliminarse, transformarse o mantenerse?

Los outliers no son necesariamente basura — a veces son la historia más interesante.
```

## Prompts Intermedios

### 4. Análisis de Correlaciones
```
Analiza las correlaciones entre las variables numéricas:
1. Genera la matriz de correlación con heatmap
2. Identifica correlaciones fuertes (>0.7 o <-0.7)
3. Analiza si las correlaciones tienen sentido causal
4. Busca correlaciones espurias (que no tienen relación lógica)
5. Identifica si alguna variable es redundante

Correlación no implica causalidad — ¡nunca lo olvides!
```

### 5. Análisis por Segmentos
```
Realiza un análisis segmentado del dataset:
1. Ventas y beneficio promedio por región
2. Ventas y beneficio promedio por categoría
3. Análisis combinado región + categoría
4. Identifica los segmentos más y menos rentables
5. Detecta patrones inesperados

Busca donde se esconden los problemas — a veces el promedio general oculta verdades incómodas.
```

### 6. Análisis Temporal
```
Analiza las tendencias temporales del dataset:
1. Ventas y beneficio mensual
2. Detecta estacionalidad
3. Identifica meses con mejor/peor rendimiento
4. Analiza si hay tendencias de crecimiento o decrecimiento
5. Visualiza las tendencias con gráficos de línea

Los datos temporales cuentan historias que los promedios ocultan.
```

## Prompts Avanzados

### 7. Análisis Ético de Datos
```
Realiza un análisis ético del dataset:
1. ¿Hay sesgos en la representación de regiones o categorías?
2. ¿Los outliers son errores o información valiosa?
3. ¿Las visualizaciones que has creado son honestas?
4. ¿Qué información estás omitiendo que podría ser relevante?
5. ¿Cómo afectarían tus conclusiones si ciertos datos estuvieran sesgados?

El análisis de datos no es neutral — siempre hay perspectivas que considerar.
```

### 8. Diagnóstico de Calidad de Datos
```
Diagnostica la calidad del dataset:
1. ¿Qué tan completo está? (valores nulos)
2. ¿Qué tan consistente está? (formatos, tipos)
3. ¿Qué tan preciso está? (outliers, errores)
4. ¿Qué tan actualizado está? (fechas)
5. ¿Qué tan representativo está? (sesgos de muestreo)

Los datos sucios producen conclusiones sucias.
```

### 9. Storytelling con Datos
```
Cuenta una historia con los datos del dataset:
1. ¿Cuál es el hallazgo más sorprendente?
2. ¿Cuál es el patrón más preocupante?
3. ¿Cuál es la oportunidad más grande?
4. ¿Qué pregunta no te estás haciendo que deberías hacer?
5. ¿Qué datos faltan para completar la imagen?

El objetivo no es hacer gráficos bonitos — es comunicar verdades.
```

## Prompts para Visualización

### 10. Dashboard Ejecutivo
```
Crea un dashboard ejecutivo con 4 gráficos clave:
1. KPI principal (ventas totales, margen de beneficio)
2. Tendencia temporal (ventas mensuales)
3. Comparativa por región (barras o boxplots)
4. Relación ventas-beneficio (scatter con centroides)

El dashboard debe contar una historia en 30 segundos.
```

### 11. Análisis de Outliers Visual
```
Crea una visualización que muestre claramente los outliers:
1. Boxplots por categoría
2. Scatter plots con outliers resaltados
3. Histogramas con regiones de outliers marcadas
4. Tabla resumen de outliers con métricas

Los outliers deben ser visibles, no escondidos.
```

### 12. Comparativa de Segmentos
```
Diseña una visualización que compare segmentos:
1. Small multiples por región
2. Heatmap de métricas por región y categoría
3. Gráficos de radar para comparar perfiles
4. Slope charts para cambios entre períodos

La comparación justa requiere las mismas escalas.
```

## Prompts para Machine Learning

### 13. Preparación para Modelado
```
Prepara el dataset para modelado:
1. Identifica variables candidatas para features
2. Detecta multicolinealidad entre predictores
3. Sugiere transformaciones para normalizar distribuciones
4. Recomienda estrategias para manejar outliers
5. Proporciona un pipeline de preprocesamiento

El modelado empieza aquí, no cuando escribimos el algoritmo.
```

### 14. Feature Engineering Inicial
```
Sugiere nuevas features basadas en el análisis exploratorio:
1. Agregaciones por categoría/región
2. Variables derivadas (ratio ventas/beneficio)
3. Indicadores de tendencia temporal
4. Variables de interacción entre predictores
5. Binning de variables continuas

Las mejores features vienen del entendimiento del dominio.
```

## Prompts de Validación

### 15. Sanity Check
```
Valida que tus análisis sean correctos:
1. ¿Los totales cuadran?
2. ¿Las medias son representativas?
3. ¿Las correlaciones tienen sentido?
4. ¿Los gráficos son honestos con las escalas?
5. ¿Las conclusiones están respaldadas por los datos?

La prudencia es la madre de la ciencia de datos.
```

### 16. Replicabilidad
```
Asegura que tu análisis sea replicable:
1. ¿El código está documentado?
2. ¿Los pasos están en orden lógico?
3. ¿Se pueden cambiar parámetros fácilmente?
4. ¿Los resultados son consistentes?
5. ¿Alguien más podría reproducir tu análisis?

Un análisis que no se puede replicar no es ciencia.
```

---

## Uso de Prompts

Cada prompt está diseñado para:
1. **Establecer el rol** (científico de datos escéptico)
2. **Definir el alcance** (qué analizar)
3. **Especificar el formato** (cómo presentar resultados)
4. **Incluir la perspectiva ética** (qué Considerar)

**Consejo:** Usa estos prompts como punto de partida y ajústalos según tu dataset específico y tus necesidades de análisis.
