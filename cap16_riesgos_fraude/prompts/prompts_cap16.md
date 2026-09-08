# Prompts para el Capítulo 16: Detección de Riesgos y Fraude en Tiempo Real

## Prompt 1: Análisis Exploratorio de Datos de Fraude

```
Eres un experto en ciencia de datos especializado en detección de fraude. 

Utilizando el dataset de transacciones (datos_transacciones_fraude.csv), realiza un análisis exploratorio completo que incluya:

1. Distribución de transacciones fraudulentas vs legítimas
2. Análisis de patrones por tipo de fraude (card_testing, account_takeover, velocity_fraud)
3. Distribución geográfica del fraude
4. Relación entre velocity_score y probabilidad de fraude
5. Análisis temporal: ¿a qué horas ocurre más fraude?
6. Correlación entre account_age_days y fraude

Presenta los hallazgos en español, con visualizaciones claras y conclusiones accionables. Incluye consideraciones éticas sobre posibles sesgos en los datos.
```

## Prompt 2: Construcción del Modelo de Detección

```
Eres un ingeniero de machine learning construyendo un sistema de detección de fraude en tiempo real.

Construye un pipeline completo que incluya:

1. Preprocesamiento de datos (manejo de outliers, encoding de variables categóricas)
2. Ingeniería de features relevantes para detección de fraude
3. Entrenamiento de algoritmos: Random Forest, Gradient Boosting, y Red Neuronal
4. Optimización de hiperparámetros
5. Selección del modelo basada en métricas de negocio

El sistema debe priorizar el recall sobre la precisión (mejor prevenir que dejar pasar fraude).

Consideraciones técnicas:
- El modelo debe ser capaz de inferir en <100ms
- Manejar desbalance de clases (fraude es minoritario)
- Incluir explicabilidad de decisiones (SHAP values)

Incluye código Python completo y explicaciones en español.
```

## Prompt 3: Sistema de Reglas de Negocio

```
Eres un experto en sistemas de fraude diseñando reglas de negocio para complementar un modelo de ML.

Diseña un motor de reglas que detecte:

1. Card Testing:
   - Más de 3 transacciones de monto < $10 en 5 minutos desde la misma IP
   - Más de 5 tarjetas diferentes desde el mismo dispositivo en 1 hora

2. Account Takeover:
   - Login desde país diferente + cambio de contraseña + transacción en < 30 minutos
   - Dispositivo nuevo + monto > 3x el promedio histórico

3. Velocity Fraud:
   - Más de 10 transacciones en 1 minuto desde la misma cuenta
   - Acumulación de puntos/recompensas > 2 desviaciones estándar

4. Friendly Fraud:
   - Usuario con > 2 disputas en 6 meses
   - Producto de alto valor + entrega rápida + disputa

Presenta las reglas en formato YAML o JSON para facilitar su implementación. Incluye umbrales justificables y mecanismos de evolución.
```

## Prompt 4: Evaluación Ética del Sistema

```
Eres un consultor ético evaluando un sistema de detección de fraude para una plataforma financiera.

Realiza una auditoría ética que incluya:

1. Análisis de sesgo algorítmico:
   - ¿El modelo penaliza usuarios de ciertos países o regiones?
   - ¿Los usuarios con cuentas nuevas son tratados injustamente?
   - ¿El velocity scoring afecta desproporcionadamente a ciertos grupos?

2. Evaluación de impacto:
   - Calcula la tasa de falsos positivos por segmento demográfico
   - Identifica poblaciones vulnerables que podrían ser afectadas
   - Evalúa si el sistema crea "zonas de exclusión digital"

3. Recomendaciones de mitigación:
   - Diseña un sistema de apelación para usuarios bloqueados
   - Propón métricas de equidad para monitoreo continuo
   - Establece umbrales diferenciados por contexto

4. Cumplimiento normativo:
   - RGPD (Europa)
   - Leyes de protección de datos de Latinoamérica
   - Principios de explicabilidad algorítmica

Presenta el informe en español, con hallazgos concretos y recomendaciones accionables. Cita a Bolton (2012) y Abdallah (2016) donde sea relevante.
```

## Prompt 5: Monitoreo y Mantenimiento del Sistema

```
Eres un ingeniero de MLops diseñando el sistema de monitoreo para un modelo de detección de fraude en producción.

Diseña un sistema de monitoreo que incluya:

1. Métricas de rendimiento del modelo:
   - Precisión, recall, F1-score en ventanas de 1 hora, 1 día, 1 semana
   - Distribución de scores de riesgo
   - Tasa de predicciones por clase (APPROVE, REVIEW, BLOCK)

2. Detección de drift:
   - Monitoreo de distribución de features (Population Stability Index)
   - Alertas cuando el PSI > 0.2 (cambio significativo)
   - Análisis de causas raíz cuando se detecta drift

3. Dashboard de operaciones:
   - Métricas en tiempo real (latencia, throughput, error rate)
   - Alertas de fraude agrupadas por tipo y severidad
   - ROI del sistema (fraude prevenido vs costo de operación)

4. Procesos de retrenamiento:
   - Trigger automático cuando recall cae por debajo del 85%
   - Validación A/B antes de desplegar nuevo modelo
   - Rollback automático si métricas críticas se degradan

Presenta el diseño en español, con diagramas y código de configuración de alertas (Prometheus/Grafana o similar).
```

## Prompt 6: Integración con Sistemas de Pago

```
Eres un arquitecto de software integrando un sistema de detección de fraude con una plataforma de pagos.

Diseña la integración considerando:

1. Requisitos de latencia:
   - La validación de fraude debe completarse en < 200ms
   - El sistema debe manejar 10,000 transacciones por segundo
   - Fallback a reglas simples si el modelo ML falla

2. Flujo de la transacción:
   - Validación de datos básicos
   - Cálculo de features en tiempo real (Redis/Kafka)
   - Scoring de riesgo
   - Decisión y logging
   - Notificación al usuario si es bloqueada

3. Estrategia de respuesta:
   - Score < 0.3: Aprobación automática
   - Score 0.3-0.7: Revisión automática con chance de aprobación
   - Score 0.7-0.9: Revisión manual obligatoria
   - Score > 0.9: Bloqueo automático + notificación

4. Manejo de edge cases:
   - Timeout del modelo: fallback a reglas
   - Servicio de features no disponible: scoring diferido
   - Alto volumen: escalado horizontal automático

Presenta la arquitectura en español, con diagramas de secuencia y código de integración.
```

## Prompt 7: Análisis de Impacto Financiero

```
Eres un analista financiero evaluando el ROI de un sistema de detección de fraude.

Contexto:
- Plataforma con 5 millones de transacciones mensuales
- Ticket promedio: $85
- Tasa de fraude actual: 2.1%
- Costo promedio por fraude exitoso: $420

Realiza un análisis que incluya:

1. Costo del fraude actual:
   - Pérdidas directas anuales
   - Costos operativos de investigación
   - Impacto en experiencia del usuario

2. Beneficios proyectados del sistema:
   - Reducción estimada de fraude (70-85%)
   - Ahorro en costos de investigación
   - Mejor conversión por mayor confianza

3. Costos de implementación:
   - Desarrollo e integración
   - Infraestructura en la nube
   - Mantenimiento y retrenamiento
   - Personal de monitoreo

4. ROI y Payback:
   - ROI a 1, 2 y 3 años
   - Punto de equilibrio
   - Sensibilidad a diferentes escenarios

Presenta el análisis en español con tablas comparativas y gráficos de tendencia.
```

## Prompt 8: Pruebas y Validación del Sistema

```
Eres un QA engineer probando un sistema de detección de fraude antes de su puesta en producción.

Diseña una suite de pruebas que incluya:

1. Pruebas unitarias:
   - Cálculo correcto de features
   - Score del modelo en rangos esperados
   - Reglas de negocio se aplican correctamente

2. Pruebas de integración:
   - Flujo completo: transacción → features → score → decisión
   - Latencia end-to-end < 200ms
   - Manejo de errores y timeouts

3. Pruebas de estrés:
   - 10,000 transacciones por segundo
   - Caída de servicios dependientes (Redis, Kafka)
   - Recuperación automática

4. Pruebas de validación de modelo:
   - Backtesting con datos históricos
   - Validación cruzada temporal
   - Comparación contra baseline (reglas simples)

5. Pruebas de equidad:
   - Tasa de falsos positivos por segmento
   - Consistencia de predicciones entre grupos
   - Ausencia de discriminación por variables protegidas

Presenta los casos de prueba en español con código Python (pytest) y resultados esperados.
```
