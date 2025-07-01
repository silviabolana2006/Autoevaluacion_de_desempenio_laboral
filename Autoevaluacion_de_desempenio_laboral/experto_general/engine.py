
def procesar_rangos(valor):
    valor = int(valor)
    if valor >= 80:
        return 100
    elif 50 <= valor <= 70:
        return 70
    return 0

def inferir_resultado(respuestas_usuario, base_conocimiento):
    puntajes = []
    explicacion = []

    for clave, valor in respuestas_usuario.items():
        regla = base_conocimiento.get(clave)

        if not regla:
            explicacion.append(f"Advertencia: No se encontró una regla para '{clave}'.")
            continue

        puntaje_obtenido = 0
        if regla.get("tipo") == "porcentaje":
            try:
                puntaje_obtenido = int(valor)
                explicacion.append(f"'{regla['pregunta']}' ({clave}): Se obtuvo un {valor}% de cumplimiento, puntuación: {puntaje_obtenido}.")
            except ValueError:
                explicacion.append(f"Error: Valor no numérico para '{clave}'. Se asignó 0.")
                puntaje_obtenido = 0
        elif regla.get("tipo") == "rango":
            try:
                puntaje_obtenido = procesar_rangos(valor)
                explicacion.append(f"'{regla['pregunta']}' ({clave}): Valor '{valor}' procesado como rango, puntuación: {puntaje_obtenido}.")
            except ValueError:
                explicacion.append(f"Error: Valor no numérico para '{clave}'. Se asignó 0.")
                puntaje_obtenido = 0
        else:
            puntaje_obtenido = regla["respuestas"].get(valor.lower(), 0)
            if puntaje_obtenido == 0 and valor.lower() not in regla["respuestas"]:
                explicacion.append(f"'{regla['pregunta']}' ({clave}): Respuesta '{valor}' no reconocida. Se asignó 0.")
            else:
                explicacion.append(f"'{regla['pregunta']}' ({clave}): Respuesta '{valor}', puntuación: {puntaje_obtenido}.")

        puntajes.append(puntaje_obtenido)

    resultado_final = sum(puntajes) // len(puntajes) if puntajes else 0
    return resultado_final, puntajes, explicacion
