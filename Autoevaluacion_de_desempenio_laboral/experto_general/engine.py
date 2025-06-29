def procesar_rangos(valor):
    valor = int(valor)
    if valor >= 80:
        return 100
    elif 50 <= valor <= 70:
        return 70
    return 0

def inferir_resultado(respuestas, base):
    puntajes = []
    for clave, valor in respuestas.items():
        regla = base.get(clave)

        if not regla:
            continue

        if regla.get("tipo") == "porcentaje":
            puntajes.append(int(valor))

        elif regla.get("tipo") == "rango":
            puntajes.append(procesar_rangos(valor))

        else:
            puntajes.append(regla["respuestas"].get(valor.lower(), 0))

    return sum(puntajes) // len(puntajes) if puntajes else 0
