

class EvaluacionEmpleado:
    """
    Clase para encapsular los datos de una evaluación de empleado.
    Contiene las respuestas del usuario y los resultados de la inferencia.
    """
    def __init__(self, id_empleado=None, nombre_empleado="Desconocido"):
        self.id_empleado = id_empleado
        self.nombre_empleado = nombre_empleado
        self.respuestas = {}  # Diccionario para almacenar las respuestas del usuario
        self.puntajes_individuales = [] 
        self.puntaje_final = 0       # Puntaje promedio final
        self.interpretacion = ""    # Interpretación textual del puntaje final
        self.explicacion_proceso = [] # Lista de cadenas explicando la inferencia

    def agregar_respuesta(self, clave_pregunta, valor_respuesta):
        """
        Agrega una respuesta del usuario para un criterio específico.
        """
        self.respuestas[clave_pregunta] = valor_respuesta

    def set_resultados_inferencia(self, puntaje_final, puntajes_detallados, explicacion):
        """
        Establece los resultados obtenidos del motor de inferencia.
        puntajes_detallados ahora es una lista de diccionarios con {'clave', 'pregunta', 'puntaje'}
        """
        self.puntaje_final = puntaje_final
        self.puntajes_individuales = puntajes_detallados 
        self.explicacion_proceso = explicacion

    def set_interpretacion(self, interpretacion):
        """
        Establece la interpretación textual del puntaje final.
        """
        self.interpretacion = interpretacion

    def to_dict(self):
        """
        Convierte el objeto EvaluacionEmpleado a un diccionario, útil para serialización
        (ej. para pasar a una plantilla HTML o guardar en JSON).
        """
        return {
            "id_empleado": self.id_empleado,
            "nombre_empleado": self.nombre_empleado,
            "respuestas": self.respuestas,
            "puntajes_individuales": self.puntajes_individuales, 
            "puntaje_final": self.puntaje_final,
            "interpretacion": self.interpretacion,
            "explicacion_proceso": self.explicacion_proceso
        }
