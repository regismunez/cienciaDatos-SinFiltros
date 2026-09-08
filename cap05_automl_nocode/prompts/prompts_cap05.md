# Prompts para el Capítulo 5: AutoML y Herramientas No-Code

## Análisis Exploratorio

### Prompt 1: Análisis general del dataset
```
Tengo un dataset de rotación de clientes SaaS con 2000 filas. Las columnas son:
- customer_id: identificador único
- company_size: Small, Medium, Enterprise
- plan: Basic, Professional, Enterprise
- monthly_usage: uso mensual del producto
- support_tickets: tickets de soporte abiertos
- contract_length: duración del contrato en meses
- monthly_revenue: ingreso mensual por cliente
- churned: 1 si el cliente se fue, 0 si se quedó
- days_since_last_login: días desde último login
- num_users: número de usuarios en la cuenta
- industry: sector del cliente

Haz un análisis exploratorio completo. Identifica:
1. Distribución de la variable objetivo (churned)
2. Variables numéricas con mayor correlación con churn
3. Patrones por plan y tamaño de empresa
4. Valores atípicos o anomalies
5. Recomendaciones de features para un modelo predictivo
```

### Prompt 2: Análisis de correlaciones
```
Analiza las correlaciones entre las variables del dataset de churn. Responde:
1. ¿Qué variables están más correlacionadas entre sí?
2. ¿Hay multicolinealidad problemática?
3. ¿Qué variables parecen tener relación causal con churn (no solo correlación)?
4. Sugiere 3 features derivados que podrían mejorar un modelo predictivo
```

## Construcción de Modelos

### Prompt 3: Comparación de algoritmos
```
Quiero comparar los siguientes algoritmos para predecir churn:
- Regresión logística
- Random Forest
- Gradient Boosting (XGBoost o LightGBM)
- Support Vector Machine

Para cada uno, genera el código en Python con:
1. Preprocesamiento adecuado
2. Validación cruzada de 5 folds
3. Métricas: AUC-ROC, precision, recall, F1
4. Matriz de confusión

Explica cuál elegirías y por qué, considerando que necesito explicar el modelo a stakeholders no técnicos.
```

### Prompt 4: H2O AutoML
```
Genera código en Python para usar H2O AutoML con el dataset de churn. Incluye:
1. Inicialización de H2O
2. Carga y preparación de datos
3. Configuración de AutoML (max_models=10, seed=42)
4. Entrenamiento y leaderboard
5. Extracción del mejor modelo
6. Evaluación en test set
7. Guardado del modelo en MOJO

Explica cada paso y las decisiones que toma AutoML automáticamente.
```

## Explicabilidad y Ética

### Prompt 5: SHAP values
```
Explica cómo usar SHAP (SHapley Additive exPlanations) para interpretar un modelo de Gradient Boosting entrenado con el dataset de churn. Genera código que muestre:
1. SHAP summary plot (importancia global de variables)
2. SHAP dependence plot para las 2 variables más importantes
3. SHAP force plot para un cliente específico que churned
4. SHAP waterfall plot explicando la predicción

Interpreta los resultados en lenguaje de negocio, no técnico.
```

### Prompt 6: Evaluación ética
```
Diseña un protocolo de evaluación ética para el modelo de churn. El modelo se usará para decidir a qué clientes ofrecer descuentos de retención. Incluye:
1. Definición de fairness para este caso de uso
2. Métricas de fairness a calcular
3. Código para detectar sesgos por industry y company_size
4. Plan de monitoreo continuo
5. Escenarios donde el modelo podría causar daño
```

## Herramientas No-Code

### Prompt 7: KNIME vs. Python
```
Compara KNIME y Python para un proyecto de ciencia de datos con las siguientes características:
- Equipo: 2 analistas (saben Excel, no saben programar) + 1 data scientist
- Datos: 500K filas, 20 variables
- Objetivo: modelo de churn para retención
- Presupuesto: limitado
- Timeline: 4 semanas

Recomienda qué herramienta usar para cada fase del proyecto y justifica tu respuesta.
```

### Prompt 8: Power Query para datos de churn
```
Explora qué transformaciones de Power Query serían útiles para preparar datos de churn antes de modelar. Incluye:
1. Ejemplos de DAX para métricas de churn
2. Transformaciones de Power Query para limpiar datos
3. Limitaciones de Power Query vs. Python para este caso
4. Cuándo migrar de Excel/Power BI a código
```

## Casos Prácticos

### Prompt 9: Caso de negocio
```
Un CEO te pregunta: "¿Por qué debemos invertir en un data scientist si tenemos H2O AutoML que hace todo automáticamente?"

Responde con:
1. Qué hace bien AutoML (y es genuinamente útil)
2. Qué NO puede hacer AutoML (y por qué importa)
3. El costo real de un modelo que nadie entiende
4. Un ejemplo concreto de fracaso por usar AutoML sin supervisión
5. La propuesta de valor de un data scientist
```

### Prompt 10: Modelo en producción
```
Diseña un pipeline de MLOps para un modelo de churn que:
- Se reentrena semanalmente
- Tiene requisitos de explicabilidad (regulación financiera)
- Necesita monitoreo de drift
- Debe integrarse con el CRM de la empresa

Incluye decisiones sobre:
1. ¿AutoML o código personalizado?
2. Herramientas de monitoreo
3. Estrategia de A/B testing
4. Rollback en caso de degradación
