# Prompts para Capítulo 14: Segmentación Inteligente de Clientes

## 1. Generación de Nombres de Cluster con IA

```
Eres un estratega de marketing y data scientist. He ejecutado un algoritmo K-Means sobre
3000 clientes de e-commerce y obtuve los siguientes perfiles clusterizados:

Cluster 0 (n=612):
  - Compras totales promedio: 78
  - Valor promedio de orden: $245.30
  - Días desde última compra: 22
  - Engagement con emails: 0.78
  - Tickets de soporte: 2.1
  - Lifetime value: $14,520

Cluster 1 (n=588):
  - Compras totales promedio: 45
  - Valor promedio de orden: $380.50
  - Días desde última compra: 180
  - Engagement con emails: 0.35
  - Tickets de soporte: 8.4
  - Lifetime value: $8,900

Cluster 2 (n=634):
  - Compras totales promedio: 12
  - Valor promedio de orden: $65.20
  - Días desde última compra: 290
  - Engagement con emails: 0.12
  - Tickets de soporte: 1.2
  - Lifetime value: $420

Cluster 3 (n=567):
  - Compras totales promedio: 95
  - Valor promedio de orden: $180.00
  - Días desde última compra: 15
  - Engagement con emails: 0.85
  - Tickets de soporte: 3.5
  - Lifetime value: $12,300

Cluster 4 (n=599):
  - Compras totales promedio: 30
  - Valor promedio de orden: $420.00
  - Días desde última compra: 45
  - Engagement con emails: 0.60
  - Tickets de soporte: 0.8
  - Lifetime value: $7,200

Para cada cluster genera:
1. Un nombre evocador y memorable (máximo 3 palabras)
2. Un eslogan de marketing (máximo 8 palabras)
3. Una estrategia de retención de 1 línea
4. Un riesgo ético potencial de segmentación

Formato: Markdown con tabla.
```

## 2. Evaluación de Ética en Segmentación

```
Sos experto en ética de datos y legislación de protección de datos. Analiza esta
segmentación de clientes de e-commerce y responde:

¿Puede esta segmentación generar discriminación indirecta?
¿Qué variables de este dataset podrían correlacionar con características protegidas?
¿Cómo mitigate los riesgos de que los segmentos se usen para negar servicios?

Contexto:
- Dataset de 3000 clientes con 10 variables
- Variables: compras totales, valor promedio de orden, días desde última compra,
  categoría preferida, engagement con emails, tickets de soporte, lifetime value,
  región geográfica, fecha de registro
- Segmentación por K-Means con 5 clusters
```

## 3. Prompt para Análisis Comparativo

```
Genera un análisis comparativo de los 5 segmentos de clientes. Incluye:
1. Cuadro comparativo con las métricas clave de cada segmento
2. Recomendación de canal de comunicación ideal por segmento
3. Sugerencia de oferta personalizada por segmento
4. Métrica de éxito para evaluar la efectividad de cada estrategia
```

## 4. Prompt para Visualización Recomendada

```
Sugiere 3 tipos de visualizaciones diferentes para comunicar los resultados
de esta segmentación a un equipo directivo no técnico. Para cada una explica:
- Qué tipo de gráfico usar
- Qué variables incluir en ejes
- Qué mensagem clave transmite
- Herramienta sugerida (Python, Tableau, PowerBI)
```
