
def procesar_rangos(valor): #
    valor = int(valor) #
    if valor >= 80: #
        return 100 #
    elif 50 <= valor <= 70: #
        return 70 #
    return 0 #

def inferir_resultado(respuestas, base): 
    puntajes_detallados = []
    explicacion = [] # Para almacenar la explicación del proceso

    # Accede a las reglas dentro de la clave 'reglas'
    reglas_base = base.get("reglas", base) # Usa 'reglas' si está anidado, sino usa la base directamente

    for clave, valor in respuestas.items():
        regla = reglas_base.get(clave) #

        if not regla:
            explicacion.append(f"Advertencia: No se encontró una regla para '{clave}'.")
            continue

        puntaje_obtenido = 0
        pregunta_texto = regla.get("pregunta", clave) # Usar la pregunta definida o la clave si no existe

        if regla.get("tipo") == "porcentaje": 
            try:
                puntaje_obtenido = int(valor) 
                explicacion.append(f"'{pregunta_texto}' ({clave}): Se obtuvo un {valor}% de cumplimiento, puntuación: {puntaje_obtenido}.")
            except ValueError:
                explicacion.append(f"Error: Valor no numérico para '{clave}'. Se asignó 0.")
                puntaje_obtenido = 0
        elif regla.get("tipo") == "rango": 
            try:
                puntaje_obtenido = procesar_rangos(valor) 
                explicacion.append(f"'{pregunta_texto}' ({clave}): Valor '{valor}' procesado como rango, puntuación: {puntaje_obtenido}.")
            except ValueError:
                explicacion.append(f"Error: Valor no numérico para '{clave}'. Se asignó 0.")
                puntaje_obtenido = 0
        else: # Tipo de respuesta directa (respuestas predefinidas)
            puntaje_obtenido = regla["respuestas"].get(valor.lower(), 0) #
            if puntaje_obtenido == 0 and valor.lower() not in regla["respuestas"]:
                explicacion.append(f"'{pregunta_texto}' ({clave}): Respuesta '{valor}' no reconocida. Se asignó 0.")
            else:
                explicacion.append(f"'{pregunta_texto}' ({clave}): Respuesta '{valor}', puntuación: {puntaje_obtenido}.")

        # Añadimos un diccionario con la clave y el puntaje
        puntajes_detallados.append({"clave": clave, "pregunta": pregunta_texto, "puntaje": puntaje_obtenido})

    # Calcular el resultado final 
    total_puntajes_sum = sum(item["puntaje"] for item in puntajes_detallados)
    resultado_final = total_puntajes_sum // len(puntajes_detallados) if puntajes_detallados else 0 #
    
    # Retornamos los puntajes detallados en lugar de solo los números
    return resultado_final, puntajes_detallados, explicacion
