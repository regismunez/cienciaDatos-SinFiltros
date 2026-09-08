# Prompts para Capítulo 3: El Modelo Maldito (Regresión Lineal y Logística)

## Prompt 1: Generación del Dataset

```
Genera un dataset CSV para una cafetería con las siguientes especificaciones:

ARCHIVO: datos_cafeteria.csv
COLUMNAS:
- date (formato YYYY-MM-DD, 180 días del 2024)
- transactions (número de transacciones diarias, rango 80-210)
- avg_order_value (valor promedio del pedido en USD, rango 5.50-8.20)
- total_revenue (transactions * avg_order_value + variación aleatoria)
- loyalty_signups (suscripciones al programa de lealtad, rango 2-28)
- day_of_week (lunes a domingo)
- is_holiday (1 si es festivo, 0 si no)
- weather (Sunny, Cloudy, Rainy)

PATRONES A INCLUIR:
1. Fines de semana (sábado y domingo) tienen ~40% más transacciones
2. Lunes tienen ~10% menos transacciones
3. Días festivos tienen ~20% más transacciones Y más loyalty_signups
4. Lluvia reduce transacciones ~15%
5. Tendencia ascendente gradual a lo largo del año (negocio creciendo)
6. Outliers en Navidad (25 dic), Año Nuevo (31 dic, 1 ene), Día de la Independencia (4 jul)
7. Correlación positiva entre transactions y total_revenue (~0.95)
8. Correlación positiva entre avg_order_value y total_revenue (~0.85)
9. loyalty_signups correlacionado con transactions (~0.90)

RESTRICCIONES:
- NO usar valores perfectamente lineales (agregar ruido realista)
- Incluir al menos 5 días con valores atípicos extremos
- total_revenue debe ser CALCULADO, no copiado de otro dataset
- El dataset debe tener sentido de negocio (una cafetería real)
```

---

## Prompt 2: EDA Rápido

```
Realiza un EDA rápido del dataset de cafetería. Incluye:

1. Información general del dataset (shape, dtypes, nulls)
2. Estadísticas descriptivas para cada columna numérica
3. Distribución de transacciones por día de la semana (boxplot)
4. Distribución de loyalty_signups por clima (violin plot)
5. Correlación entre variables numéricas (heatmap)
6. Detección de outliers usando IQR
7. Tendencia de total_revenue a lo largo del tiempo (serie temporal)
8. Análisis de días festivos vs normales

Cada gráfico debe tener título, etiquetas y ser interpretado en una celda markdown.
```

---

## Prompt 3: Regresión Lineal

```
Implementa una regresión lineal para predecir total_revenue usando:

VARIABLES INDEPENDIENTES:
- transactions
- avg_order_value
- is_holiday

PASOS:
1. Dividir datos en train (80%) y test (20%)
2. Estandarizar variables (StandardScaler)
3. Entrenar modelo LinearRegression
4. Imprimir coeficientes e intercepto
5. Interpretar cada coeficiente en contexto de negocio
6. Calcular R², RMSE, MAE en train y test
7. Graficar residuos vs predicciones
8. Verificar supuestos de regresión lineal

INTERPRETACIÓN ESPERADA:
- transactions: coeficiente positivo (~8-10 por transacción)
- avg_order_value: coeficiente positivo (~100-130 por dólar)
- is_holiday: coeficiente positivo (~200-300 en festivos)
```

---

## Prompt 4: Regresión Logística

```
Implementa una regresión logística para predecir loyalty_signups (convertido a binario: >10 = 1, <=10 = 0).

VARIABLES INDEPENDIENTES:
- transactions
- avg_order_value
- total_revenue
- is_holiday

PASOS:
1. Crear variable binaria loyalty_class
2. Dividir datos en train (80%) y test (20%)
3. Estandarizar variables
4. Entrenar modelo LogisticRegression
5. Imprimir coeficientes y odds ratios
6. Interpretar odds ratios en contexto de negocio
7. Calcular accuracy, precision, recall, F1
8. Generar matriz de confusión
9. Graficar curva ROC y calcular AUC

INTERPRETACIÓN ESPERADA:
- is_holiday: odds ratio ~2.0-2.5 (duplica probabilidad de suscripción)
- transactions: odds ratio > 1 (más transacciones = más suscripciones)
```

---

## Prompt 5: Comparación de Modelos

```
Compara los dos modelos implementados:

1. Regresión Lineal (predecir total_revenue)
2. Regresión Logística (predecir loyalty_class)

MÉTRICAS A COMPARAR:
- Lineal: R², RMSE, MAE
- Logística: Accuracy, Precision, Recall, F1, AUC

ANÁLISIS:
- ¿Cuál modelo es más interpretable?
- ¿Cuál tiene mejor rendimiento relativo a su tarea?
- ¿Qué variables son más importantes en cada modelo?
- ¿Hay overfitting? (comparar train vs test)
- ¿Qué mejorarías?

CONCLUSIÓN:
- ¿Cumple la regresión con el estándar de "prueba de fuego"?
- ¿Es suficiente para el problema de negocio?
```

---

## Prompt 6: Post-Mortem

```
Realiza un post-mortem de la implementación:

1. ERRORES COMETIDOS:
   - ¿Se violaron supuestos de regresión?
   - ¿Hay variables que deberían haberse excluido?
   - ¿Se manejaron correctamente los outliers?
   - ¿Se verificó la ética del modelo?

2. LECCIONES APRENDIDAS:
   - ¿Qué harías diferente la próxima vez?
   - ¿Qué supuestos fueron problemáticos?
   - ¿Qué métricas fueron más reveladoras?

3. MEJORAS PROPUESTAS:
   - ¿Qué variables faltan?
   - ¿Qué transformaciones mejorarían el modelo?
   - ¿Qué regularización aplicarías?

4. ÉTICA:
   - ¿Hay sesgo en las variables de entrada?
   - ¿El modelo podría discriminar?
   - ¿Se puede explicar cada predicción?
```

---

## Prompt 7: Extensiones del Capítulo

```
Genera código para extensiones avanzadas:

1. REGULARIZACIÓN:
   - Ridge Regression (L2)
   - Lasso Regression (L1)
   - ElasticNet (L1 + L2)
   - Comparar coeficientes con y sin regularización

2. FEATURE ENGINEERING:
   - Crear variable day_type (weekday/weekend)
   - Crear variable season (invierno/primavera/verano/otoño)
   - Crear lagged variables (ventas del día anterior)
   - Interacciones entre variables

3. VALIDACIÓN CRUZADA:
   - K-Fold Cross Validation
   - Time Series Split (para datos temporales)
   - Comparar scores entre métodos

4. DIAGNÓSTICOS AVANZADOS:
   - VIF (Variance Inflation Factor) para multicolinealidad
   - Test de Breusch-Pagan para heterocedasticidad
   - Q-Q plot para normalidad de residuos
   - Cook's distance para puntos influyentes
```

---

## Instrucciones de Uso

1. **Cada prompt es independiente** - puedes ejecutarlos en cualquier orden
2. **Los prompts asumen que ya existe el dataset** - ejecuta Prompt 1 primero
3. **Cada prompt incluye interpretación** - no solo código, sino explicación
4. **Los prompts son modulares** - puedes combinar o separar según necesidad
5. **Enfocados en negocio** - cada modelo tiene interpretación de cafetería

## Notas para el Autor

- El dataset tiene 180 días para ser manejable pero suficiente para análisis
- Los patrones semanales son clave para el EDA
- Los outliers en festivos generan discusión ética
- La correlación entre variables permite discutir multicolinealidad
- La variable loyalty_signups permite transición de lineal a logística
