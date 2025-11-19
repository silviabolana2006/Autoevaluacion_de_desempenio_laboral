## Tecnicaturatura Superior en Ciencia de Datos e Inteligencia Artificial

Politécnico Malvinas Argentinas.


# Sistema Experto: Autoevaluación de Desempeño Laboral

Este proyecto es un sistema experto optimizado para la autoevaluación de desempeño laboral. Permite a los empleados evaluar su rendimiento de manera objetiva y automatizada, utilizando reglas y un motor de inferencia basado en conocimiento experto de RRHH.

## Características principales
- Evaluación automática por criterios: asistencia, cumplimiento de objetivos, desempeño, gestión del tiempo y trabajo en equipo.
- Motor de inferencia optimizado y explicaciones detalladas.
- Interfaz web moderna y fácil de usar.
- Resultados y recomendaciones personalizadas.

## Reglas y criterios
Las reglas del sistema se basan en criterios medibles y objetivos:
1. Asistencia: Puntaje según faltas y llegadas tarde.
2. Cumplimiento de objetivos: Considera razones grupales o personales.
3. Desempeño y responsabilidad: Porcentaje y rangos.
4. Gestión del tiempo: Rango porcentual.
5. Trabajo en equipo: Rango porcentual.

## Estructura del proyecto
- `app.py`: servidor Flask y lógica principal.
- `experto_general/`: motor de inferencia, base de conocimiento y clases.
- `templates/`: formularios y resultados HTML.
- `static/`: estilos CSS.
- `requirements.txt`: dependencias.

## Instalación y ejecución
1. Clona el repositorio:
   ```bash
   git clone https://github.com/silviabolana2006/Autoevaluacion_de_desempenio_laboral.git
   cd Autoevaluacion_de_desempenio_laboral/Autoevaluacion_de_desempenio_laboral
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   # source venv/bin/activate  # En Linux/MacOS
   ```
3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
5. Accede en tu navegador a:
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Solución de problemas
Si falta alguna dependencia, instálala con pip (ejemplo: `pip install flask-cors`).

## Créditos
Autor: Bolaña Silvia
Colaboración: Experto en RRHH Federico Magaldi

## Video demostrativo
[YouTube](https://www.youtube.com/watch?v=EmN-NL9oaQs)
## Estructura del proyecto (resumen)

- `app.py`: archivo principal que levanta el servidor Flask.
-  `doc`: contiene la documentacion del sistema experto.
- `experto_general/`: contiene la lógica del motor de inferencia y reglas.
- `templates/`: archivos HTML (formulario y resultado).
- `static/`: archivos estáticos (estilos CSS).
- `requirements.txt`: dependencias del proyecto.

