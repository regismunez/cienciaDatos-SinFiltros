# Prompts para Capítulo 12: Análisis de Marketing con IA Generativa

> Prompts específicos para generar, expandir o mejorar contenido del Capítulo 12.
> Cada prompt incluye contexto, instrucciones y restricciones.

---

## Prompt 12.1: Generar Análisis de Campañas con IA

**Objetivo:** Crear un prompt completo para que una IA genere un análisis de campañas de marketing.

**Prompt:**
```
Eres un analista de marketing digital senior. Analiza los siguientes datos
de campañas de una empresa B2B SaaS y genera un reporte ejecutivo:

DATOS (24 meses, 5 canales):
- SEO: Gasto $68,000 | Revenue $20,500 | ROAS 0.30 | CPL $641
- Paid Search: Gasto $113,000 | Revenue $12,800 | ROAS 0.11 | CPL $2,166
- Social: Gasto $76,000 | Revenue $4,300 | ROAS 0.06 | CPL $2,746
- Email: Gasto $40,000 | Revenue $320,000 | ROAS 8.03 | CPL $26
- Display: Gasto $106,000 | Revenue $3,200 | ROAS 0.03 | CPL $4,111

CONTEXTO:
- Empresa B2B SaaS con ciclo de venta de 3-6 meses
- Mercado competitivo con 5 competidores directos
- Presupuesto total anual: $403,000
- Equipo de marketing de 4 personas

GENERA:
1. Resumen ejecutivo (3 oraciones máximo)
2. Diagnóstico por canal (fortalezas y debilidades)
3. 5 hipótesis sobre el bajo rendimiento de Display
4. 3 estrategias para mejorar ROAS sin aumentar presupuesto
5. Riesgos de cada estrategia
6. Métricas de seguimiento recomendadas
```

**Restricciones:**
- Tono directo, ejecutivo, sin jerga técnica innecesaria
- Incluir números concretos en cada recomendación
- Considerar la estacionalidad en las recomendaciones
- Mencionar al menos 2 riesgos por estrategia

---

## Prompt 12.2: Generar Análisis de Sesgo Geográfico

**Objetivo:** Crear un prompt para que una IA identifique sesgos en datos de marketing por ubicación.

**Prompt:**
```
Analiza la distribución geográfica de la inversión de marketing y responde:

DATOS POR REGIÓN:
- Norte: 30% inversión | ROAS promedio 2.8 | CPL $450
- Sur: 25% inversión | ROAS promedio 3.1 | CPL $380
- Centro: 25% inversión | ROAS promedio 2.9 | CPL $420
- Occidente: 20% inversión | ROAS promedio 3.5 | CPL $310

PREGUNTAS:
1. ¿La distribución de inversión es justa o está sesgada?
2. ¿Qué factores podrían explicar las diferencias de ROAS?
3. ¿Incluir código postal en el targeting crearía problemas éticos?
4. ¿Cómo saber si el sesgo es "natural" o "inducido por el algoritmo"?
5. ¿Qué métricas de equidad deberíamos monitorear?

CONTEXTO: Empresa que vende software empresarial a PyMEs en México.
```

**Restricciones:**
- No asumir causalidad sin evidencia
- Incluir perspectiva de fairness algorítmico
- Mencionar marcos regulatorios (LFPDPPP en México, GDPR en Europa)
- Proponer al menos 3 métricas de equidad

---

## Prompt 12.3: Generar Prompts para Optimización de Presupuesto

**Objetivo:** Crear prompts específicos para que una IA recomiende reasignación de presupuesto.

**Prompt:**
```
Diseña 3 prompts diferentes para optimización de presupuesto de marketing:

PROMPT 1 - Para análisis de canales:
Contexto: 5 canales, ROAS variables, CPL entre $26 y $4,111
Objetivo: Maximizar leads manteniendo ROI positivo
Restricción: Presupuesto fijo de $403,000/año

PROMPT 2 - Para análisis estacional:
Contexto: 24 meses de datos con picos en Navidad y verano
Objetivo: Identificar cuándo invertir más y cuándo reducir
Restricción: No puede reducir inversión en ningún canal a menos del 50% del promedio

PROMPT 3 - Para análisis de segmentos:
Contexto: 4 segmentos demográficos con rendimiento diferente
Objetivo: Balancear eficiencia y diversidad de audiencia
Restricción: No puede excluir ningún segmento completamente

Para cada prompt incluir:
1. El prompt completo y listo para usar
2. Métricas de éxito esperadas
3. Riesgos específicos
4. Cómo validar los resultados
```

**Restricciones:**
- Cada prompt debe ser autocontenido (la IA no necesita contexto adicional)
- Incluir datos concretos, no generalidades
- Mencionar explícitamente los trade-offs
- Incluir instrucciones de verificación

---

## Prompt 12.4: Generar Recuadro "¿Qué Hizo Mal el Modelo?"

**Objetivo:** Crear un recuadro diagnóstico completo sobre fracasos de IA en marketing.

**Prompt:**
```
Crea un recuadro completo "¿Qué Hizo Mal el Modelo y por Qué?" para el
Capítulo 12 de Marketing con IA Generativa. Incluye:

1. Escenario: Una empresa confió ciegamente en las recomendaciones de IA
   para reasignar su presupuesto de marketing.

2. Lo que la IA recomendó:
   - "Invierte 40% más en Email, reduce 30% en Display"
   - "Cierra el canal de Social, no genera revenue atribuible"
   - "Aumenta inversión en la Región Norte por mayor ROAS"

3. Lo que salió mal:
   - Email saturó su base de leads (diminishing returns después de 3 meses)
   - Display sostenía brand awareness; sin él, las búsquedas orgánicas cayeron 25%
   - La Región Norte tenía clientes de alto valor, pero el mercado estaba saturado
   - Los leads de Email eran de bajo valor (muchos free trial, pocos enterprise)

4. Consecuencias reales:
   - Pérdida de $120,000 en 6 meses
   - Caída de 35% en pipeline de ventas
   - Equipo de marketing desmoralizado

5. Lecciones:
   - La IA optimiza para métricas históricas, no para el futuro
   - La canibalización entre canales es real
   - Los datos de atribución son incompletos

6. Preguntas para el lector:
   - ¿Cómo habrías validado la recomendación de la IA?
   - ¿Qué datos adicionales necesitarías?
   - ¿Cómo implementarías un piloto antes del cambio completo?
```

**Restricciones:**
- Tono directo, sin condescendencia
- Incluir números concretos en cada consecuencia
- La moraleja debe ser accionable, no moralina
- Conectar con la ética de datos

---

## Prompt 12.5: Generar Ejercicios Prácticos

**Objetivo:** Crear 5 ejercicios progresivos para practicar análisis de marketing con IA.

**Prompt:**
```
Diseña 5 ejercicios progresivos para el Capítulo 12 de Marketing con IA:

**Ejercicio 1 (Básico):** Análisis Exploratorio
- Cargar el dataset y calcular ROAS y CPL por canal
- Identificar el canal más eficiente y el menos eficiente
- Habilidades: groupby, agg, sort_values

**Ejercicio 2 (Intermedio):** Prompt Engineering
- Escribir 3 prompts diferentes para analizar el dataset
- Evaluar cuál prompt genera mejor respuesta
- Habilidades: Redacción de prompts, contexto, especificidad

**Ejercicio 3 (Intermedio):** Detección de Sesgo
- Analizar distribución geográfica de inversión
- Identificar posibles sesgos en la segmentación
- Proponer métricas de equidad
- Habilidades: Análisis de distribución, razonamiento ético

**Ejercicio 4 (Avanzado):** Verificación de IA
- Tomar una recomendación genérica de IA
- Aplicar las 5 reglas de verificación
- Generar un reporte de confiabilidad
- Habilidades: Pensamiento crítico, verificación de datos

**Ejercicio 5 (Avanzado):** Reasignación de Presupuesto
- Diseñar un plan de reasignación de presupuesto
- Calcular el impacto estimado en leads e ingresos
- Proponer un piloto de validación
- Habilidades: Modelado financiero, planificación

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
- Conectar con la ética de datos
- Cada ejercicio debe ser independiente

---

## Prompt 12.6: Generar Contenido Ético Adicional

**Objetivo:** Crear recuadros éticos para cada sección del capítulo.

**Prompt:**
```
Genera 5 recuadros éticos para el Capítulo 12, uno por cada tema:

1. **Datos Geográficos:** ¿Qué pasa si incluimos código postal?
   - Proxy para raza, etnia, nivel socioeconómico
   - Ejemplo: Targeting por código postal excluye comunidades
   - Marco regulatorio: LFPDPPP, GDPR

2. **Segmentación Demográfica:** ¿Quién decidimos incluir y excluir?
   - Sesgo en targeting de audiencia
   - Ejemplo: Priorizar "Profesionales 41-55" excluye jóvenes
   - Impacto en diversidad de mercado

3. **Atribución de Revenue:** ¿Quién recibe el crédito?
   - Modelo de atribución sesgado
   - Ejemplo: Email recibe crédito de Display
   - Justicia en distribución de presupuesto

4. **IA Generativa:** ¿Confiamos ciegamente en las recomendaciones?
   - Sesgo algorítmico amplificado
   - Ejemplo: IA recomienda excluir mercados emergentes
   - Necesidad de verificación humana

5. **Transparencia:** ¿Podemos explicar nuestras decisiones?
   - Caja negra en marketing
   - Ejemplo: No saber por qué la IA priorizó un canal
   - Derecho a explicación

Para cada recuadro incluir:
- Pregunta provocadora
- Ejemplo concreto con números
- Consecuencia real
- Pregunta para reflexión
- Referencia a marco regulatorio
```

**Restricciones:**
- Tono directo, sin moralina
- Ejemplos numéricos concretos
- Conectar con impacto humano real
- Incluir al menos 1 referencia legal por recuadro

---

## Prompt 12.7: Generar Metáforas para Principiantes

**Objetivo:** Crear analogías que faciliten la comprensión de conceptos de marketing analytics.

**Prompt:**
```
Genera 6 metáforas para explicar conceptos de marketing con IA a principiantes:

1. **ROAS** → Cuánto ganas por cada dólar invertido
2. **CPL** → Cuánto te cuesta comprar un cliente potencial
3. **Atribución** → Quién recibe el crédito cuando varios amigos te presentan a tu pareja
4. **Sesgo Geográfico** → Si solo invitas a fiestas a tus vecinos, nunca conocerás a nadie de otro barrio
5. **IA Generativa** → Un analista junior brillante que nunca pregunta si los datos son correctos
6. **Reasignación de Presupuesto** → Mover piezas de ajedrez sin entender el juego completo

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

## Prompt 12.8: Generar Código para Análisis Automático

**Objetivo:** Crear funciones para análisis automatizado de campañas.

**Prompt:**
```
Crea 5 funciones de análisis automatizado para el Capítulo 12:

1. **analizar_rendimiento_canal(df, canal)**
   - Calcula ROAS, CPL, tendencia, estacionalidad
   - Retorna diccionario con métricas y diagnóstico
   - Incluye comparación con promedio general

2. **detectar_sesgo_geografico(df, columna_region)**
   - Analiza distribución de inversión por región
   - Calcula métricas de equidad
   - Detecta posibles sesgos
   - Retorna reporte con nivel de severidad

3. **generar_prompt_analisis(datos_resumen, contexto)**
   - Genera prompts específicos para IA
   - Incluye datos concretos y contexto
   - Formatea para máxima efectividad
   - Retorna string listo para usar

4. **evaluar_respuesta_ia(respuesta, datos_reales)**
   - Compara respuesta de IA con datos reales
   - Detecta inconsistencias
   - Calcula puntuación de confiabilidad
   - Retorna reporte de verificación

5. **simular_reasignacion(df, cambios)**
   - Simula impacto de reasignar presupuesto
   - Estima cambio en leads e ingresos
   - Incluye intervalos de confianza
   - Retorna tabla comparativa

Para cada función incluir:
- Docstring completo
- Ejemplo de uso
- Casos edge manejados
- Manejo de errores
```

**Restricciones:**
- Código sin dependencias externas (solo pandas/numpy)
- Compatible con Python 3.8+
- Incluir type hints
- Manejo de errores incluido

---

## Prompt 12.9: Generar Contenido para el Notebook

**Objetivo:** Crear celdas adicionales para el Jupyter notebook.

**Prompt:**
```
Diseña 3 celdas adicionales para el notebook del Capítulo 12:

**Celda Extra 1: Análisis de ROI por Segmento**
- Cruza canal × segmento de audiencia
- Identifica combinaciones ganadoras y perdedoras
- Genera tabla de recomendación
- Incluye visualización de heat map

**Celda Extra 2: Simulador de Presupuesto**
- Interfaz simple para ajustar % de inversión por canal
- Calcula impacto estimado en leads e ingresos
- Muestra alertas de riesgo
- Genera reporte de sensibilidad

**Celda Extra 3: Generador de Reportes Ejecutivos**
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

## Prompt 12.10: Generar Referencias y Citas

**Objetivo:** Crear sección completa de referencias académicas.

**Prompt:**
```
Genera una sección de referencias para el Capítulo 12 que incluya:

1. **Referencias Principales (obligatorias):**
   - Kumar, V., & Reinartz, W. (2018). Customer Relationship Management. Springer.
   - Provost, F., & Fawcett, T. (2013). Data Science for Business. O'Reilly.
   - Turtle, T. (2023). AI-Powered Marketing Analytics. Harvard Business Review.

2. **Referencias Complementarias:**
   - Artículos sobre atribución de marketing
   - Papers sobre sesgo algorítmico en marketing
   - Estudios de caso de IA en marketing

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
- Referencias de los últimos 5 años cuando sea posible
