# Prompts para Capítulo 13: Optimización de Operaciones y Logística

> Prompts específicos para generar, expandir o mejorar contenido del Capítulo 13.
> Cada prompt incluye contexto, instrucciones y restricciones.

---

## Prompt 13.1: Generar Análisis de Retrasos con IA

**Objetivo:** Crear un prompt completo para que una IA analice causas de retrasos logísticos.

**Prompt:**
```
Eres un consultor de logística senior. Analiza los siguientes datos de
entregas de última milla y genera un reporte diagnóstico:

DATOS (25,000 entregas, 5 repartidores):
- Partner-A: 5,000 envíos | 42% retrasos | Tiempo prom: 4.8h | Costo: $28.50
- Partner-B: 5,000 envíos | 40% retrasos | Tiempo prom: 4.6h | Costo: $27.20
- Partner-C: 5,000 envíos | 37% retrasos | Tiempo prom: 4.5h | Costo: $26.80
- Partner-D: 5,000 envíos | 36% retrasos | Tiempo prom: 4.4h | Costo: $26.50
- Partner-E: 5,000 envíos | 35% retrasos | Tiempo prom: 4.3h | Costo: $25.90

CONDICIONES CLIMÁTICAS:
- Soleado: 33% envíos | 34% retrasos
- Lluvioso: 34% envíos | 42% retrasos
- Nublado: 33% envíos | 38% retrasos

CONTEXTO:
- Empresa de última milla en 4 regiones
- Tipos de paquete: Electrónica, Alimentos, Documentos, Ropa
- Vehículos: Moto, Urbano, Bicicleta, Camión
- Modalidades: Express, Estándar

GENERAR:
1. Diagnóstico: ¿Por qué Partner-A tiene 7% más retrasos que Partner-E?
2. Análisis de clima: ¿Cómo afecta la lluvia a los retrasos?
3. 5 hipótesis sobre las causas raíz de los retrasos
4. 3 estrategias específicas para reducir retrasos un 15%
5. Métricas de seguimiento para cada estrategia
6. Riesgos de cada recomendación
```

**Restricciones:**
- Tono directo, ejecutivo, sin jerga técnica innecesaria
- Incluir números concretos en cada recomendación
- Considerar el impacto humano en los repartidores
- Mencionar al menos 2 riesgos por estrategia

---

## Prompt 13.2: Generar Análisis de Calidad de Datos

**Objetivo:** Crear un prompt para que una IA identifique problemas de calidad en datos logísticos.

**Prompt:**
```
Analiza la calidad de datos del siguiente dataset de logística y responde:

ESTRUCTURA DEL DATASET:
- 25,000 registros de entregas
- 15 columnas: delivery_id, delivery_partner, package_type, vehicle_type,
  delivery_mode, region, weather_condition, distance_km, package_weight_kg,
  delivery_time_hours, expected_time_hours, delayed, delivery_status,
  delivery_rating, delivery_cost

PROBLEMAS DETECTADOS:
- 120 registros con tiempos negativos
- 85 registros con tiempos >20 horas
- 45 registros con distancia >50km en <1 hora
- 200 registros donde delayed='Yes' pero delivery_status='Completada'
- 150 registros donde delivery_time_hours <= expected_time_hours pero delayed='Yes'

PREGUNTAS:
1. ¿Qué tipo de error es más común y por qué ocurre?
2. ¿Qué impacto tienen estos errores en un modelo predictivo?
3. ¿Cómo limpiar los datos sin perder información valiosa?
4. ¿Qué métricas de calidad deberíamos monitorear continuamente?
5. ¿Cómo comunicar estos problemas a stakeholders no técnicos?

CONTEXTO: Empresa de logística de última milla con sistemas de tracking GPS.
```

**Restricciones:**
- No asumir causalidad sin evidencia
- Incluir perspectiva de integridad de datos
- Proponer métodos específicos de limpieza
- Conectar con impacto en decisiones de negocio

---

## Prompt 13.3: Generar Prompts para Optimización de Rutas

**Objetivo:** Crear prompts específicos para que una IA recomiende optimización de rutas.

**Prompt:**
```
Diseña 3 prompts diferentes para optimización de rutas logísticas:

PROMPT 1 - Para análisis de eficiencia regional:
Contexto: 4 regiones con diferentes tasas de retraso
Objetivo: Identificar regiones con mayor potencial de mejora
Restricción: No puede reducir servicio en ninguna región

PROMPT 2 - Para asignación de repartidores:
Contexto: 5 repartidores con diferentes niveles de rendimiento
Objetivo: Balancear carga de trabajo sin sobrecargar a nadie
Restricción: No puede reasignar más del 20% de entregas

PROMPT 3 - Para optimización considerando clima:
Contexto: 3 condiciones climáticas con diferentes impactos
Objetivo: Adaptar rutas a pronóstico del clima
Restricción: No puede cancelar entregas por clima

Para cada prompt incluir:
1. El prompt completo y listo para usar
2. Métricas de éxito esperadas
3. Riesgos específicos
4. Cómo validar los resultados
5. Consideraciones éticas
```

**Restricciones:**
- Cada prompt debe ser autocontenido
- Incluir datos concretos, no generalidades
- Mencionar explícitamente los trade-offs
- Incluir consideraciones de bienestar laboral

---

## Prompt 13.4: Generar Recuadro "¿Qué Hizo Mal el Modelo?"

**Objetivo:** Crear un recuadro diagnóstico completo sobre fracasos de IA en logística.

**Prompt:**
```
Crea un recuadro completo "¿Qué Hizo Mal el Modelo y por Qué?" para el
Capítulo 13 de Optimización de Operaciones y Logística. Incluye:

1. Escenario: Una empresa confió ciegamente en las recomendaciones de IA
   para optimizar su operación de última milla.

2. Lo que la IA recomendó:
   - "Reasigna entregas del Partner-A al Partner-E"
   - "Reduce un 20% el tiempo estimado en días lluviosos"
   - "Elimina las rutas con calificación < 3.0"

3. Lo que salió mal:
   - Partner-E se sobrecargó y su rendimiento cayó un 30%
   - Los repartidores tomaron atajos peligrosos para cumplir nuevos tiempos
   - Las rutas "eliminadas" eran las más difíciles pero necesarias
   - La satisfacción del cliente general cayó un 15%

4. Consecuencias reales:
   - 3 repartidores renunciaron en un mes
   - 2 accidentes de tráfico por exceso de velocidad
   - Pérdida de 50 clientes empresariales
   - Demanda laboral por condiciones inseguras

5. Lecciones:
   - La IA optimiza para métricas, no para personas
   - Los datos históricos no capturan el contexto humano
   - La optimización extrema crea sistemas frágiles

6. Preguntas para el lector:
   - ¿Cómo habrías validado la recomendación de la IA?
   - ¿Qué datos adicionales necesitarías?
   - ¿Cómo implementarías un piloto antes del cambio completo?
```

**Restricciones:**
- Tono directo, sin condescendencia
- Incluir números concretos en cada consecuencia
- La moraleja debe ser accionable, no moralina
- Conectar con ética laboral

---

## Prompt 13.5: Generar Ejercicios Prácticos

**Objetivo:** Crear 5 ejercicios progresivos para practicar análisis logístico.

**Prompt:**
```
Diseña 5 ejercicios progresivos para el Capítulo 13 de Optimización Logística:

**Ejercicio 1 (Básico):** Diagnóstico de Calidad
- Cargar el dataset y detectar anomalías
- Identificar tipos de errores más comunes
- Habilidades: isnull, describe, value_counts

**Ejercicio 2 (Intermedio):** Análisis de Retrasos
- Calcular tasas de retraso por repartidor, clima, vehículo
- Identificar factores con mayor correlación
- Habilidades: groupby, crosstab, correlation

**Ejercicio 3 (Intermedio):** Predicción
- Entrenar modelo de Random Forest
- Evaluar métricas e importancia de features
- Habilidades: sklearn, classification_report

**Ejercicio 4 (Avanzado):** Optimización
- Simular mejora de rutas
- Calcular ahorros potenciales
- Habilidades: numpy, simulación, estimación financiera

**Ejercicio 5 (Avanzado):** Ética
- Analizar si hay patrones de asignación sesgada
- Proponer framework ético para optimización
- Habilidades: razonamiento ético, análisis de sesgos

Para cada ejercicio incluir:
1. Enunciado claro
2. Datos de entrada
3. Salida esperada
4. Pista (sin solución completa)
5. Nivel de dificultad (1-5)
6. Preguntas de reflexión ética
```

**Restricciones:**
- Ejercicios resolverse con pandas estándar
- Incluir casos edge en cada ejercicio
- Conectar con la ética laboral
- Cada ejercicio debe ser independiente

---

## Prompt 13.6: Generar Contenido Ético Adicional

**Objetivo:** Crear recuadros éticos para cada sección del capítulo.

**Prompt:**
```
Genera 5 recuadros éticos para el Capítulo 13, uno por cada tema:

1. **Datos de Rendimiento:** ¿Qué capturan y qué ignoran?
   - Solo miden velocidad y costo
   - Ignoran fatiga, estrés, condiciones laborales
   - Ejemplo: Partner-A parece "peor" pero maneja las rutas más difíciles

2. **Optimización de Rutas:** ¿Eficiencia o explotación?
   - Optimizar puede significar más carga para los "mejores"
   - Ejemplo: Reasignar entregas sin considerar capacidad
   - Consecuencia: burnout, rotación, accidentes

3. **Predicción de Retrasos:** ¿Predecir o prejuzgar?
   - Modelos pueden crear profecías autocumplidas
   - Ejemplo: Si predices que Partner-A se retrasa, le das menos trabajo, y se retrasa más
   - Sesgo de confirmación algorítmico

4. **IA Generativa:** ¿Quién decide y quién ejecuta?
   - La IA recomienda, los humanos ejecutan
   - Ejemplo: IA recomienda reducir tiempos, repartidores toman atajos
   - Responsabilidad difusa

5. **Transparencia:** ¿Los repartidores saben cómo se evalúan?
   - Sistema opaco genera desconfianza
   - Ejemplo: No saber por qué te asignan ciertas rutas
   - Derecho a explicación

Para cada recuadro incluir:
- Pregunta provocadora
- Ejemplo concreto con números
- Consecuencia real
- Pregunta para reflexión
- Referencia a marco regulatorio o ético
```

**Restricciones:**
- Tono directo, sin moralina
- Ejemplos numéricos concretos
- Conectar con impacto humano real
- Incluir perspectiva de trabajadores

---

## Prompt 13.7: Generar Metáforas para Principiantes

**Objetivo:** Crear analogías que faciliten la comprensión de conceptos de logística.

**Prompt:**
```
Genera 6 metáforas para explicar conceptos de optimización logística a principiantes:

1. **Logística** → Orquesta sin director donde cada músico toca diferente
2. **Datos Sucios** → Lente empañado: ves las letras pero confundes la "m" con la "n"
3. **Optimización de Rutas** → Jenga: cada pieza que mueves puede debilitar otra
4. **Predicción de Retrasos** → Meteorología: puedes dar probabilidades, nunca certezas
5. **Repartidores** → Músculos del sistema: si los sobrecargas, se lesionan
6. **Eficiencia** → Equilibrio: no es hacer más rápido, es hacer sostenible

Para cada metáfora incluir:
- Analogía completa (3-4 oraciones)
- Conexión directa con el concepto técnico
- Ejemplo visual o numérico
- Por qué funciona para principiantes
- Limitación de la metáfora (qué no captura)
```

**Restricciones:**
- Metáforas basadas en experiencias cotidianas
- Evitar jerga técnica en la explicación
- Incluir limitaciones de cada analogía
- Conectar con ejemplos del capítulo

---

## Prompt 13.8: Generar Código para Análisis Automático

**Objetivo:** Crear funciones para análisis automatizado de operaciones.

**Prompt:**
```
Crea 5 funciones de análisis automatizado para el Capítulo 13:

1. **diagnosticar_calidad_datos(df)**
   - Detecta anomalías, nulos, duplicados
   - Retorna reporte con severidad
   - Incluye recomendaciones de limpieza

2. **analizar_retrasos(df, agrupar_por)**
   - Calcula tasas de retraso por categoría
   - Identifica factores de mayor impacto
   - Retorna ranking con métricas

3. **predecir_retrasos(df, features, target)**
   - Entrena modelo de clasificación
   - Evalúa métricas de rendimiento
   - Retorna modelo y reporte

4. **simular_optimizacion(df, n_rutas)**
   - Simula diferencia entre rutas aleatorias y optimizadas
   - Estima ahorros en tiempo y costo
   - Retorna proyección anual

5. **evaluar_impacto_etico(df, columna_repartidor)**
   - Analiza distribución de carga de trabajo
   - Detecta posibles sesgos de asignación
   - Retorna reporte ético con alertas

Para cada función incluir:
- Docstring completo
- Ejemplo de uso
- Casos edge manejados
- Manejo de errores
```

**Restricciones:**
- Código sin dependencias externas (solo pandas/numpy/sklearn)
- Compatible con Python 3.8+
- Incluir type hints
- Manejo de errores incluido

---

## Prompt 13.9: Generar Contenido para el Notebook

**Objetivo:** Crear celdas adicionales para el Jupyter notebook.

**Prompt:**
```
Diseña 3 celdas adicionales para el notebook del Capítulo 13:

**Celda Extra 1: Análisis de Eficiencia por Región**
- Cruza región × tipo de paquete × modalidad
- Identifica combinaciones ganadoras y perdedoras
- Genera tabla de recomendación
- Incluye visualización de heat map

**Celda Extra 2: Simulador de Asignación**
- Interfaz simple para ajustar % de entrega por repartidor
- Calcula impacto estimado en retrasos y costos
- Muestra alertas de riesgo laboral
- Genera reporte de sensibilidad

**Celda Extra 3: Generador de Reportes Operativos**
- Toma los datos y genera un reporte en texto plano
- Incluye resumen ejecutivo, métricas clave, recomendaciones
- Formato listo para copiar y pegar en email
- Incluye disclaimer ético

Para cada celda incluir:
1. Markdown explicativo
2. Código funcional
3. Salida esperada
4. Preguntas para reflexión
```

**Restricciones:**
- Código ejecutable sin modificaciones
- Compatibilidad con Google Colab
- Incluir verificación de entorno
- Comentarios en español

---

## Prompt 13.10: Generar Referencias y Citas

**Objetivo:** Crear sección completa de referencias académicas.

**Prompt:**
```
Genera una sección de referencias para el Capítulo 13 que incluya:

1. **Referencias Principales (obligatorias):**
   - Simchi-Levi, D., Kaminsky, P., & Simchi-Levi, E. (2008). Designing and Managing the Supply Chain. McGraw-Hill.
   - Bozorgi, M., et al. (2016). A New Model for Multi-Temperature Logistics. Transportation Research Part E.
   - Russell, R. S., & Taylor, B. W. (2018). Operations and Supply Chain Management. Wiley.

2. **Referencias Complementarias:**
   - Artículos sobre optimización de rutas
   - Papers sobre ética en IA para operaciones
   - Estudios de caso de logística inteligente

3. **Formato APA 7ª edición**

4. **Para cada referencia incluir:**
   - Cita completa
   - Resumen de 1 línea (qué aporta)
   - Dónde se usa en el capítulo
   - Enlace DOI o URL si existe

5. **Recuadro "Lecturas Adicionales"**
   - 5 artículos para profundizar
   - Nivel de dificultad de cada uno
   - Tiempo estimado de lectura
```

**Restricciones:**
- Solo referencias verificadas
- Incluir DOI cuando exista
- Formato consistente APA 7
- Referencias de los últimos 10 años cuando sea posible
