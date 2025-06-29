## Tecnicaturatura Superior en Ciencia de Datos e Inteligencia Artificial

Politécnico Malvinas Argentinas.

Desarrollo de Sistemas de IA

Autor: Bolaña Silvia

## Autoevaluacion_de_desempenio_laboral



Este proyecto se basa en un sistema experto de “Autoevaluación de desempeño laboral", tiene como objetivo proporcionar una herramienta tecnológica para el area de RRHH, que permitirá a los trabajadores evaluar su rendimiento de manera objetiva, estructurada y automatizada. El diseño de este sistema experto garantizará la equidad en la evaluación, evitando sesgos y ofreciendo recomendaciones basadas en datos proporcionados por el propio empleado. La implementación de este sistema contribuirá a la transparencia en las relaciones laborales, optimizando el crecimiento profesional de los empleados y fortaleciendo la cultura organizacional dentro de las empresas, adaptando el sistema a la revolución tecnológica actual.

## Métodos de inferencia

El sistema experto aplica reglas de inferencia para procesar la información ingresada por el empleado y determinar su evaluación final. Se utilizan principalmente reglas If-Then( toma decisiones basadas en condiciones establecidas) y categorización por rangos de desempeño.

## Estructura del conocimiento

Para desarrollar el sistema experto de Autoevaluación del Desempeño Laboral, se llevó a cabo una entrevista con el profesor Federico Magaldi experto en Recursos Humanos, quien brindó su experiencia y conocimientos en la evaluación de desempeño. En esta entrevista, se definieron las métricas y criterios que el sistema utilizará para generar una evaluación objetiva del empleado. Las mismas están detalladas en las Reglas del sistema 

## Reglas del sistema

   1.Asistencia: Condiciones para asignar 100% o 0% según la presencia del empleado.    

   2.Cumplimiento de objetivos: Evaluación basada en cumplimiento personal o grupal. 

   3.Desempeño según el puesto: Uso de porcentajes según ítems de la descripción del cargo.

   4.Gestión del tiempo y organización: Categorización en rangos de desempeño.

   5.Trabajo en equipo y colaboración: Evaluación por diferentes criterios como comunicación y cooperación

## Criterios de evaluación

Cada área de evaluación está estructurada con criterios medibles y objetivos, permitiendo asignar un porcentaje basado en el desempeño del empleado. Las reglas del sistema se derivan de estos criterios, asegurando una evaluación justa y automatizada; Este enfoque basado en conocimiento experto garantiza que el sistema refleje estándares profesionales de Recursos Humanos, mejorando la calidad y precisión de la autoevaluación.

## Organización del conocimiento

El sistema experto organiza la información y toma decisiones utilizando un árbol de decisión, donde cada nodo representa una pregunta o condición y cada rama indica el resultado basado en la respuesta del empleado.

![image](https://github.com/user-attachments/assets/91a86160-8d80-4a75-87dc-a925100abaf6)




## Herramientas utilizadas
Librerías pathlib, json, graphviz

Repositorio github, git

Lenguaje python

Flask framework

Enlace video: https://drive.google.com/file/d/1cLHIRIvLz37prIXDfZAf-3s50PP8UHm-/view?usp=sharing

## Pasos para ejecutar el Sistema Experto

Instalación:
Para instalar y ejecutar este sistema experto, sigue estos pasos:

### Descargar en ZIP o Clonar el Repositorio

Para obtener el código en tu equipo, puedes elegir entre las siguientes opciones:

1. **Descargar en formato ZIP**  
   - Ingresa a la página web del repositorio.  
   - Busca la opción **"Download ZIP"**.  
   - Una vez descargado, extrae los archivos en tu equipo.  

2. **Clonar el repositorio**  
   - Abre una terminal o consola en tu equipo.  
   - Ejecuta el siguiente comando:  
     ```bash
     git clone <URL_DEL_REPOSITORIO>
     ```
   - Luego, navega al directorio del repositorio:  
     ```bash
     cd <NOMBRE_DEL_REPOSITORIO>
     ```
   - Ahora puedes acceder y utilizar el sistema experto.  



                                  




## Estructura del Proyecto
Autoevaluacion_desempeño_laboral/

├── app.py

├── main.py

├── requirements.txt

├── README.md

├── experto_general/

│   ├── base.py

│   ├── engine.py

│   └── __init__.py

├── templates/

│   ├── formulario.html

│   └── resultado.html

├── static/

│   └── estilo.css

├── Data/

│   └── evaluaciones_guardadas.json

├── Video/

│   └── demo_sistema_experto.mp4

└── docs/

    ├── manual_usuario.md
    ├── manual_tecnico.md
    └── arbol_decision.png

