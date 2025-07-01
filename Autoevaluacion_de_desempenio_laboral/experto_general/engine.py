

from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from base import base_conocimiento
from engine import inferir_resultado, procesar_rangos
from property import EvaluacionEmpleado
from response import interpretar_puntaje_final, generar_resumen_evaluacion_html

app = Flask(__name__)
CORS(app) # Habilita CORS para permitir solicitudes desde el frontend (importante para desarrollo)

@app.route('/')
def index():
    """
    Ruta para la página inicial que muestra el formulario de evaluación.
    """
    # Pasamos las reglas de la base de conocimiento a la plantilla para que pueda usarlas, si es necesario.
    # Usaremos base_conocimiento.get("reglas", {}) para acceder a la parte relevante.
    return render_template('formulario_evaluacion.html', preguntas_reglas=base_conocimiento.get("reglas", {}))

@app.route('/evaluar', methods=['POST'])
def evaluar():
    """
    Ruta que procesa las respuestas del formulario, ejecuta el motor de inferencia
    y muestra los resultados.
    """
    if request.method == 'POST':
        respuestas_form = request.form # Obtiene los datos enviados por el formulario (ImmutableMultiDict)

        # Crea una nueva instancia del objeto de evaluación
        evaluacion = EvaluacionEmpleado(
            id_empleado=respuestas_form.get('id_empleado'),
            nombre_empleado=respuestas_form.get('nombre_empleado')
        )

        # Prepara las respuestas para el motor de inferencia, manejando tipos complejos
        respuestas_para_inferencia = {}

        # Iterar sobre las reglas definidas en la base de conocimiento para saber qué esperar
        for clave_pregunta, regla in base_conocimiento.get("reglas", {}).items():
            pregunta_tipo = regla.get("tipo")

            if pregunta_tipo == "directa":
                if clave_pregunta == "objetivos":
                    # Manejo específico para la pregunta de objetivos que tiene estado y razón
                    estado = respuestas_form.get('objetivos_estado')
                    if estado == 'no_cumplido':
                        razon = respuestas_form.get('objetivos_razon')
                        # Guarda el valor como un diccionario, como espera inferir_resultado
                        respuestas_para_inferencia[clave_pregunta] = {"estado": estado, "razon": razon}
                    else:
                        # Si es "cumplido", solo necesitamos el estado
                        respuestas_para_inferencia[clave_pregunta] = {"estado": estado}
                else:
                    # Para otras preguntas directas simples como 'asistencia'
                    respuesta_recibida = respuestas_form.get(clave_pregunta)
                    if respuesta_recibida is not None:
                        respuestas_para_inferencia[clave_pregunta] = respuesta_recibida
            elif pregunta_tipo == "porcentaje" or pregunta_tipo == "rango":
                # Para preguntas que esperan un valor numérico
                respuesta_recibida = respuestas_form.get(clave_pregunta)
                if respuesta_recibida is not None:
                    try:
                        respuestas_para_inferencia[clave_pregunta] = int(respuesta_recibida)
                    except ValueError:
                        # En caso de que el usuario no ingrese un número válido
                        respuestas_para_inferencia[clave_pregunta] = 0

            # Añade las respuestas procesadas al objeto de evaluación
            if clave_pregunta in respuestas_para_inferencia:
                evaluacion.agregar_respuesta(clave_pregunta, respuestas_para_inferencia[clave_pregunta])

        # Ejecuta el motor de inferencia con las respuestas y la base de conocimiento
        # inferir_resultado ya espera la base completa (con la clave "reglas")
        puntaje_final, puntajes_detallados, explicacion = inferir_resultado(
            respuestas_para_inferencia, base_conocimiento
        )

        # Actualiza el objeto de evaluación con los resultados obtenidos
        evaluacion.set_resultados_inferencia(puntaje_final, puntajes_detallados, explicacion)
        evaluacion.set_interpretacion(interpretar_puntaje_final(puntaje_final))

        # Genera el HTML de resumen usando la función de response.py
        resumen_html = generar_resumen_evaluacion_html(evaluacion)

        # Renderiza la plantilla de resultados, pasando el HTML generado y los datos de la evaluación
        return render_template('resultados_evaluacion.html', resumen_html=resumen_html, evaluacion_data=evaluacion.to_dict())
    
    # Si la solicitud no es POST, redirigir al formulario
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Ejecuta la aplicación Flask en modo depuración (útil durante el desarrollo)
    app.run(debug=True)
