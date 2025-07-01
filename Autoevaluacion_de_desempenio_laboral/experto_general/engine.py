

def procesar_rangos(valor):
    """Procesa un valor porcentual para determinar un puntaje de rango."""
    try:
        valor = int(valor)
    except ValueError:
        return 0 # Valor por defecto si no es un número válido

    if valor >= 80:
        return 100
    elif 50 <= valor <= 79: # Corregido para incluir 79
        return 70
    else:
        return 0

def inferir_resultado(respuestas, base_conocimiento):
    """
    Infiere el resultado de la evaluación basándose en las respuestas del usuario
    y la base de conocimiento.
    Devuelve el puntaje final, una lista de puntajes detallados y una explicación.
    """
    puntajes_detallados = []
    explicacion_proceso = []
    puntaje_final_ponderado = 0

    reglas = base_conocimiento.get("reglas", {}) # Accede a las reglas

    for clave, respuesta_usuario in respuestas.items():
        regla = reglas.get(clave)

        if not regla:
            explicacion_proceso.append(f"Advertencia: No se encontró una regla para '{clave}'.")
            continue

        puntaje_criterio = 0
        explicacion_criterio = f"'{regla['pregunta']}' ({clave}): "

        if regla.get("tipo") == "directa":
            if clave == "objetivos":
                estado_objetivos = respuesta_usuario.get("estado")
                if estado_objetivos == "cumplido":
                    puntaje_criterio = regla["respuestas"]["cumplido"]["estado"]
                    explicacion_criterio += f"Objetivos cumplidos. Puntaje: {puntaje_criterio}."
                elif estado_objetivos == "no_cumplido":
                    razon = respuesta_usuario.get("razon")
                    puntaje_criterio = regla["respuestas"]["no_cumplido"]["razones"].get(razon, 0)
                    explicacion_criterio += f"Objetivos no cumplidos por razón '{razon}'. Puntaje: {puntaje_criterio}."
                else:
                    explicacion_criterio += "Estado de objetivos no reconocido. Puntaje: 0."
            else: # Asistencia u otras directas simples
                puntaje_criterio = regla["respuestas"].get(respuesta_usuario, 0)
                explicacion_criterio += f"Respuesta '{respuesta_usuario}'. Puntaje: {puntaje_criterio}."

        elif regla.get("tipo") == "porcentaje":
            valor_porcentaje = int(respuesta_usuario) # Ya se valida a int en app.py
            for rango_nombre, detalles_rango in regla["rangos"].items():
                if detalles_rango["min"] <= valor_porcentaje <= detalles_rango["max"]:
                    puntaje_criterio = detalles_rango["puntaje"]
                    explicacion_criterio += f"{valor_porcentaje}% cae en el rango '{rango_nombre}'. Puntaje: {puntaje_criterio}."
                    break
            else:
                explicacion_criterio += f"{valor_porcentaje}% no cae en ningún rango definido. Puntaje: 0."

        elif regla.get("tipo") == "rango":
            puntaje_criterio = procesar_rangos(respuesta_usuario)
            explicacion_criterio += f"Valor {respuesta_usuario}% procesado por rango. Puntaje: {puntaje_criterio}."
        
        else:
            explicacion_criterio += f"Tipo de regla desconocido para '{clave}'. Puntaje: 0."

        peso_criterio = regla.get("peso", 0)
        puntaje_ponderado_criterio = puntaje_criterio * peso_criterio
        puntaje_final_ponderado += puntaje_ponderado_criterio

        puntajes_detallados.append({
            "clave": clave,
            "pregunta": regla["pregunta"],
            "puntaje": puntaje_criterio,
            "peso": peso_criterio
        })
        explicacion_proceso.append(explicacion_criterio)

    return round(puntaje_final_ponderado, 2), puntajes_detallados, explicacion_proceso
