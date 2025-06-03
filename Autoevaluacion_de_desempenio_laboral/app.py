from flask import Flask, request, jsonify

app = Flask(__name__)

# JSON estructurado como referencia interna para la evaluación
AUTOEVALUACION_CONFIG = {
    "asistencia": {
        "sin_faltas": 100,
        "faltas": {
            "justificada": 100,
            "no_justificada": 0,
            "llegadas_tarde": 0
        }
    },
    "cumplimiento": {
        "cumplido": 100,
        "no_cumplido": {
            "razón_grupal": 50,
            "razón_personal": 0
        }
    },
    "perfil": {
        "menor_50": 0,
        "50_70": 70,
        "mayor_80": 100
    },
    "equipo": {
        "menor_50": 0,
        "50_70": 70,
        "mayor_80": 100
    }
}

def procesar_evaluacion(datos):
    puntaje_total = 0

    # Evaluar asistencia
    asistencia = datos.get("asistencia")
    if asistencia in AUTOEVALUACION_CONFIG["asistencia"]:
        puntaje_total += AUTOEVALUACION_CONFIG["asistencia"][asistencia]
    elif asistencia in AUTOEVALUACION_CONFIG["asistencia"]["faltas"]:
        puntaje_total += AUTOEVALUACION_CONFIG["asistencia"]["faltas"][asistencia]

    # Evaluar cumplimiento de objetivos
    cumplimiento = datos.get("cumplimiento")
    if cumplimiento in AUTOEVALUACION_CONFIG["cumplimiento"]:
        puntaje_total += AUTOEVALUACION_CONFIG["cumplimiento"][cumplimiento]
    elif cumplimiento in AUTOEVALUACION_CONFIG["cumplimiento"]["no_cumplido"]:
        puntaje_total += AUTOEVALUACION_CONFIG["cumplimiento"]["no_cumplido"][cumplimiento]

    # Evaluar desempeño y responsabilidad
    desempeño = int(datos.get("desempeño", 0))
    puntaje_total += desempeño

    # Evaluar concordancia con el perfil del puesto
    perfil = int(datos.get("perfil", 0))
    perfil_puntaje = (
        AUTOEVALUACION_CONFIG["perfil"]["mayor_80"] if perfil > 80 else
        AUTOEVALUACION_CONFIG["perfil"]["50_70"] if 50 <= perfil <= 70 else
        AUTOEVALUACION_CONFIG["perfil"]["menor_50"]
    )
    puntaje_total += perfil_puntaje

    # Evaluar trabajo en equipo
    equipo = int(datos.get("equipo", 0))
    equipo_puntaje = (
        AUTOEVALUACION_CONFIG["equipo"]["mayor_80"] if equipo > 80 else
        AUTOEVALUACION_CONFIG["equipo"]["50_70"] if 50 <= equipo <= 70 else
        AUTOEVALUACION_CONFIG["equipo"]["menor_50"]
    )
    puntaje_total += equipo_puntaje

    return {"puntaje_total": puntaje_total}

@app.route('/evaluacion', methods=['POST'])
def evaluar_desempeño():
    datos = request.json
    resultado = procesar_evaluacion(datos)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
