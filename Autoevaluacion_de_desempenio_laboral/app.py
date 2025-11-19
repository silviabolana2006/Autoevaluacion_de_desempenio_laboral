
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from experto_general.base import base_conocimiento
from experto_general.engine import inferir_resultado
from experto_general.property import EvaluacionEmpleado
from experto_general.response import interpretar_puntaje_final, generar_resumen_evaluacion_html

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('formulario_evaluacion.html', preguntas_reglas=base_conocimiento.get("reglas", {}))

@app.route('/evaluar', methods=['POST'])
def evaluar():
    respuestas_form = request.form
    evaluacion = EvaluacionEmpleado(
        id_empleado=respuestas_form.get('id_empleado'),
        nombre_empleado=respuestas_form.get('nombre_empleado')
    )
    respuestas_para_inferencia = {}
    for clave, regla in base_conocimiento["reglas"].items():
        tipo = regla["tipo"]
        valor = respuestas_form.get(clave)
        if tipo == "directa":
            if clave == "objetivos":
                estado = respuestas_form.get('objetivos_estado')
                razon = respuestas_form.get('objetivos_razon') if estado == 'no_cumplido' else None
                respuestas_para_inferencia[clave] = {"estado": estado}
                if razon:
                    respuestas_para_inferencia[clave]["razon"] = razon
            elif valor is not None:
                respuestas_para_inferencia[clave] = valor
        elif tipo in ("porcentaje", "rango") and valor is not None:
            try:
                respuestas_para_inferencia[clave] = int(valor)
            except ValueError:
                respuestas_para_inferencia[clave] = 0
        if clave in respuestas_para_inferencia:
            evaluacion.agregar_respuesta(clave, respuestas_para_inferencia[clave])
    puntaje_final, puntajes_detallados, explicacion = inferir_resultado(
        respuestas_para_inferencia, base_conocimiento
    )
    evaluacion.set_resultados_inferencia(puntaje_final, puntajes_detallados, explicacion)
    evaluacion.set_interpretacion(interpretar_puntaje_final(puntaje_final))
    resumen_html = generar_resumen_evaluacion_html(evaluacion)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.headers.get('Accept') == 'application/json':
        return jsonify({
            "puntaje_final": puntaje_final,
            "puntajes_individuales": puntajes_detallados,
            "interpretacion": evaluacion.interpretacion,
            "explicacion": "\n".join(evaluacion.explicacion_proceso),
            "resumen_html": resumen_html
        })
    return render_template('resultados_evaluacion.html', resumen_html=resumen_html, evaluacion_data=evaluacion.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
