from flask import Flask, render_template, request
from experto_general.base import base_conocimiento
from experto_general.engine import inferir_resultado

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html', base=base_conocimiento)

@app.route('/resultado', methods=['POST'])
def resultado():
    respuestas = {}
    for clave in base_conocimiento:
        respuestas[clave] = request.form.get(clave)

    puntaje = inferir_resultado(respuestas, base_conocimiento)

    if puntaje >= 90:
        mensaje = f"✅ Excelente desempeño ({puntaje}%)"
    elif puntaje >= 70:
        mensaje = f"🟡 Desempeño aceptable ({puntaje}%)"
    else:
        mensaje = f"🔴 Necesita mejorar ({puntaje}%)"

    return render_template("resultado.html", mensaje=mensaje)
