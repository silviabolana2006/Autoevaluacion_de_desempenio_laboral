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

Repositorio github

Lenguaje python, Html

Flask microframework

Enlace video

# Instrucciones para ejecutar el sistema

# Proyecto de Autoevaluación – Instrucciones de Ejecución

Este proyecto utiliza **Flask** para levantar una aplicación web de autoevaluación. A continuación, encontrarás los pasos necesarios para su correcta ejecución.

---

##  Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

-  Python 3.8 o superior
-  PIP (Gestor de paquetes de Python)
-  Navegador web moderno (Chrome, Firefox, Edge, etc.)

---

 1. Clonar el repositorio
git clone https://github.com/silviabolana2006/Autoevaluacion_de_desempenio_laboral.git
cd Autoevaluacion_de_desempenio_laboral


🛠️ 2. Crear y activar entorno virtual
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En Linux/MacOS:
source venv/bin/activate

 3. Instalar dependencias
pip install flask flask-cors

 Si ves el error ModuleNotFoundError: No module named 'flask_cors', asegúrate de instalar flask-cors manualmente:

pip install flask-cors


4. Ejecutar el sistema
python app.py


El sistema estará disponible en http://localhost:5000 si no has modificado la configuración por defecto de Flask.






## Estructura del proyecto (resumen)

- `app.py`: archivo principal que levanta el servidor Flask.
-  `doc`: contiene la documentacion del sistema experto.
- `experto_general/`: contiene la lógica del motor de inferencia y reglas.
- `templates/`: archivos HTML (formulario y resultado).
- `static/`: archivos estáticos (estilos CSS).
- `requirements.txt`: dependencias del proyecto.

