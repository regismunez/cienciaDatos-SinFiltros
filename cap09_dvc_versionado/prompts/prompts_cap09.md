# Prompts para Capítulo 9: Versionando el Caos (DVC y Control de Versiones)

## Prompts de Exploración

### Comprensión del Problema
1. **Explica por qué Git solo no es suficiente para ciencia de datos.** Incluye ejemplos de problemas comunes que surgen al intentar versionar datos grandes con Git.

2. **¿Cuál es la diferencia fundamental entre Git y DVC?** Usa una analogía para explicar cómo cada uno maneja el versionado.

3. **¿Qué significa "reproducibilidad" en el contexto de ciencia de datos?** Proporciona un ejemplo práctico de por qué es importante.

### DVC - Data Version Control
4. **Crea una guía paso a paso para configurar DVC con Google Drive como remote storage.** Incluye comandos específicos y posibles errores.

5. **Explica el flujo de trabajo completo de DVC:** init → add → commit → push → pull. Usa un ejemplo concreto con un dataset de clientes.

6. **¿Cómo funciona el tracking de versiones en DVC?** Explica el papel de los archivos `.dvc` y `.gitignore`.

7. **Compara DVC con soluciones alternativas** como LakeFS, Delta Lake, o DVC con S3 vs Google Drive.

### Estructura de Proyecto
8. **Diseña una estructura de proyecto estándar** para un proyecto de machine learning que incluya Git, DVC, y MLflow.

9. **¿Por qué es importante separar raw data de processed data?** Explica los beneficios de esta práctica.

10. **Crea un template de `params.yaml`** que sea fácil de mantener y versionar.

11. **Explica cómo configurar un `dvc.yaml`** para un pipeline de 3 etapas: prepare, featurize, train.

### MLflow y Tracking de Experimentos
12. **¿Qué problemas resuelve MLflow** en comparación con simplemente guardar resultados en un CSV?

13. **Crea una guía para registrar experimentos con MLflow** que incluya: parámetros, métricas, modelos, y artefactos.

14. **¿Cómo se integran DVC y MLflow?** Explica cómo usar versiones de datos de DVC dentro de experimentos de MLflow.

15. **Diseña un sistema de naming conventions** para experimentos en MLflow que facilita la comparación.

### Reproducibilidad
16. **¿Qué componentes son necesarios para la reproducibilidad completa?** Lista y explica cada uno.

17. **Crea un checklist de reproducibilidad** para un proyecto de ML.

18. **Explica cómo usar `dvc repro`** para reproducir un pipeline completo.

19. **¿Cómo manejas la reproducibilidad cuando los datos cambian frequentemente?**

### Ética y Trazabilidad
20. **¿Por qué la trazabilidad es un asunto ético** y no solo técnico?

21. **Diseña un template de metadata para modelos** que incluya: datos, proceso, evaluación, y auditoría ética.

22. **¿Qué información debe registrar cada modelo** para cumplir con regulaciones como GDPR o CCPA?

23. **Crea un checklist de auditoría ética** para modelos de ML en producción.

24. **Explica cómo la trazabilidad ayuda a mitigar sesgos** en modelos de ML.

### Casos de Uso Prácticos
25. **Un equipo de DS tiene 3 versiones de un dataset** y no saben cuál se usó para entrenar el modelo en producción. ¿Cómo resuelves esto con DVC?

26. **Un modelo en producción está dando resultados diferentes** a los del experimento. ¿Qué pasos seguirías para diagnosticar el problema?

27. **Necesitas comparar 10 experimentos** con diferentes hiperparámetros. ¿Cómo organizarías el tracking con MLflow?

28. **Un auditor te pide documentación completa** de un modelo crediticio. ¿Qué información necesitas proporcionar?

### Integración y Workflow
29. **Crea un workflow completo** desde la ingestión de datos hasta el deployment, usando Git + DVC + MLflow.

30. **¿Cómo manejas los merge conflicts** cuando dos científicos de datos modifican el pipeline simultáneamente?

31. **Diseña un proceso de code review** para cambios en el pipeline de ML.

32. **¿Cómo automatizas la validación** de que un pipeline es reproducible después de cambios?

### Solución de Problemas
33. **Un archivo .dvc está corrupto.** ¿Cómo recuperas la versión anterior?

34. **Los tiempos de ejecución del pipeline aumentaron** después de actualizar una librería. ¿Cómo diagnosticas y resuelves?

35. **DVC push falla porque el remote storage está lleno.** ¿Qué estrategias de limpieza implementas?

36. **MLflow no está registrando las métricas correctamente.** ¿Cómo depuras este problema?

### Arquitectura y Diseño
37. **Diseña un sistema de versionado** que escale para un equipo de 10 científicos de datos.

38. **¿Cómo implementar feature flags** para experimentos de ML?

39. **Crea una arquitectura de CI/CD** para pipelines de ML que incluya testing automatizado.

40. **¿Cómo manejar múltiples modelos en producción** con diferentes versiones de datos?

### Investigación y Tendencias
41. **¿Qué son los Feature Stores** y cómo se relacionan con el versionado de datos?

42. **Explora las diferencias entre MLOps y DevOps.** ¿Qué herramientas de MLOps son más relevantes?

43. **¿Cómo están evolucionando las herramientas de versionado de modelos** (Model Registry)?

44. **Investiga sobre Data Contracts** y cómo se relacionan con la reproducibilidad.

### Ejercicios Prácticos
45. **Crea un proyecto completo** desde cero usando la estructura del capítulo.

46. **Implementa un pipeline de ML** con al menos 3 experimentos y compara resultados.

47. **Genera documentación ética completa** para uno de los modelos entrenados.

48. **Simula un escenario de auditoría** donde necesitas justificar las decisiones del modelo.

### Reflexión Crítica
49. **¿Qué trade-offs existes** entre reproducibilidad y velocidad de experimentación?

50. **¿Debería ser obligatorio el versionado de datos** en proyectos de ML? Argumenta a favor o en contra.

51. **¿Cómo afecta la trazabilidad** a la confianza de los usuarios en los modelos de ML?

52. **Si tuvieras que elegir solo 3 herramientas** para MLOps, ¿cuáles serían y por qué?

---

## Prompts para Generación de Código

### Scripts de Utilidad
53. **Crea un script de Python** que automatice la inicialización de un proyecto con Git y DVC.

54. **Genera un script de validación** que verifique si un pipeline es reproducible.

55. **Diseña una función de logging** que registre automáticamente experimentos en MLflow.

56. **Crea un generador de reportes** de trazabilidad para modelos.

### Templates
57. **Genera un template de `dvc.yaml`** para pipelines de N etapas.

58. **Crea un template de `params.yaml`** para diferentes tipos de modelos (clasificación, regresión, clustering).

59. **Diseña un template de documentación ética** para modelos de ML.

60. **Genera un template de README.md** para proyectos de ciencia de datos con DVC.

---

## Prompts para Análisis

61. **Analiza el dataset de experimentos proporcionado** (`datos_experimentos_mlflow.csv`). ¿Qué tendencias observas?

62. **¿Qué modelo tiene el mejor balance** entre rendimiento y tiempo de entrenamiento?

63. **¿Cómo afecta el cambio de dataset** (v1.0 a v1.4) al rendimiento de los modelos?

64. **Identifica posibles problemas de sobreajuste** en los experimentos.

65. **¿Qué configuración de ensemble** ofrece el mejor rendimiento?

---

## Prompts para Discusión

66. **¿Es ético usar un modelo sin documentación completa** en producción?

67. **¿Quién es responsable** cuando un modelo toma una decisión incorrecta: el científico de datos, la empresa, o el algoritmo?

68. **¿Cómo平衡ar la transparencia del modelo** con la protección de propiedad intelectual?

69. **¿Deberían los modelos de ML tener "fecha de expiración"?** Argumenta.

70. **¿Cómo afecta la falta de trazabilidad** a la confianza del público en la IA?

---

*Estos prompts están diseñados para acompañar el Capítulo 9 y profundizar en los conceptos de versionado, reproducibilidad, y ética en ciencia de datos.*
