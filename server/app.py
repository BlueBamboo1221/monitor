import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
import os


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/ping/log')
def effectuer_le_ping():
    #latence = ping("google.fr")
    response_object = {'status': 'success'}
    labels = []
    values = []
    fichier = open(os.path.join("logs", "data.log"), 'r')
    data = fichier.read()
    fichier.close()
    tab = data.split('\n')
    for line in tab:
        if line is not '':
            donnee = line.split('||')
            values.append(donnee[1])
            labels.append(donnee[0])
    response_object['values'] = values
    response_object['labels'] = labels
    return jsonify(response_object)        

if __name__ == '__main__':
    app.run()
