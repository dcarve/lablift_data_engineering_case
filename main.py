
from flask import Flask, jsonify, request
from modules import functions
import pandas as pd
import joblib
from werkzeug.middleware.proxy_fix import ProxyFix
from os import environ


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/donation', methods=['POST'])
def json_example():
    req_data = request.get_json()
    
    patient_id = req_data['patient_id']
    
    dict_patient_id = functions.primary_function(patient_id)
    
    dict_patient_id_aux = {}
    for k in dict_patient_id:
        dict_patient_id_aux[k] = [dict_patient_id[k]]

    
    model = joblib.load(r'modules/blood_donation_model.joblib')

    dict_patient_id['prediction'] = int(model.predict(pd.DataFrame(dict_patient_id_aux))[0])

    dict_patient_id['patient_id'] = patient_id

    return jsonify(dict_patient_id)


if __name__ == '__main__':

    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    app.run(host=SERVER_HOST,port=5500, debug=(not environ.get('ENV') == 'PRODUCTION'),threaded=True)