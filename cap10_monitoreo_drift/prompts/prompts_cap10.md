# Prompts para Capítulo 10: Monitoreando en Producción (Data Drift y Concept Drift)

## Contexto del Capítulo

Este capítulo aborda el monitoreo continuo de modelos de machine learning en producción, enfocándose en la detección de data drift y concept drift. Es el "Mandamiento 4" del libro: **El infierno que viene después del notebook**.

---

## Prompt 1: Explicación Conceptual

```
Explica de forma sencilla qué es el data drift y el concept drift en machine learning.
Usa una metáfora cotidiana (como el cambio climático o recetas de cocina) para que
un ejecutivo no técnico entienda por qué es importante monitorear modelos en producción.
Incluye ejemplos reales de negocios.
```

---

## Prompt 2: Código de Detección

```python
# Prompt para generar código de detección de drift

"""
Implementa una función en Python que detecte data drift usando el test de
Kolmogorov-Smirnov. La función debe:
1. Recibir dos arrays (datos de entrenamiento y datos de producción)
2. Calcular el estadístico KS y el p-valor
3. Clificar la severidad del drift (baja, media, alta, crítica)
4. Retornar un diccionario con los resultados
5. Incluir documentación completa
"""

def detectar_drift_ks(datos_entrenamiento, datos_produccion, alpha=0.05):
    """
    Detecta data drift usando el test Kolmogorov-Smirnov.
    
    Args:
        datos_entrenamiento: array de datos del período de entrenamiento
        datos_produccion: array de datos del período actual
        alpha: nivel de significancia (default: 0.05)
    
    Returns:
        dict con estadístico KS, p-valor, severidad y si hay drift
    """
    from scipy import stats
    import numpy as np
    
    stat, p_value = stats.ks_2samp(datos_entrenamiento, datos_produccion)
    
    # Clasificar severidad
    if p_value < 0.01:
        severidad = 'CRÍTICA'
    elif p_value < 0.05:
        severidad = 'ALTA'
    elif p_value < 0.1:
        severidad = 'MEDIA'
    else:
        severidad = 'BAJA'
    
    return {
        'drift_detectado': p_value < alpha,
        'estadistico_ks': stat,
        'p_valor': p_value,
        'severidad': severidad
    }
```

---

## Prompt 3: Dashboard de Monitoreo

```
Diseña un dashboard en Python usando Streamlit o Dash que muestre en tiempo real:

1. Métricas de drift (PSI, KS) para las features principales
2. Gráfico de evolución temporal de la accuracy
3. Distribución de predicciones (histograma)
4. Tabla de alertas activas
5. Indicador de estado del modelo (verde/amarillo/rojo)

El dashboard debe actualizarse automáticamente cada 5 minutos y guardar
un log de todas las métricas calculadas.
```

---

## Prompt 4: Sistema de Alertas

```python
# Prompt para sistema de alertas automatizado

"""
Crea un sistema de alertas para monitoreo de modelos que:

1. Evalúe múltiples métricas (drift, accuracy, nulos)
2. Genere alertas con diferentes severidades
3. Envíe notificaciones por email (simulado)
4. Mantenga un historial de alertas
5. Escale alertas si no se atienden en X horas

Incluye un ejemplo de uso con datos sintéticos.
"""

class SistemaAlertas:
    def __init__(self, config):
        """
        config = {
            'email_from': 'ml-monitoring@empresa.com',
            'email_to': 'equipo-datos@empresa.com',
            'umbral_psi_critico': 0.2,
            'umbral_accuracy_minimo': 0.7,
            'horas_escalamiento': 24
        }
        """
        self.config = config
        self.historial = []
    
    def evaluar(self, metricas):
        """Evalúa métricas y genera alertas."""
        alertas = []
        
        # Alerta por drift crítico
        if metricas.get('psi', 0) > self.config['umbral_psi_critico']:
            alertas.append({
                'tipo': 'DRIFT_CRITICO',
                'severidad': 'CRÍTICA',
                'mensaje': f"PSI = {metricas['psi']:.3f}",
                'timestamp': datetime.now().isoformat(),
                'accion': 'Reentrenamiento inmediato'
            })
        
        # Alerta por caída de rendimiento
        if metricas.get('accuracy', 1) < self.config['umbral_accuracy_minimo']:
            alertas.append({
                'tipo': 'RENDIMIENTO_CRITICO',
                'severidad': 'CRÍTICA',
                'mensaje': f"Accuracy = {metricas['accuracy']:.3f}",
                'timestamp': datetime.now().isoformat(),
                'accion': 'Rollback necesario'
            })
        
        self.historial.extend(alertas)
        return alertas
```

---

## Prompt 5: Estrategia de Rollback

```
Explica paso a paso cómo implementar una estrategia de rollback para modelos
de machine learning en producción. Incluye:

1. Versionado de modelos (cómo guardar y recuperar versiones)
2. Criterios para activar rollback automático
3. Proceso manual de rollback
4. Verificación post-rollback
5. Comunicación al equipo y stakeholders

Proporciona un ejemplo concreto usando Python y scikit-learn.
```

---

## Prompt 6: Monitoreo de Sesgos

```python
# Prompt para monitoreo ético de sesgos

"""
Implementa un sistema de monitoreo de sesgos que:

1. Identifique características sensibles (género, raza, edad)
2. Calcule métricas de equidad por grupo:
   - Tasa de positivos
   - Disparate impact ratio
   - Equal opportunity difference
3. Detecte cuando una métrica supera umbrales éticos
4. Genere un reporte de auditoría
5. Proponga acciones correctivas

Incluye un ejemplo con datos sintéticos que tengan sesgo incorporado.
"""

def calcular_disparate_impact(y_pred, sensitive_feature):
    """
    Calcula el disparate impact ratio.
    
    Un valor < 0.8 indica sesgo potencial according a la guía EEOC.
    """
    import numpy as np
    
    grupos = np.unique(sensitive_feature)
    tasas = {}
    
    for grupo in grupos:
        mascara = sensitive_feature == grupo
        tasa = np.mean(y_pred[mascara])
        tasas[grupo] = tasa
    
    # Ratio entre grupo minoritario y mayoritario
    tasa_max = max(tasas.values())
    tasa_min = min(tasas.values())
    
    disparate_impact = tasa_min / tasa_max if tasa_max > 0 else 1
    
    return {
        'tasas_por_grupo': tasas,
        'disparate_impact': disparate_impact,
        'alerta_sesgo': disparate_impact < 0.8
    }
```

---

## Prompt 7: Caso de Estudio Real

```
Describe un caso de estudio real (o basado en realidad) donde un modelo de
machine learning falló por no monitorear data drift. Incluye:

1. Contexto del problema (qué modelo, qué datos)
2. Qué tipo de drift ocurrió
3. Cómo se detectó (o no se detectó)
4. Consecuencias para el negocio
5. Cómo se resolvió
6. Lecciones aprendidas

El caso debe ser realista y aplicable a industries como banca, salud o retail.
```

---

## Prompt 8: Checklist de Monitoreo

```
Crea un checklist completo para monitoreo de modelos en producción que incluya:

PRE-DEPLOYMENT:
- [ ] Features críticas identificadas
- [ ] Baseline de métricas establecido
- [ ] Umbrales de alerta configurados
- [ ] Responsables designados
- [ ] Plan de rollback documentado

POST-DEPLOYMENT:
- [ ] Monitoreo de data drift activo
- [ ] Validación de performance diaria
- [ ] Detección de sesgos semanal
- [ ] Alertas revisadas diariamente
- [ ] Historial de métricas guardado

MANTENIMIENTO:
- [ ] Reentrenamiento programado
- [ ] Auditorías de equidad trimestrales
- [ ] Actualización de umbrales
- [ ] Documentación de cambios
- [ ] Comunicación a stakeholders

El checklist debe ser ejecutable y incluir frecuencias específicas.
```

---

## Prompt 9: Métricas de Evaluación

```
Define las métricas más importantes para evaluar el monitoreo de modelos
y explica cómo interpretarlas:

1. PSI (Population Stability Index)
2. KS (Kolmogorov-Smirnov)
3. CSI (Characteristic Stability Index)
4. Accuracy degradation
5. Prediction distribution shift

Para cada métrica incluye:
- Fórmula o cálculo
- Rangos de interpretación
- Cuándo preocuparse
- Acción recomendada
```

---

## Prompt 10: Integración con Herramientas

```
Explica cómo integrar el monitoreo de drift con herramientas modernas:

1. Evidently AI: Configuración básica y reportes
2. Great Expectations: Validación de datos
3. MLflow: Tracking de métricas
4. Prometheus + Grafana: Métricas en tiempo real
5. Airflow: Orquestación de monitoreo

Para cada herramienta, proporciona:
- Caso de uso ideal
- Ejemplo de configuración
- Ventajas y desventajas
- Integración con el pipeline existente
```

---

## Referencias para Profundizar

1. **Widmer, G., & Kubat, M. (1996)** - "Learning in the presence of concept drift and hidden contexts"
   - Paper fundamental sobre concept drift

2. **Lu, J., et al. (2018)** - "Learning under Concept Drift: A Review"
   - Revisión completa de técnicas de detección

3. **Reis, M., et al. (2022)** - "Monitoring ML Models in Production"
   - Guía práctica para monitoreo

4. **Diamond, S. (2023)** - "Evidently AI: Open Source ML Monitoring"
   - Documentación de herramienta de código abierto

---

## Tips para Autores

1. **Metáfora del cambio climático**: Úsala para explicar por qué los modelos se degradan
2. **Visualizaciones**: Incluye gráficos de distribuciones antes/después del drift
3. **Código ejecutable**: Todos los ejemplos deben funcionar sin dependencias externas complejas
4. **Casos reales**: Usa ejemplos de industrias que el lector reconozca
5. **Checklists**: Proporciona listas de verificación que el lector pueda usar inmediatamente
