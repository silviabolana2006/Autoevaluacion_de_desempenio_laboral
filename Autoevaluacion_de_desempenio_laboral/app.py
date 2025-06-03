from flask import Flask, request, jsonify

app = Flask(__name__)

def procesar_evaluacion(datos):
    puntaje_total = 0


    asistencia = datos.get("asistencia")
    if asistencia == "sin_faltas":
        puntaje_total += 100
    elif asistencia == "faltas_justificadas":
        puntaje_total += 100
    elif asistencia == "faltas_no_justificadas" or asistencia == "llegadas_tarde":
        puntaje_total += 0

    
    cumplimiento = datos.get("cumplimiento")
    if cumplimiento == "cumplido":
        puntaje_total += 100
    elif cumplimiento == "razón_grupal":
        puntaje_total += 50
    elif cumplimiento == "razón_personal":
        puntaje_total += 0


    desempeño = int(datos.get("desempeño", 0))  
    puntaje_total += desempeño

    perfil = int(datos.get("perfil", 0))
    if perfil < 50:
        puntaje_total += 0
    elif 50 <= perfil <= 70:
        puntaje_total += 70
    elif perfil > 80:
        puntaje_total += 100

    equipo = int(datos.get("equipo", 0))
    if equipo < 50:
        puntaje_total += 0
    elif 50 <= equipo <= 70:
        puntaje_total += 70
    elif equipo > 80:
        puntaje_total += 100

    return {"puntaje_total": puntaje_total}

@app.route('/evaluacion', methods=['POST'])
def evaluar_desempeño():
    datos = request.json  
    resultado = procesar_evaluacion(datos)  
    return jsonify(resultado)  

if __name__ == '__main__':
    app.run(debug=True)
