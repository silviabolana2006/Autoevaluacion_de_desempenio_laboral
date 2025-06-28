from flask import Flask, request, jsonify, render_template
import json
from flask_cors import CORS # Import Flask-CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all routes (for development purposes)

# JSON de evaluación 
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
            continue # Ignora preguntas que no estén definidas en nuestro esquema de evaluación

        tipo_pregunta = preguntas_definidas[pregunta_key]["tipo"]
        puntaje_obtenido = 0 # Inicializa el puntaje para cada pregunta

        if tipo_pregunta == "asistencia":
            # Reglas para "asistencia" (pregunta_1)
            if respuesta_data == "sin_faltas" or respuesta_data == "faltas.justificada":
                puntaje_obtenido = 100
            elif respuesta_data == "faltas.no_justificada" or respuesta_data == "llegadas_tarde":
                puntaje_obtenido = 0
            
        elif tipo_pregunta == "cumplimiento":
            # Reglas para "cumplimiento de objetivos" (pregunta_2)
            # Esperamos un diccionario con "estado" y opcionalmente "razon"
            estado = respuesta_data.get("estado")
            razon = respuesta_data.get("razon")

            if estado == "cumplido":
                puntaje_obtenido = 100
            elif estado == "no_cumplido":
                if razon == "grupal":
                    puntaje_obtenido = 50
                elif razon == "personal":
                    puntaje_obtenido = 0
            
        elif tipo_pregunta == "desempeño":
            # Reglas para "desempeño y responsabilidad" (pregunta_3)
            # Esperamos un diccionario con "estado" y "valor_ingresado"
            if isinstance(respuesta_data, dict) and respuesta_data.get("estado") == "cumple":
                try:
                    # El puntaje es el valor numérico ingresado
                    puntaje_ingresado = int(respuesta_data.get("valor_ingresado", 0))
                    # Aseguramos que el puntaje no exceda 100
                    if puntaje_ingresado > 100:
                        puntaje_obtenido = 100
                    else:
                        puntaje_obtenido = puntaje_ingresado
                except ValueError:
                    # Si el valor ingresado no es un número, se considera 0
                    puntaje_obtenido = 0 
            elif isinstance(respuesta_data, dict) and respuesta_data.get("estado") == "no_cumple":
                puntaje_obtenido = 0
            
        elif tipo_pregunta == "habilidades" or tipo_pregunta == "trabajo_equipo":
            # Reglas para "habilidades" (pregunta_4) y "trabajo en equipo" (pregunta_5)
            # Ambas usan el mismo rango porcentual
            try:
                # Se espera un porcentaje entero directamente como respuesta_data
                porcentaje = int(respuesta_data)
                if porcentaje >= 80:
                    puntaje_obtenido = 100
                elif 50 <= porcentaje < 80:
                    puntaje_obtenido = 70
                else: # porcentaje < 50
                    puntaje_obtenido = 0
            except ValueError:
                # Si el valor no es numérico, se considera 0
                puntaje_obtenido = 0 
        
        puntajes.append(puntaje_obtenido)

    if not puntajes:
        # Si no se evaluó ninguna pregunta válida, el puntaje total es 0
        return 0 

    # Calcula el promedio de los puntajes obtenidos
    return sum(puntajes) / len(puntajes)

@app.route('/evaluacion', methods=['POST'])
def evaluar():
    """
    Endpoint para recibir los datos de la autoevaluación y devolver el puntaje total.
    Los datos deben enviarse como JSON en el cuerpo de la solicitud POST.
    """
    datos = request.json
    if not datos:
        return jsonify({"error": "No se recibieron datos de evaluación. Por favor, envía un JSON con tus respuestas."}), 400
        
    puntaje_total = calcular_puntaje(datos)
    return jsonify({"puntaje_total": round(puntaje_total, 2)})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Ejecuta la aplicación Flask en modo de depuración para desarrollo
    # Considera usar un servidor de producción como Gunicorn en un entorno real
    app.run(debug=True)
