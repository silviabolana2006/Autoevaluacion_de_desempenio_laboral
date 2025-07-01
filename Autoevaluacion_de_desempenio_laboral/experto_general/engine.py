
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
from ingeneri import inferir_resultado, procesar_rangos # Importa las funciones de tu archivo ingeneri.py

app = Flask(__name__)
CORS(app) # Habilita CORS para permitir solicitudes desde el frontend (importante para desarrollo)

# La base de conocimiento con las reglas de evaluación
# Esta estructura es crucial y debe coincidir con lo que 'inferir_resultado' espera.
base_conocimiento = {
    "reglas": {
        "pregunta_1": {
            "pregunta": "Asistencia",
            "tipo": "directa",
            "respuestas": {
                "sin_faltas": 100,
                "faltas.justificada": 100,
                "faltas.no_justificada": 0,
                "llegadas_tarde": 0
            }
        },
        "pregunta_2": {
            "pregunta": "Cumplimiento de objetivos",
            "tipo": "directa", # Maneja la anidación internamente en inferir_resultado
            "respuestas": {
                "cumplido": 100,
                "no_cumplido": { # Aquí se definen las sub-opciones para "no_cumplido"
                    "grupal": 50,
                    "personal": 0
                }
            }
        },
        "pregunta_3": {
            "pregunta": "Desempeño y responsabilidad",
            "tipo": "porcentaje", # Indica que el valor de entrada es directamente el porcentaje
            "respuestas": {} # No hay respuestas predefinidas aquí, se usa el valor ingresado
        },
        "pregunta_4": {
            "pregunta": "Concordancia entre habilidades y perfil del puesto",
            "tipo": "rango", # Indica que se usará la función procesar_rangos
            "respuestas": {} # Las reglas de rango se gestionan en procesar_rangos
        },
        "pregunta_5": {
            "pregunta": "Trabajo en equipo y colaboración",
            "tipo": "rango", # Indica que se usará la función procesar_rangos
            "respuestas": {} # Las reglas de rango se gestionan en procesar_rangos
        }
    }
}


@app.route('/evaluacion', methods=['POST'])
def evaluar():
    """
    Endpoint de la API para recibir los datos de la autoevaluación,
    inferir el resultado usando la base de conocimiento y devolverlo como JSON.
    """
    datos = request.json # Obtiene los datos JSON enviados desde el frontend
    if not datos:
        return jsonify({"error": "No se recibieron datos de evaluación. Por favor, envía un JSON con tus respuestas."}), 400
        
    # Llama a la función inferir_resultado de ingeneri.py para obtener el puntaje y la explicación
    puntaje_total, puntajes_detallados, explicacion = inferir_resultado(datos, base_conocimiento)

    # Devuelve la respuesta como JSON
    return jsonify({
        "puntaje_total": round(puntaje_total, 2), # Redondea el puntaje total a dos decimales
        "puntajes_detallados": puntajes_detallados, # Información detallada por pregunta
        "explicacion": explicacion # Lista de cadenas que explican el cálculo
    })

@app.route('/')
def index():
    """
    Ruta para servir el archivo HTML principal del formulario de autoevaluación.
    Flask buscará 'index.html' dentro de la carpeta 'templates'.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Este bloque asegura que la aplicación Flask se ejecute cuando el archivo app.py es iniciado
    # 'debug=True' habilita el modo de depuración, que recarga el servidor automáticamente
    # con los cambios y muestra errores detallados. Usar solo para desarrollo.
    app.run(debug=True)
