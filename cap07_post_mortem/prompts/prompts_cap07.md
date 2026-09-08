# Prompts Capítulo 7: El Post-Mortem (¿Qué Hizo Mal el Modelo y por Qué?)

## Prompt 1: Diagnosticar un modelo que falla en producción
```
Mi modelo de predicción de churn tiene estos resultados en producción:
- Accuracy: 0.87
- Precision: 0.72
- Recall: 0.31
- F1: 0.43
- AUC: 0.78

Los stakeholders están molestos. El modelo "detecta" churn pero se perdieron 3 clientes importantes este mes.

Dame un diagnóstico completo:
1. ¿Qué métricas están fallando y por qué?
2. ¿Cuáles son las 3 causas más probables?
3. ¿Qué hago primero (plan de acción priorizado)?
4. ¿Cómo presento esto a un stakeholder no técnico?

Sé directo. Sin rodeos. Come si fuera tu post-mortem real.
```

## Prompt 2: Explicar la matriz de confusión a un CEO
```
Necesito explicarle a mi CEO por qué el accuracy de 85% no significa que el modelo funcione.

Usa la analogía del detector de humo:
- El detector de humo suena 85 veces de cada 100 cuando hay humo
- Pero suena 85 veces de cada 100 cuando NO hay humo
- Entonces el 85% de accuracy es inútil

Convierte esto en una explicación de 3 oraciones que un CEO entienda.
Incluye una tabla comparativa de métricas con sus definiciones.
```

## Prompt 3: Crear un post-mortem de proyecto real
```
Escribe un post-mortem detallado de este escenario ficticio:

CONTEXTO:
- Equipo de 3数据 scientists construyeron un modelo de scoring crediticio
- El modelo tenía AUC=0.92 en testing
- Se desplegó en producción hace 3 meses
- Ahora hay 40% más de impagos que el año pasado

DATOS:
- Accuracy en test: 0.91
- Accuracy en producción: 0.74
- Recall para "buenos pagadores": 0.95
- Recall para "malos pagadores": 0.45

INCLUYE:
1. Timeline de lo que pasó
2. Qué salió bien (sí, hay cosas)
3. Causa raíz de cada problema
4. Lecciones aprendidas
5. Plan de acción para los próximos 30/60/90 días
6. Template reutilizable para futuros post-mortems

Tono: senior data scientist hablando con su equipo. Honestidad brutal.
```

## Prompt 4: Auditar fairness de un modelo
```
Tengo un modelo de predicción de rotación de empleados. Necesito auditar si es justo.

Métricas por género:
- Hombres: Recall=0.78, Precision=0.65
- Mujeres: Recall=0.62, Precision=0.71

¿Qué problema ves? ¿Es discrimination? ¿Qué hago?

Incluye:
1. Análisis de las métricas (¿qué significan estas diferencias?)
2. Criterios legales (GDPR, leyes anti-discriminación)
3. 3 opciones con sus pros/contras
4. Recomendación con justificación
5. Código Python para calcular métricas de fairness

Sé específico. No des respuestas genéricas.
```

## Prompt 5: Métricas alternativas al accuracy
```
Mi manager me pregunta: "¿Por qué no usamos accuracy como métrica principal?"

Genera una guía que incluya:
1. Cuándo SÍ usar accuracy
2. Cuándo NO usar accuracy
3. 5 métricas alternativas con sus fórmulas
4. Ejemplo numérico de cada una (misma matriz de confusión, diferentes métricas)
5. Tabla de decisión: qué métrica usar según el problema

Formato: Markdown limpio, listo para copiar a un reporte.
```

## Prompt 6: Plan de mejora para un modelo malo
```
Mi modelo tiene estos problemas:
- Overfitting (train acc=0.98, test acc=0.71)
- Clases desbalanceadas (90% vs 10%)
- 5 features irrelevantes de 20
- Sin regularización
- Threshold en 0.5

Dame un plan de mejora paso a paso, priorizado por impacto/esfuerzo.

Para cada paso:
- Qué hacer
- Por qué (justificación técnica)
- Código Python
- Métrica esperada de mejora
- Tiempo estimado

Ordena de mayor a menor impacto. Sé práctico.
```

## Prompt 7: Documentar sesgos conocidos
```
Necesito crear una "ficha técnica" de un modelo de scoring crediticio que documente sus sesgos conocidos.

Incluye:
1. Variables que podrían codificar sesgos (raza, género, ubicación)
2. Proxy variables (variables que correlacionan con protegidas)
3. Limitaciones del dataset (qué poblaciones están underrepresentadas)
4. Riesgos de uso indebido
5. Recomendaciones de monitoreo

Formato: template reutilizable que pueda adaptar a otros modelos.
```

## Prompt 8: Preparar una presentación de post-mortem
```
Tengo que presentar un post-mortem de un proyecto que falló ante la dirección general.

Crea una estructura de presentación de 10 slides:
1. Portada
2. Contexto (qué construimos y por qué)
3. Resultados esperados vs reales
4. Timeline de incidentes
5. Qué salió bien
6. Causa raíz (diagrama)
7. Impacto en el negocio
8. Lecciones aprendidas
9. Plan de acción
10. Preguntas

Para cada slide:
- Título
- 3-5 puntos clave
- Notas del presentador
- Visual sugerido

Tono: profesional, honesto, orientado a soluciones.
```
