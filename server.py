from flask import Flask, jsonify, make_response, request, render_template
from automation import commandManager

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/command', methods=['GET'])
def voiceCmd():
    commandResponse = commandManager(str(request.args['voiceCommand']))
    if commandResponse:
        return make_response(jsonify({'commandResponse' : 'Command executed'}),200)
    else:
        return make_response(jsonify({'commandResponse' : 'Command not recognized'}),200)