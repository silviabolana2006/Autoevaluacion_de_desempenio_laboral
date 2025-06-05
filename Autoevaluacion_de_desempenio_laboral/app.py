from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# JSON de evaluación
evaluacion_json = '''{
  "Autoevaluación_de_desempeño_laboral": {
    "pregunta_1": {
      "tipo": "Asistencia",
      "opciones": {
        "sin_faltas": 100,
        "faltas": {
          "justificada": 100,
          "no_justificada": 0,
          "llegadas_tarde": 0
        }
      }
    },
    "pregunta_2": {
      "tipo": "Cumplimiento de objetivos",
      "opciones": {
        "cumplido": 100,
        "no_cumplido": {
          "razón_grupal": 50,
          "razón_personal": 0
        }
      }
    },
    "pregunta_3": {
      "tipo": "Desempeño y responsabilidad",
      "opciones": {
        "cumple": "porcentaje_ingresado",
        "no_cumple": 0
      }
    },
    "pregunta_4": {
      "tipo": "Concordancia entre habilidades y perfil del puesto",
      "opciones": {
        "porcentaje_ingresado": {
          "menor_50": 0,
          "50_70": 70,
          "mayor_80": 100
        }
      }
    },
    "pregunta_5": {
      "tipo": "Trabajo en equipo y colaboración",
      "opciones": {
        "porcentaje_ingresado": {
          "menor_50": 0,
          "50_70": 70,
          "mayor_80": 100
        }
      }
    }
  }
}'''

evaluacion = json.loads(evaluacion_json)

def calcular_puntaje(datos):
    puntajes = []
    for pregunta, respuesta in datos.items():
        opciones = evaluacion["Autoevaluación_de_desempeño_laboral"].get(pregunta, {}).get("opciones", {})

        if pregunta == "pregunta_3":
            try:
                puntaje = int(respuesta)
            except ValueError:
                puntaje = 0
        elif isinstance(opciones.get(respuesta), dict):
            puntaje = opciones.get("porcentaje_ingresado", {}).get(respuesta, 0)
        else:
            puntaje = opciones.get(respuesta, 0)

        puntajes.append(puntaje)

    return sum(puntajes) / len(puntajes)

@app.route('/evaluacion', methods=['POST'])
def evaluar():
    datos = request.json
    puntaje_total = calcular_puntaje(datos)
    return jsonify({"puntaje_total": round(puntaje_total, 2)})

if __name__ == '__main__':
    app.run(debug=True)
