from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS

# Importar desde la carpeta experto_general
from experto_general.base import base_conocimiento
from experto_general.engine import inferir_resultado, procesar_rangos
from experto_general.property import EvaluacionEmpleado
from experto_general.response import interpretar_puntaje_final, generar_resumen_evaluacion_html

app = Flask(__name__)
CORS(app) # Habilita CORS

@app.route('/')
def index():
    """
    Ruta para la página inicial que muestra el formulario de evaluación.
    """
    return render_template('formulario_evaluacion.html', preguntas_reglas=base_conocimiento.get("reglas", {}))

@app.route('/evaluar', methods=['POST'])
def evaluar():
    """
    Ruta que procesa las respuestas del formulario, ejecuta el motor de inferencia
    y muestra los resultados.
    """
    if request.method == 'POST':
        respuestas_form = request.form # Obtiene los datos enviados por el formulario

        # Crea una nueva instancia del objeto de evaluación
        evaluacion = EvaluacionEmpleado(
            id_empleado=respuestas_form.get('id_empleado'),
            nombre_empleado=respuestas_form.get('nombre_empleado')
        )

        respuestas_para_inferencia = {}

        # Iterar sobre las reglas definidas en la base de conocimiento (dentro de "reglas")
        for clave_pregunta, regla in base_conocimiento.get("reglas", {}).items():
            pregunta_tipo = regla.get("tipo")

            if pregunta_tipo == "directa":
                if clave_pregunta == "objetivos":
                    estado = respuestas_form.get('objetivos_estado')
                    if estado == 'no_cumplido':
                        razon = respuestas_form.get('objetivos_razon')
                        respuestas_para_inferencia[clave_pregunta] = {"estado": estado, "razon": razon}
                    else:
                        respuestas_para_inferencia[clave_pregunta] = {"estado": estado}
                else:
                    respuesta_recibida = respuestas_form.get(clave_pregunta)
                    if respuesta_recibida is not None:
                        respuestas_para_inferencia[clave_pregunta] = respuesta_recibida
            elif pregunta_tipo == "porcentaje" or pregunta_tipo == "rango":
                respuesta_recibida = respuestas_form.get(clave_pregunta)
                if respuesta_recibida is not None:
                    try:
                        respuestas_para_inferencia[clave_pregunta] = int(respuesta_recibida)
                    except ValueError:
                        respuestas_para_inferencia[clave_pregunta] = 0

            if clave_pregunta in respuestas_para_inferencia:
                evaluacion.agregar_respuesta(clave_pregunta, respuestas_para_inferencia[clave_pregunta])

        # Ejecuta el motor de inferencia
        puntaje_final, puntajes_detallados, explicacion = inferir_resultado(
            respuestas_para_inferencia, base_conocimiento
        )

        # Actualiza el objeto de evaluación
        evaluacion.set_resultados_inferencia(puntaje_final, puntajes_detallados, explicacion)
        evaluacion.set_interpretacion(interpretar_puntaje_final(puntaje_final))

        # Genera el HTML de resumen
        resumen_html = generar_resumen_evaluacion_html(evaluacion)

        # Renderiza la plantilla de resultados
        return render_template('resultados_evaluacion.html', resumen_html=resumen_html, evaluacion_data=evaluacion.to_dict())
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
