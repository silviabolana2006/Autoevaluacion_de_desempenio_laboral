
from flask import Flask, render_template, request, redirect, url_for

# Importar la base de conocimiento
from base import base_conocimiento

# Importar las funciones del motor de inferencia
from engine import inferir_resultado, procesar_rangos 

# Importar la clase de datos para la evaluación
from property import EvaluacionEmpleado

# Importar las funciones para generar respuestas y formatear el HTML
from response import interpretar_puntaje_final, generar_resumen_evaluacion_html

app = Flask(__name__)

@app.route('/')
def index():
    """
    Ruta para la página inicial que muestra el formulario de evaluación.
    """
    # Pasamos 'base_conocimiento' a la plantilla para que pueda generar las preguntas dinámicamente.
    return render_template('formulario_evaluacion.html', preguntas=base_conocimiento)

@app.route('/evaluar', methods=['POST'])
def evaluar():
    """
    Ruta que procesa las respuestas del formulario, ejecuta el motor de inferencia
    y muestra los resultados.
    """
    if request.method == 'POST':
        respuestas_form = request.form # Obtiene los datos enviados por el formulario (ImmutableMultiDict)

        #  Crea una nueva instancia del objeto de evaluación
        evaluacion = EvaluacionEmpleado(
            id_empleado=respuestas_form.get('id_empleado'),
            nombre_empleado=respuestas_form.get('nombre_empleado')
        )

        #  respuestas del formulario a la estructura esperada por inferir_resultado
        # almacenarlas en el objeto EvaluacionEmpleado
        respuestas_para_inferencia = {}
  
        for clave_pregunta, regla in base_conocimiento.items(): # Itera directamente sobre base_conocimiento, si no tiene "reglas"
            if clave_pregunta == "id_empleado" or clave_pregunta == "nombre_empleado":
                continue # Saltar los campos que no son preguntas de la base de conocimiento
            
            respuesta_recibida = respuestas_form.get(clave_pregunta)
            if respuesta_recibida is not None: # Asegurarse de que la respuesta no es None
                evaluacion.agregar_respuesta(clave_pregunta, respuesta_recibida)
                respuestas_para_inferencia[clave_pregunta] = respuesta_recibida

        # Ejecuta el motor de inferencia con las respuestas y la base de conocimiento
        puntaje_final, puntajes_detallados, explicacion = inferir_resultado(
            respuestas_para_inferencia, base_conocimiento # Aquí pasas la base completa
        )

        #  Actualiza el objeto de evaluación con los resultados obtenidos
        evaluacion.set_resultados_inferencia(puntaje_final, puntajes_detallados, explicacion)
        evaluacion.set_interpretacion(interpretar_puntaje_final(puntaje_final))

        #  Genera el HTML de resumen para mostrarlo en la plantilla
        resumen_html = generar_resumen_evaluacion_html(evaluacion)

        #  Renderiza la plantilla de resultados, pasando el HTML generado y los datos de la evaluación
        return render_template('resultados_evaluacion.html', resumen_html=resumen_html, evaluacion_data=evaluacion.to_dict())
    
    # Si la solicitud no es POST, redirigir al formulario
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Ejecuta la aplicación Flask en modo depuración (útil durante el desarrollo)
    app.run(debug=True)
