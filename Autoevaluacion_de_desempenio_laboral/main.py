
from base_conocimiento import base_conocimiento
from engine import procesar_rangos, inferir_resultado 

def obtener_respuestas_usuario(base_conocimiento):
    respuestas = {}
    print("Por favor, responda las siguientes preguntas:")
    for clave, regla in base_conocimiento.items():
        pregunta = regla["pregunta"]
        while True:
            respuesta_str = input(f"{pregunta} ")
            if regla.get("tipo") == "porcentaje" or regla.get("tipo") == "rango":
                try:
                    valor = int(respuesta_str)
                    if 0 <= valor <= 100:
                        respuestas[clave] = valor
                        break
                    else:
                        print("Por favor, ingrese un número entre 0 y 100.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
            else:
                opciones_validas = [k.lower() for k in regla["respuestas"].keys()]
                if respuesta_str.lower() in opciones_validas:
                    respuestas[clave] = respuesta_str
                    break
                else:
                    print(f"Respuesta inválida. Las opciones son: {', '.join(opciones_validas)}")
    return respuestas

def interpretar_resultado(puntaje_final):
    if puntaje_final >= 90:
        return "Rendimiento Excelente"
    elif puntaje_final >= 75:
        return "Buen Rendimiento"
    elif puntaje_final >= 50:
        return "Rendimiento Aceptable"
    else:
        return "Necesita Mejorar"

def main():
    print("--- Sistema de Evaluación de Rendimiento ---")

    respuestas_usuario = obtener_respuestas_usuario(base_conocimiento)

    puntaje_final, puntajes_individuales, explicacion = inferir_resultado(respuestas_usuario, base_conocimiento)

    print("\n--- Resultados de la Evaluación ---")
    print(f"Puntajes individuales: {puntajes_individuales}")
    print(f"Puntaje Final Promedio: {puntaje_final}")
    print(f"Interpretación del Resultado: {interpretar_resultado(puntaje_final)}")

    print("\n--- Explicación del Proceso ---")
    for linea in explicacion:
        print(f"- {linea}")

if __name__ == "__main__":
    main()
