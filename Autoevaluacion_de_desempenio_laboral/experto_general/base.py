base_conocimiento = {
    "reglas": {
        "asistencia": {
            "pregunta": "Asistencia",
            "tipo": "directa",
            "respuestas": {
                "sin_faltas": 100,
                "faltas.justificada": 100, # Asumiendo que el frontend enviará "faltas.justificada"
                "faltas.no_justificada": 0, # Asumiendo que el frontend enviará "faltas.no_justificada"
                "llegadas_tarde": 0
            }
        },
        "objetivos": {
            "pregunta": "Cumplimiento de objetivos",
            "tipo": "directa", # Este tipo indica que usa respuestas directas, incluyendo anidadas
            "respuestas": {
                "cumplido": 100,
                "no_cumplido": { # Aquí es donde se anidan las opciones de razón
                    "grupal": 50,
                    "personal": 0
                }
            }
        },
        "desempeno": {
            "pregunta": "Desempeño y responsabilidad",
            "tipo": "porcentaje", # Este tipo indica que el valor es el puntaje directo
            "respuestas": {} # No hay respuestas predefinidas, el valor se toma directamente
        },
        "tiempo": {
            "pregunta": "Gestión del tiempo", # Corregido el nombre de la pregunta
            "tipo": "rango", # Este tipo indica que usa la función procesar_rangos
            "respuestas": {} # Las reglas de rango se manejan en procesar_rangos
        },
        "equipo": {
            "pregunta": "Trabajo en equipo y colaboración",
            "tipo": "rango", # Este tipo indica que usa la función procesar_rangos
            "respuestas": {} # Las reglas de rango se manejan en procesar_rangos
        }
    }
}
