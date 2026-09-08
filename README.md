# Ciencia de Datos sin Filtros
## Guía para Profesionales que No toleran datasets de juguete

### Edición 2026

---

## Sobre este libro

Este libro fue escrito para profesionales de ingeniería de sistemas, analistas de datos y científicos de datos que quieren aprender ciencia de datos e inteligencia artificial con rigor técnico y sentido práctico. **No hay datasets de juguete.** Cada ejemplo usa datos sucios, reales y actuales.

### Los 5 Mandamientos que siguen todos los capítulos:

1. **Mata al Titanic y al MNIST** — Datasets sucios, reales y actuales desde el Capítulo 1
2. **El Diamante de la Estructura** — De la Estadística al ML, sin atajos
3. **El Taller Mecánico** — Código que no sea un copy-paste
4. **Del Notebook al Infierno** — MLOps y Deuda Técnica
5. **El Estilo del Científico de Datos Escéptico** — Ética incrustada en cada ejemplo

---

## Estructura del Libro

### Parte 1: Los Cimientos (Capítulos 1-3)
| Cap | Título | Tema Principal |
|-----|--------|----------------|
| 1 | El 80% de tu Trabajo es Data Wrangling | Fechas, nulos, duplicados, categorías |
| 2 | Describiendo lo que Ves | Estadística descriptiva y visualización |
| 3 | El Modelo Maldito | Regresión Lineal y Logística |

### Parte 2: El Taller del Científico de Datos (Capítulos 4-5)
| Cap | Título | Tema Principal |
|-----|--------|----------------|
| 4 | El Bosque y el Boost | Random Forest, XGBoost, LightGBM |
| 5 | Programando sin Programar | AutoML, H2O, KNIME, No-Code |

### Parte 3: La Fabricación de Modelos (Capítulos 6-7)
| Cap | Título | Tema Principal |
|-----|--------|----------------|
| 6 | Construyendo el Primer Modelo | Pipeline completo de ML |
| 7 | El Post-Mortem | Diagnóstico y mejora de modelos |

### Parte 4: Deep Learning (Capítulo 8)
| Cap | Título | Tema Principal |
|-----|--------|----------------|
| 8 | Cuando los Árboles No Suficienten | CNNs, RNNs, Transformers |

### Parte 5: Del Notebook al Infierno (Capítulos 9-11)
| Cap | Título | Tema Principal |
|-----|--------|----------------|
| 9 | Versiónando el Caos | DVC, Git, MLflow |
| 10 | Monitoreando en Producción | Data Drift y Concept Drift |
| 11 | La Latencia Mata al Modelo | ONNX, cuantización, deploy |

### Parte 6: Aplicaciones Empresariales (Capítulos 12-14)
| Cap | Título | Tema Principal |
|-----|--------|----------------|
| 12 | Análisis de Marketing con IA | ROAS, CPL, IA generativa |
| 13 | Optimización de Operaciones | Logística, rutas, predicción |
| 14 | Segmentación de Clientes | K-Means, clustering inteligente |

### Parte 7: Toma de Decisiones (Capítulos 15-16)
| Cap | Título | Tema Principal |
|-----|--------|----------------|
| 15 | Consultas en Lenguaje Natural | SQL con IA, copilotos de BI |
| 16 | Detección de Riesgos y Fraude | Anomalías, patrones fraudulentos |

### Capítulo Final
| Cap | Título | Tema Principal |
|-----|--------|----------------|
| 18 | El Futuro de la Ciencia de Datos | IA Agente y Autónoma |

---

## Cada capítulo incluye

```
capitulo_N/
├── capitulo_N.md              # Contenido completo del capítulo
├── notebooks/
│   └── capitulo_N.ipynb       # Jupyter notebook ejecutable
├── datos/
│   └── dataset.csv            # Datos para practicar
└── prompts/
    └── prompts_capitulo_N.md  # Prompts de IA (si aplica)
```

---

## Requisitos

```bash
# Instalación rápida
pip install pandas numpy scikit-learn matplotlib seaborn jupyter

# Instalación completa
pip install -r requirements.txt
```

---

## Cómo usar este libro

1. **Empieza por el Capítulo 1** — No saltes a modelos sin entender el wrangling
2. **Ejecuta los notebooks** — Cada celda está diseñada para ejecutarse secuencialmente
3. **Lee los Post-Mortem** — Los errores enseñan más que los aciertos
4. **Verifica la ética** — Cada ejemplo tiene un recuadro ético. Léelo.

---

## Autores y Referencias

Este libro sigue las recomendaciones de:
- Wickham, H. (2014). "Tidy Data". Journal of Statistical Software.
- Fayyad, U. et al. (1996). "From Data Mining to Knowledge Discovery in Databases". AI Magazine.
- James, G. et al. (2021). "An Introduction to Statistical Learning". Springer.
- Chen, T. & Guestrin, C. (2016). "XGBoost". KDD.
- LeCun, Y. et al. (2015). "Deep Learning". Nature.

---

## Licencia

Uso educativo y profesional. Los datasets incluidos son sintéticos pero representan problemas reales de la industria.
