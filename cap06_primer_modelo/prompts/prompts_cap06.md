# Prompts para el Capítulo 6: Construyendo el Primer Modelo

## Prompt 1: Configuración y Carga

```
Crea un notebook de Jupyter para el Capítulo 6 de un libro de Ciencia de Datos titulado "Construyendo el Primer Modelo (Del Código al Modelo)".

REGLAS OBLIGATORIAS (Mandamiento 3 - Taller Mecánico):
1. Estructura de cada bloque de código:
   - Líneas 1-5: Configuración y carga (por qué esa versión de librería)
   - Líneas 6-15: Transformación ETL (con antes/después de df.head())
   - Líneas 16-25: El modelo
   - Línea 26: model.fit()
   - Líneas 27-35: El Post-Mortem
2. NO datasets de juguete.
3. Ética incrustada.
4. Voz escéptica.

CELDA 1: Configuración
- Importar pandas 2.0+, numpy, scikit-learn 1.3+
- Explicar POR QUÉ esas versiones específicas
- Incluir warnings.filterwarnings('ignore')
- Mostrar versiones al final

CELDA 2: Carga de datos
- Leer datos/datos_empleados_hr.csv
- Mostrar shape, columnas, distribución del target
- Dataset de empleados HR con 1470 registros y 23 features
- Target: Attrition (Yes/No)

CELDA 3: ANTES de la transformación
- df.head() ANTES del preprocesamiento
- Comentar qué mirar: categóricas crudos, rangos numéricos, encoding necesario
- Incluir nota ética sobre variables protegidas (Gender, Age)

CELDA 4: Transformaciones ETL
- OneHotEncoder para categóricas: Department, Gender, OverTime
- StandardScaler para numéricas: Age, DistanceFromHome, MonthlyIncome, etc.
- ColumnTransformer para aplicar transformaciones diferentes por tipo
- Explicar por qué cada transformación

CELDA 5: DESPUÉS de la transformación
- df.head() DESPUÉS del preprocesamiento
- Comparar con Celda 3: mismas filas, features transformadas
- Explicar la trampa del encoding (n-1 columnas)

CELDA 6: Split train/test
- train_test_split con test_size=0.2, random_state=42, stratify=y
- Explicar por qué stratify (mantener proporción de clases)
- Explicar la trampa del leakage (fit solo en train)

CELDA 7: Modelo Random Forest
- RandomForestClassifier con hiperparámetros justificados:
  - n_estimators=200
  - max_depth=10
  - min_samples_split=10
  - min_samples_leaf=5
  - class_weight='balanced'
  - random_state=42
  - n_jobs=-1

CELDA 8: Entrenamiento
- model.fit() con medición de tiempo
- Explicar qué hace internamente (bootstrap, feature sampling, votación)

CELDA 9: Predicciones
- model.predict() y model.predict_proba()
- Distribución de predicciones
- Pregunta ética: ¿qué hacemos con la predicción?

CELDA 10: Reporte de clasificación
- classification_report con target_names=['No', 'Yes']
- Explicar precision, recall, F1
- Recordar que para rotación importa RECALL

CELDA 11: Matriz de confusión
- confusion_matrix con interpretación clara
- Explicar TN, FP, FN, TP
- Enfatizar que FN es el peor escenario

CELDA 12: Post-Mortem
- Feature importance (top 10)
- Análisis de errores (FN vs FP)
- Sesgos potenciales (Gender, Age)
- Lecciones aprendidas

METÁFORAS A INCLUIR:
- Pipeline como "línea de montaje de fábrica"
- Train/test split como "examen final vs ejercicios de clase"
- Overfitting como "memorizar el examen sin entender la materia"
```

## Prompt 2: Markdown del Capítulo

```
Crea el archivo markdown para el Capítulo 6 de un libro de Ciencia de Datos.

ESTRUCTURA:
1. Introducción: "Construir un modelo es como cocinar - necesitas la receta correcta"
2. Pipeline completo de ML (línea de montaje de fábrica)
3. Configuración y carga (por qué versiones específicas)
4. Preprocesamiento (antes/después de transformaciones)
5. Entrenamiento (el corazón del modelo)
6. Evaluación (métricas que importan)
7. Post-Mortem (qué salió mal)
8. Ética (lo que el modelo aprendió de nosotros)

METÁFORAS:
- Pipeline como "línea de montaje de fábrica"
- Train/test split como "examen final vs ejercicios de clase"
- Overfitting como "memorizar el examen sin entender la materia"
- Random Forest como "SUV del ML"

SECCIÓN POST-MORTEM:
- Error 1: "Mi modelo tiene 95% de accuracy" → Clases desbalanceadas
- Error 2: "Overfitea — 99% en train, 70% en test" → Modelo memorizó
- Error 3: "Las métricas cambian cada vez que entreno" → Datos insuficientes
- Error 4: "Mi modelo predice todo como 'No'" → Clases desbalanceadas + default
- Error 5: "Feature importance no tiene sentido" → Features correlacionadas

SECCIÓN ÉTICA:
- El espejo del pasado: el modelo aprende del pasado
- Preguntas éticas: ¿qué features? ¿qué no vemos? ¿para qué se usa?
- Buenas prácticas: auditar, buscar proxies, evaluar equidad, documentar

CITAS:
- Pedregosa, F., et al. (2011). "Scikit-learn: Machine Learning in Python". JMLR, 12, 2825-2830.
- Müller, A. C., & Guido, S. (2016). "Introduction to Machine Learning with Python". O'Reilly.
- Molino, P. (2023). "Machine Learning Design Patterns". O'Reilly.

REGLAS:
1. Todo en español
2. Voz escéptica
3. Ética incrustada, no al final
4. Metáforas claras
5. Código con comentarios explicativos
```

## Prompt 3: Dataset

```
Crea un dataset CSV para el Capítulo 6 sobre predicción de rotación de empleados.

ESPECIFICACIONES:
- Nombre: datos_empleados_hr.csv
- 1470 registros (o similar, dataset realista)
- Target: Attrition (Yes/No)
- Features numéricas: Age, DistanceFromHome, MonthlyIncome, NumCompaniesWorked, PercentSalaryHike, TotalWorkingYears, TrainingTimesLastYear, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager
- Features categóricas: Department, Gender, OverTime
- Features ordinales: Education, EnvironmentSatisfaction, JobInvolvement, JobLevel, JobSatisfaction, PerformanceRating, RelationshipSatisfaction, StockOptionLevel, WorkLifeBalance

DISTRIBUCIÓN DEL TARGET:
- ~84% No (empleados que se quedaron)
- ~16% Yes (empleados que renunciaron)
- DESBALANCE intencional para enseñar métricas

NOTAS ÉTICAS:
- Incluir Gender (Male/Female) para discutir sesgos
- Incluir Age para discutir discriminación por edad
- Dataset basado en IBM HR Analytics Employee Attrition

ESTRUCTURA:
15 filas de ejemplo:
- Edades variadas (18-60)
- Diferentes departamentos (Sales, R&D, HR)
- Diferentes niveles de satisfacción
- Algunos con OverTime=Yes, otros No
- Mezcla de Attrition=Yes y No
```

## Prompt 4: Evaluación

```
Crea las preguntas de evaluación para el Capítulo 6.

PREGUNTAS DE COMPRENSIÓN:
1. ¿Por qué usamos train_test_split con stratify=y?
2. ¿Qué transformaciones aplicamos y por qué?
3. ¿Cuál es la diferencia entre precision y recall?
4. ¿Por qué el recall es más importante que el accuracy para predicción de rotación?
5. ¿Qué es el post-mortem y por qué es importante?

PREGUNTAS DE APLICACIÓN:
1. Modifica el pipeline para usar XGBoost en vez de RandomForest. ¿Qué cambia?
2. Prueba con test_size=0.3 en vez de 0.2. ¿Cómo afecta las métricas?
3. Elimina class_weight='balanced'. ¿Qué pasa con el recall?
4. Aumenta max_depth a 20. ¿Overfitea?
5. Agrega una feature proxy (ej: código postal). ¿Cómo afecta la importancia?

PREGUNTAS ÉTICAS:
1. Si el modelo predice que una mujer tiene mayor probabilidad de renunciar, ¿es ético usar esa predicción?
2. ¿Qué features deberíamos eliminar antes de entrenar?
3. ¿Cómo sabemos si nuestro modelo perpetúa sesgos?
4. ¿Quién debería validar un modelo que afecta decisiones de RH?
5. ¿Es ético usar un modelo que tiene 90% de accuracy pero 60% de fairness?

PREGUNTAS DE REFLEXIÓN:
1. ¿El 80% de tiempo en ETL es realista o una exageración?
2. ¿Un modelo siempre es mejor que la intuición humana?
3. ¿Qué pasaría si todo el mundo usara el mismo modelo?
4. ¿El post-mortem debería ser un paso obligatorio?
5. ¿La ética en ML es una responsabilidad individual o institucional?
```
