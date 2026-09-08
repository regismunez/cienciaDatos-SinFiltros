# Prompts para el Capítulo 11: La Latencia Mata al Modelo

## 📋 Descripción del Capítulo

**Título:** "La Latencia Mata al Modelo (Optimización para Producción)"  
**Objetivo:** Enseñar técnicas de optimización de modelos para producción, incluyendo benchmarking, cuantización, pruning y ONNX.

---

## 🎯 Prompts de Aprendizaje

### Nivel Básico

#### Prompt 1: Entendiendo la latencia
```
Explica la diferencia entre latencia y throughput en el contexto de modelos de ML.
¿Por qué un modelo puede tener bajo throughput pero alta latencia? 
Incluye ejemplos prácticos de aplicaciones donde la latencia es crítica.
```

#### Prompt 2: ¿Qué es la cuantización?
```
Define la cuantización de modelos de ML como si le explicaras a alguien 
que sabe programar pero no tiene experiencia en optimización de modelos.
Usa la metáfora de "comprimir una foto sin perder calidad visible".
```

#### Prompt 3: Pruning para principiantes
```
Explica el pruning (poda) de redes neuronales usando la analogía 
de podar un árbol para que crezca mejor. ¿Cuándo es útil y cuándo 
puede ser perjudicial?
```

---

### Nivel Intermedio

#### Prompt 4: Benchmarking completo
```
Diseña un protocolo de benchmarking para un modelo de clasificación 
de imágenes que será desplegado en producción. Incluye:
- Métricas a medir (P95, P99, throughput)
- Condiciones del entorno
- Número mínimo de iteraciones
- Calentamiento del modelo
Proporciona código Python para implementarlo.
```

#### Prompt 5: Cuantización INT8 paso a paso
```
Implementa la cuantización INT8 de un modelo PyTorch preentrenado.
Explica cada paso:
1. Preparación del modelo
2. Calibración (si es necesario)
3. Conversión
4. Validación de resultados
Incluye código completo y explicación de trade-offs.
```

#### Prompt 6: ONNX en producción
```
Crea una guía completa para exportar un modelo PyTorch a ONNX 
y servirlo con ONNX Runtime en producción. Incluye:
- Exportación con batch dinámico
- Validación del modelo exportado
- Benchmark comparativo
- Integración con FastAPI
```

---

### Nivel Avanzado

#### Prompt 7: Pipeline de optimización completo
```
Diseña un pipeline automatizado de optimización que incluya:
1. Benchmark del modelo base
2. Cuantización (INT8, FP16)
3. Pruning (estructurado y no estructurado)
4. Exportación ONNX
5. Comparación de rendimiento
6. Validación de precisión
El pipeline debe ser reproducible y documentado.
```

#### Prompt 8: Optimización ética
```
Desarrolla un framework de decisión ética para optimización de modelos.
El framework debe responder:
- ¿Cuándo NO es ético optimizar?
- ¿Cómo afecta la optimización a diferentes grupos demográficos?
- ¿Qué transparencia se debe proporcionar a los usuarios?
- ¿Cómo se平衡a velocidad vs precisión en casos críticos?
```

#### Prompt 9: Deploy con FastAPI
```
Crea un servicio de inferencia completo usando FastAPI que incluya:
- Carga de modelo ONNX al inicio
- Endpoints para predicción y health check
- Métricas de latencia en tiempo real
- Rate limiting
- Manejo de errores
- Documentación automática con OpenAPI
```

---

## 🔧 Prompts de Código

### Prompt C1: Benchmarking
```python
# Crea una función de benchmarking que mida:
# - Tiempo promedio
# - Percentiles P95 y P99
# - Throughput
# - Memoria utilizada
# La función debe:
# 1. Calentar el modelo
# 2. Ejecutar múltiples iteraciones
# 3. Retornar un diccionario con métricas
```

### Prompt C2: Cuantización dinámica
```python
# Implementa cuantización dinámica INT8 para un modelo PyTorch
# La función debe:
# 1. Aceptar un modelo y un tipo de destino
# 2. Cuantizar solo las capas especificadas
# 3. Retornar el modelo cuantizado
# 4. Incluir verificación de reducción de tamaño
```

### Prompt C3: Pruning estructurado
```python
# Implementa pruning estructurado que elimine neuronas completas
# La función debe:
# 1. Aceptar un modelo y porcentaje de poda
# 2. Usar norma L2 para identificar neuronas a eliminar
# 3. Mantener la arquitectura funcional
# 4. Retornar modelo y estadísticas de sparsity
```

### Prompt C4: Exportación ONNX
```python
# Crea una función para exportar modelos PyTorch a ONNX
# La función debe:
# 1. Soportar batch dinámico
# 2. Validar el modelo exportado
# 3. Incluir opset version configurable
# 4. Generar reporte de exportación
```

### Prompt C5: Servicio FastAPI
```python
# Diseña un servicio FastAPI para inferencia de modelos ONNX
# El servicio debe:
# 1. Cargar modelo al inicio
# 2. Tener endpoints de predicción y health check
# 3. Incluir métricas de latencia
# 4. Manejar errores correctamente
# 5. Documentarse automáticamente
```

---

## 📊 Prompts de Análisis

### Prompt A1: Comparación de técnicas
```
Compara las tres técnicas principales de optimización:
- Cuantización
- Pruning
- ONNX

Para cada una, analiza:
1. ¿Cuándo usarla?
2. ¿Qué trade-offs implica?
3. ¿Qué reducción de tamaño/tiempo se puede esperar?
4. ¿Qué casos de uso son ideales?
```

### Prompt A2: Análisis de benchmarks
```
Analiza el archivo datos_benchmark_modelos.csv y responde:
1. ¿Qué framework tiene mejor relación tamaño/precisión?
2. ¿Cuánto se puede acelerar un modeloBERT con optimización?
3. ¿Qué modelos son candidatos para edge devices?
4. ¿Qué modelo tiene mejor throughput?
```

### Prompt A3: Caso de estudio
```
Diseña un caso de estudio completo para optimizar un modelo de
detección de fraude que debe:
- Procesar 10,000 transacciones por segundo
- Mantener precisión > 95%
- Ejecutarse en hardware con 8GB de RAM
- Responder en < 50ms

Incluye justificación de cada decisión de optimización.
```

---

## 🎓 Prompts de Enseñanza

### Prompt E1: Metáforas efectivas
```
Crea analogías para explicar conceptos de optimización:
- Latencia → velocidad de respuesta de un mesonero
- Quantización → comprimir una foto
- ONNX → adaptador universal de cargadores
- Pruning → podar un árbol
- Throughput → mesas atendidas por hora
```

### Prompt E2: Ejercicios prácticos
```
Diseña 3 ejercicios progresivos para practicar optimización:
1. Básico: Cuantizar un modelo simple y medir diferencias
2. Intermedio: Crear un pipeline completo de optimización
3. Avanzado: Implementar un servicio de producción con métricas
Incluye código starter y soluciones esperadas.
```

### Prompt E3: Errores comunes
```
Lista los 10 errores más comunes al optimizar modelos para producción:
1. No hacer benchmark antes de optimizar
2. Optimizar demasiado (pérdida de precisión)
3. No considerar el hardware target
4. Olvidar validar después de optimizar
5. No documentar cambios
6. Usar técnicas incompatibles
7. No medir en condiciones reales
8. Ignorar el impacto ético
9. No tener plan de rollback
10. No transparentar a usuarios
```

---

## 🔬 Prompts de Investigación

### Prompt I1: Estado del arte
```
Investiga las técnicas más recientes de optimización de modelos (2023-2024):
- Quantización aware training
- Knowledge distillation
- Neural architecture search
- Mixed precision training

¿Cómo complementan las técnicas tradicionales?
```

### Prompt I2: Hardware específico
```
Analiza optimizaciones específicas para hardware:
- GPU (NVIDIA, AMD)
- CPU (Intel, ARM)
- Edge devices (Raspberry Pi, Coral)
- Mobile (iOS, Android)

¿Qué técnicas funcionan mejor en cada plataforma?
```

### Prompt I3: Frameworks emergentes
```
Investiga frameworks de optimización emergentes:
- TensorRT (NVIDIA)
- OpenVINO (Intel)
- CoreML (Apple)
- TFLite (Google)

Compara sus ventajas y desventajas con ONNX Runtime.
```

---

## 📝 Prompts de Documentación

### Prompt D1: README del proyecto
```
Crea un README.md para un proyecto de optimización de modelos que incluya:
1. Descripción del proyecto
2. Requisitos
3. Instalación
4. Uso
5. Ejemplos
6. Benchmarking
7. Contributing
8. License
```

### Prompt D2: Documentación de API
```
Documenta una API de optimización de modelos que incluya:
- Endpoints disponibles
- Parámetros de entrada
- Formatos de respuesta
- Códigos de error
- Ejemplos de uso
```

### Prompt D3: Changelog
```
Crea un changelog para una librería de optimización de modelos:
- v1.0.0: Soporte para cuantización INT8
- v1.1.0: Agregar pruning estructurado
- v1.2.0: Integración con ONNX Runtime
- v2.0.0: API completa de optimización
```

---

## 🎯 Prompts Específicos del Capítulo

### Prompt Cap11-1: Metáfora del mesonero
```
Explica la importancia de la latencia usando la metáfora del mesonero:
- Un mesonero que tarda 5 minutos en traer la comida
- Un mesonero que trae el pedido incorrecto
- Un mesonero rápido pero que olvida ingredientes
- El mesonero perfecto: rápido y preciso

¿Qué modelo de ML se parece a cada caso?
```

### Prompt Cap11-2: Caso práctico
```
Diseña un caso práctico completo para el capítulo:
Contexto: Empresa de e-commerce necesita modelo de recomendación
Restricciones:
- Latencia < 100ms
- Precisión > 85%
- Tamaño < 50MB
- Must run on edge devices

Incluye:
1. Análisis de baseline
2. Estrategia de optimización
3. Implementación
4. Resultados
5. Lecciones aprendidas
```

### Prompt Cap11-3: Ética en optimización
```
Crea un debate sobre ética en optimización:
Tesis: "Es ético sacrificar 2% de precisión por 3x de velocidad"

Argumentos a favor:
- Más usuarios pueden acceder al servicio
- Costos reducidos permiten más inversión
- Velocidad mejora experiencia de usuario

Argumentos en contra:
- 2% puede significar vidas perdidas
- Sesgos pueden amplificarse
- Usuarios no dan consentimiento informado

Conclusión: ¿Cuándo es ético y cuándo no?
```

---

## 📚 Prompts de Investigación Académica

### Prompt IA1: Paper seminal
```
Analiza el paper "Deep Compression" (Han et al., 2016):
1. ¿Cuál es la contribución principal?
2. ¿Qué técnicas combinan?
3. ¿Qué resultados obtienen?
4. ¿Cómo ha influenciado el campo?
5. ¿Qué limitaciones tiene?
```

### Prompt IA2: Cuantización moderna
```
Analiza el paper "Quantization and Training of Neural Networks" (Jacob et al., 2018):
1. ¿Qué es la quantization-aware training?
2. ¿Cómo difiere de la cuantización post-training?
3. ¿Qué ganancias reportan?
4. ¿Qué casos de uso recomiendan?
```

### Prompt IA3: Survey de optimización
```
Crea un mini-survey de técnicas de optimización de modelos:
1. Introducción al problema
2. Técnicas principales
3. Comparación de métodos
4. Aplicaciones
5. Direcciones futuras
6. Conclusión
```

---

## 🎮 Prompts Gamificados

### Prompt G1: Challenge de optimización
```
Crea un challenge de optimización:
Objetivo: Reducir un modelo de 500MB a <50MB sin perder más de 3% de precisión

Reglas:
1. Solo puedes usar técnicas del capítulo
2. Debes documentar cada paso
3. El modelo debe funcionar en producción
4. Debes probar en hardware real

Puntos:
- Cada 10% de reducción: 10 puntos
- Cada 1% de precisión conservada: 5 puntos
- Documentación completa: 20 puntos
- Código funcional: 30 puntos
```

### Prompt G2: Quiz interactivo
```
Crea un quiz de 10 preguntas sobre optimización:
1. ¿Qué es la cuantización?
2. ¿Cuándo usar pruning estructurado?
3. ¿Qué es ONNX?
4. ¿Qué métricas son importantes en benchmarking?
5. ¿Qué es el P95?
6. ¿Cuánto se puede reducir con INT8?
7. ¿Qué es sparsity?
8. ¿Cuándo NO debes optimizar?
9. ¿Qué es ONNX Runtime?
10. ¿Qué es throughput?

Incluye respuestas y explicaciones.
```

### Prompt G3: Simulación de producción
```
Simula un escenario de producción:
Situación: Tu modelo de clasificación tarda 2 segundos en inferir

Preguntas:
1. ¿Qué técnicas aplicarías primero?
2. ¿Cómo medirías el impacto?
3. ¿Qué métricas报告arías a tu jefe?
4. ¿Qué harías si la precisión cae demasiado?
5. ¿Cómo documentarías los cambios?
```

---

*Estos prompts están diseñados para guiar el aprendizaje progresivo del capítulo sobre optimización de modelos para producción.*
