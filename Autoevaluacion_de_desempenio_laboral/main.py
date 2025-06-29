from experto_general.base import base_conocimiento
from experto_general.engine import inferir_resultado

def obtener_respuestas():
    respuestas = {}
    for clave, datos in base_conocimiento.items():
        pregunta = datos.get("pregunta")
        tipo = datos.get("tipo", "opciones")

        print(f"\n📌 {pregunta}")

        if tipo == "porcentaje" or tipo == "rango":
            while True:
                try:
                    valor = int(input("Ingrese un valor del 0 al 100: "))
                    if 0 <= valor <= 100:
                        respuestas[clave] = valor
                        break
                    else:
                        print("⚠️ Debe ser un número entre 0 y 100.")
                except ValueError:
                    print("⚠️ Ingrese un número válido.")
        else:
            print("Opciones disponibles:")
            for opcion in datos["respuestas"].keys():
                print(f" - {opcion}")
            valor = input("Seleccione una opción: ").lower()
            respuestas[clave] = valor
    return respuestas

def mostrar_resultado(score):
    print("\n🧾 Resultado de la autoevaluación:")
    if score >= 90:
        print(f"✅ Excelente desempeño ({score}%)")
    elif score >= 70:
        print(f"🟡 Desempeño aceptable ({score}%)")
    else:
        print(f"🔴 Necesita mejorar ({score}%)")

if __name__ == "__main__":
    print("=== SISTEMA EXPERTO: AUTOEVALUACIÓN DE DESEMPEÑO LABORAL ===")
    respuestas_usuario = obtener_respuestas()
    resultado = inferir_resultado(respuestas_usuario, base_conocimiento)
    mostrar_resultado(resultado)
