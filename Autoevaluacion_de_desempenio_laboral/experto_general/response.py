
def interpretar_puntaje_final(puntaje_final):
    if puntaje_final >= 90:
        return "Rendimiento Excelente"
    elif puntaje_final >= 75:
        return "Buen Rendimiento"
    elif puntaje_final >= 50:
        return "Rendimiento Aceptable"
    else:
        return "Necesita Mejorar"

def formatear_explicacion_html(explicacion_proceso):
    if not explicacion_proceso:
        return "<p>No hay detalles de explicación disponibles.</p>"
    
    html_output = "<ul>\n"
    for linea in explicacion_proceso:
        html_output += f"    <li>{linea}</li>\n"
    html_output += "</ul>"
    return html_output

def generar_resumen_evaluacion_html(evaluacion: 'EvaluacionEmpleado'):
    """
    Genera un bloque HTML completo que resume los resultados de la evaluación.
    Ahora usa el formato detallado de puntajes_individuales.
    """
    html_resumen = f"""
    <h2>Resultados de la Evaluación para {evaluacion.nombre_empleado}</h2>
    <p><strong>Puntaje Final Promedio:</strong> {evaluacion.puntaje_final}</p>
    <p><strong>Interpretación:</strong> {evaluacion.interpretacion}</p>

    <h3>Puntajes por Criterio:</h3>
    <ul>
    """
    #  itera sobre los diccionarios en puntajes_individuales
    for item in evaluacion.puntajes_individuales:
        html_resumen += f"    <li><strong>{item['pregunta']}</strong> ({item['clave']}): {item['puntaje']}</li>\n"
    
    html_resumen += """
    </ul>

    <h3>Explicación Detallada del Proceso:</h3>
    """
    html_resumen += formatear_explicacion_html(evaluacion.explicacion_proceso)
    
    return html_resumen

