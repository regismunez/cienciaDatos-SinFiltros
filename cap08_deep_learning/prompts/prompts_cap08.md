# Prompts Capítulo 8: Cuando los Árboles No Suficienten (Deep Learning)

## Prompt 1: Explicar Deep Learning a un ejecutivo
```
Explícame Deep Learning como si fuera un ejecutivo de empresa sin背景 técnico.

Usa la analogía del "misil guiado vs martillo".

Explica:
1. Qué es Deep Learning en términos simples
2. Cuándo SÍ usarlo (imágenes, texto, audio)
3. Cuándo NO usarlo (datos tabulares)
4. Cuál es el costo real (tiempo, dinero, complejidad)
5. Qué riesgos éticos implica

Sé conciso. Máximo 5 minutos de lectura.
```

## Prompt 2: Comparar MLP vs XGBoost para datos tabulares
```
Necesito justificar por qué NO usaremos Deep Learning para un proyecto de predicción de churn de clientes.

Genera una tabla comparativa Markdown:

| Criterio | MLP (Deep Learning) | XGBoost |
|----------|---------------------|---------|
| Accuracy esperado | ? | ? |
| Tiempo de entrenamiento | ? | ? |
| Hiperparámetros a tuneear | ? | ? |
| Necesita feature engineering | ? | ? |
| Explicabilidad | ? | ? |
| Costo computacional | ? | ? |
| Facilidad de implementación | ? | ? |

Incluye:
- Referencia al estudio Shwartz-Ziv & Armon (2022)
- Conclusión clara para el ejecutivo
- Recomendación final
```

## Prompt 3: Diseñar una CNN para un problema específico
```
Tengo un problema de clasificación de imágenes médicas (radiografías de pulmón).

Diseña una arquitectura CNN que:
1. Sea adecuada para imágenes de 224x224x3
2. Use transfer learning (no entrenar desde cero)
3. Tenga menos de 10M parámetros
4. Sea desplegable en CPU (no GPU)

Incluye:
- Arquitectura completa (capas y dimensiones)
- Hiperparámetros recomendados
- Data augmentation apropiado para imágenes médicas
- Métricas a monitorear (no solo accuracy)
- Consideraciones éticas (sesgo en datos médicos)

Formato: Código + explicación + advertencias éticas
```

## Prompt 4: Implementar LSTM para series temporales
```
Necesito predecir demanda de productos (series temporales diarias).

Diseña una solución LSTM que:
1. Maneje estacionalidad diaria, semanal y anual
2. Incluya features externas (festivos, promociones)
3. Sea eficiente en inferencia (< 100ms)
4. Incluya monitoreo de concept drift

Incluye:
- Arquitectura LSTM completa
- Pipeline de preprocesamiento
- Estrategia de re-entrenamiento
- Comparación con Prophet/ARIMA (¿realmente necesito LSTM?)
- Métricas de negocio (no solo RMSE)

Formato: Código + arquitectura + justificación
```

## Prompt 5: Implementar BERT para análisis de sentimiento
```
Necesito clasificar reseñas de clientes como positivas/negativas/neutras.

Compara:
1. BERT pre-entrenado (sin fine-tuning)
2. BERT con fine-tuning
3. TF-IDF + Logistic Regression
4. DistilBERT (versión ligera)

Para cada opción incluye:
- Accuracy esperado
- Tiempo de entrenamiento
- Tiempo de inferencia
- Memoria requerida
- Costo de infraestructura

Recomendación: ¿Cuándo vale la pena invertir en BERT vs quedarse con LR?
```

## Prompt 6: Auditoría ética de un modelo de DL
```
Diseña un protocolo de auditoría ética para un modelo de DL que:
- Clasifica solicitudes de préstamo
- Usa datos de 100,000 clientes históricos
- Incluye: edad, género, código postal, ingresos, historial crediticio

El protocolo debe incluir:

1. PRE-ENTRENAMIENTO:
   - Análisis de sesgo en datos de entrenamiento
   - Features prohibidas y proxies
   - Representatividad por grupo demográfico

2. DURANTE ENTRENAMIENTO:
   - Métricas de fairness a monitorear
   - Restricciones de equidad
   - Regularización contra sesgo

3. POST-ENTRENAMIENTO:
   - Pruebas de disparate impact
   - Análisis de errores por grupo
   - Explicabilidad de predicciones individuales

4. EN PRODUCCIÓN:
   - Monitoreo continuo de fairness
   - Alertas de drift de equidad
   - Proceso de revisión y apelación

Formato: Protocolo ejecutable con código de ejemplo
```

## Prompt 7: Debate: ¿DL es overkill para la mayoría de casos?
```
Escribe un debate provocador entre dos data scientists:

DATIENTE A: "Deep Learning es el futuro de todo. Si no usas DL, estás quedándote atrás."

DATIENTE B: "Deep Learning es overkill para el 90% de los casos de negocio. Los árboles siguen ganando."

Para cada lado, incluye:
- 3 argumentos principales
- Ejemplos reales que respalden su posición
- Contraargumentos al oponente
- Concesiones honestas

Conclusión: ¿Quién tiene razón? ¿O ambos?

Tono: Respetuoso pero directo. Estilo de debate académico.
```

## Prompt 8: Plan de carrera en Deep Learning
```
Soy un data scientist con 2 años de experiencia en ML tradicional (sklearn, XGBoost).

Quiero especializarme en Deep Learning. Diseña un plan de aprendizaje de 6 meses:

Mes 1-2: Fundamentos
- Qué aprender
- Recursos específicos (cursos, libros, papers)
- Proyectos prácticos

Mes 3-4: Especialización
- Elegir entre: Computer Vision, NLP, o Audio
- Curriculum de aprendizaje
- Portfolio de proyectos

Mes 5-6: Producción
- Deployment de modelos DL
- MLOps para DL
- Optimización de inferencia

Incluye:
- Certificaciones recomendadas
- Commidades y eventos
- Salarios esperados por especialización
- Errores comunes a evitar
```

## Prompt 9: Post-Mortem de un proyecto de DL fallido
```
Escribe un post-mortem ficticio pero realista de un proyecto donde Deep Learning fue la elección incorrecta.

Incluye:
1. Contexto del proyecto (qué se intentó resolver)
2. Por qué se eligió DL (argumentos técnicos y de negocio)
3. Qué salió mal (5-6 problemas concretos)
4. Cuánto dinero/tiempo se desperdició
5. Qué modelo final se usó (spoiler: no era DL)
6. Lecciones aprendidas
7. Regla de oro que implementaron después

Tono: honesto, sin blame, enfocado en aprendizaje.
Estilo: ingeniero senior escribiendo para su equipo.
```

## Prompt 10: Checklist antes de usar Deep Learning
```
Genera un checklist de 10 preguntas que todo data scientist debe hacerse ANTES de usar Deep Learning:

Para cada pregunta:
- La pregunta clara
- Si la respuesta es "NO" → qué alternativa usar
- Si la respuesta es "SÍ" → qué Consideraciones éticas agregar
- Ejemplo concreto

Formato: Lista numerada con respuestas esperadas
```
