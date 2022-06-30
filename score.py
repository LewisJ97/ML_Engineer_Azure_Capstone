# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:15:28 2022

@author: 77901710
"""

import json
import numpy as np
import pandas as pd
import os
from sklearn.externals import joblib


def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    model = joblib.load(model_path)

def run(data):
    try:
        data = pd.DataFrame.from_dict(json.loads(data)['data'])
        result = model.predict(data)
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error