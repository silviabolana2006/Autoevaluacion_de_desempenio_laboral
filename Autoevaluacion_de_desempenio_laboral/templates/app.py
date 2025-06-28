from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# JSON de evaluación 
# las reglas de puntuación se aplicarán en la función calcular_puntaje
evaluacion_json = '''{
    "Autoevaluación_de_desempeño_laboral": {
        "pregunta_1": {
            "tipo": "asistencia"
        },
        "pregunta_2": {
            "tipo": "cumplimiento"
        },
        "pregunta_3": {
            "tipo": "desempeño"
        },
        "pregunta_4": {
            "tipo": "habilidades"
        },
        "pregunta_5": {
            "tipo": "trabajo_equipo"
        }
    }
}'''

evaluacion = json.loads(evaluacion_json)

def calcular_puntaje(datos):
    """
    Calcula el puntaje total de la autoevaluación basándose en las reglas definidas.
    """
    puntajes = []
    preguntas_definidas = evaluacion["Autoevaluación_de_desempeño_laboral"]

    for pregunta_key, respuesta_data in datos.items():
        if pregunta_key not in preguntas_definidas:
            continue # Ignora preguntas no definidas

        tipo_pregunta = preguntas_definidas[pregunta_key]["tipo"]
        puntaje_obtenido = 0

        if tipo_pregunta == "asistencia":
            # Reglas para asistencia
            if respuesta_data == "sin_faltas" or respuesta_data == "faltas.justificada":
                puntaje_obtenido = 100
            elif respuesta_data == "faltas.no_justificada" or respuesta_data == "llegadas_tarde":
                puntaje_obtenido = 0
            
        elif tipo_pregunta == "cumplimiento":
            # Reglas para cumplimiento de objetivos
            estado = respuesta_data.get("estado")
            razon = respuesta_data.get("razon") # Puede ser None si el estado es 'cumplido'

            if estado == "cumplido":
                puntaje_obtenido = 100
            elif estado == "no_cumplido":
                if razon == "grupal":
                    puntaje_obtenido = 50
                elif razon == "personal":
                    puntaje_obtenido = 0
            
        elif tipo_pregunta == "desempeño":
            # Reglas para desempeño y responsabilidad
            if isinstance(respuesta_data, dict) and respuesta_data.get("estado") == "cumple":
                try:
                    puntaje_obtenido = int(respuesta_data.get("valor_ingresado", 0))
                    # Asegurarse de que el puntaje no exceda 100
                    if puntaje_obtenido > 100:
                        puntaje_obtenido = 100
                except ValueError:
                    puntaje_obtenido = 0 # Valor no numérico
            elif isinstance(respuesta_data, dict) and respuesta_data.get("estado") == "no_cumple":
                puntaje_obtenido = 0
            
        elif tipo_pregunta == "habilidades" or tipo_pregunta == "trabajo_equipo":
            # Reglas para habilidades y trabajo en equipo (ambas usan el mismo rango porcentual)
            try:
                porcentaje = int(respuesta_data)
                if porcentaje >= 80:
                    puntaje_obtenido = 100
                elif 50 <= porcentaje < 80:
                    puntaje_obtenido = 70
                else: # porcentaje < 50
                    puntaje_obtenido = 0
            except ValueError:
                puntaje_obtenido = 0 # Valor no numérico
        
        puntajes.append(puntaje_obtenido)

    if not puntajes:
        return 0 # En caso de que no haya preguntas válidas

    return sum(puntajes) / len(puntajes)

@app.route('/evaluacion', methods=['POST'])
def evaluar():
    """
    Endpoint para recibir los datos de la autoevaluación y devolver el puntaje total.
    """
    datos = request.json
    if not datos:
        return jsonify({"error": "No se recibieron datos de evaluación."}), 400
        
    puntaje_total = calcular_puntaje(datos)
    return jsonify({"puntaje_total": round(puntaje_total, 2)})

if __name__ == '__main__':
    app.run(debug=True)
