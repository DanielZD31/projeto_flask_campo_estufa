from flask import Flask, render_template, request
from fabrica.estufa import FabricaEstufa
from fabrica.campo import FabricaCampo
from singleton.conexao_xml import ConexaoXML
from fabrica.fabrica import FabricaCreator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    ambiente = request.form['ambiente']  
    fabrica = FabricaCreator.obter_fabrica(ambiente)   
    sensor = fabrica.criar_sensor_temperatura()
    irrigacao = fabrica.criar_modulo_irrigacao()
    
    return render_template(
        'resultado.html',
        sensor=sensor.ler(),
        irrigacao=irrigacao.acionar(),
        ambiente=ambiente.capitalize()
    )
    
if __name__ == '__main__':
    app.run(debug=True)