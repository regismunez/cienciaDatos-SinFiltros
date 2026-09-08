# Prompts Capítulo 4: El Bosque y el Boost (Modelos de Árboles)

## Prompt 1: Generar el dataset HR
```
Genera un dataset de 1500 filas para un proyecto de predicción de rotación de empleados (HR Analytics). 

Columnas requeridas:
- Age (18-59), Department (Sales, R&D, HR), DistanceFromHome (1-29 km)
- Education (1-5), EnvironmentSatisfaction (1-4), Gender (Male/Female)
- JobInvolvement (1-4), JobLevel (1-5), JobSatisfaction (1-4)
- MonthlyIncome (1000-20000), NumCompaniesWorked (0-10), OverTime (Yes/No)
- PercentSalaryHike (11-25), PerformanceRating (1-4)
- RelationshipSatisfaction (1-4), StockOptionLevel (0-3)
- TotalWorkingYears (0-39), TrainingTimesLastYear (0-7)
- WorkLifeBalance (1-4), YearsAtCompany (0-39)
- YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager
- Attrition (Yes/No, ~15% tasa de rotación)

Requisitos:
- Sesgo de género implícito en MonthlyIncome (hombres ~6-8% más)
- Attrition más frecuente cuando: OverTime=Yes, JobSatisfaction baja, WorkLifeBalance bajo
- Distribuciones realistas para datos de empresa
```

## Prompt 2: Explicar Random Forest a un CEO
```
Explícame Random Forest como si fuera un CEO sin背景 técnico. 

Usa la analogía de "opinión de 100 expertos diferentes". 

Explica:
1. Por qué no basta con un solo árbol (un solo experto puede estar equivocado)
2. Cómo se diversifican (cada experto ve datos diferentes)
3. Por qué el promedio funciona mejor (sabiduría de la multitud)
4. Qué hiperparámetros debo preocuparme y cuáles puedo ignorar

Sé conciso. Máximo 5 minutos de lectura.
```

## Prompt 3: Diagnosticar overfitting en XGBoost
```
Mi XGBoost tiene estos resultados:
- Train accuracy: 0.98
- Test accuracy: 0.71
- Train F1: 0.97
- Test F1: 0.45

¿Qué está pasando? Dame un plan de acción paso a paso para diagnosticar y corregir. 

Incluye:
1. Causas probables (enumerate)
2. Qué hiperparámetros revisar primero
3. Qué métricas mirar además de accuracy
4. Código Python con las correcciones
```

## Prompt 4: Feature Importance ético
```
Estoy usando Random Forest para predecir rotación de empleados. La importancia de features muestra:

1. OverTime: 0.23
2. MonthlyIncome: 0.18
3. Age: 0.12
4. YearsAtCompany: 0.10
5. JobSatisfaction: 0.09
6. Gender: 0.07
7. DistanceFromHome: 0.06

¿Qué problemas éticos ves? ¿Cómo reformularías el modelo para evitar sesgos sin perder poder predictivo?

Sé específico con acciones concretas.
```

## Prompt 5: Comparar modelos para un reporte ejecutivo
```
Genera una tabla comparativa Markdown de estos modelos para un reporte ejecutivo:

| Modelo | Accuracy | F1-Score | AUC-ROC | Tiempo entrenamiento | Explicabilidad | Complejidad de tuning |

Modelos: Random Forest, XGBoost, LightGBM, Regresión Logística (baseline)

Incluye:
- Cuándo usar cada uno
- Riesgos de cada uno
- Recomendación final para producción

Formato: tabla + 3 oraciones de conclusión
```

## Prompt 6: Post-Mortem de un proyecto real
```
Escribe un post-mortem ficticio pero realista de un proyecto donde un modelo de árboles falló en producción.

Incluye:
1. Qué se construyó (contexto)
2. Qué salió bien
3. Qué salió mal (3-4 incidentes)
4. Lecciones aprendidas
5. Qué se haría diferente

Tono: honesto, sin blame, enfocado en aprendizaje.
Estilo: ingeniero senior escribiendo para su equipo.
```
