
base_conocimiento = {
    "reglas": {
        "asistencia": {
            "pregunta": "¿Tuvo asistencia completa?",
            "tipo": "directa",
                "respuestas": {
                    "sin_faltas": 100,
                    "faltas_justificada": 80,
                    "faltas_no_justificada": 0,
                    "llegadas_tarde": 50
                },
            "peso": 0.20
        },
        "objetivos": {
            "pregunta": "¿Cumplió los objetivos? (Estado y Razón si aplica)",
            "tipo": "directa",
            "respuestas": {
                "cumplido": {"estado": 100, "razon": None},
                "no_cumplido": {
                    "estado": 0,
                    "razones": {
                        "grupal": 50, # Si no se cumple por razón grupal
                        "personal": 0  # Si no se cumple por razón personal
                    }
                }
            },
            "peso": 0.30
        },
        "desempeno": {
            "pregunta": "Desempeño y responsabilidad (0-100%)",
            "tipo": "porcentaje",
            "rangos": {
                "excelente": {"min": 90, "max": 100, "puntaje": 100},
                "bueno": {"min": 75, "max": 89, "puntaje": 80},
                "aceptable": {"min": 50, "max": 74, "puntaje": 60},
                "necesita_mejorar": {"min": 0, "max": 49, "puntaje": 20}
            },
            "peso": 0.25
        },
        "tiempo": {
            "pregunta": "Gestión del tiempo (0-100%)",
            "tipo": "rango", # Usará la función procesar_rangos
            "peso": 0.15
        },
        "equipo": {
            "pregunta": "Trabajo en equipo y colaboración (0-100%)",
            "tipo": "rango", # Usará la función procesar_rangos
            "peso": 0.10
        }
    }
}


