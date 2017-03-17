__author__ = 'henrique.zinidasilva@student.hamk.fi'

import json
from watson_developer_cloud import VisualRecognitionV3
from os.path import join, dirname

# Configuracao da API
VR = VisualRecognitionV3(version='2016-05-20', api_key = 'YOUR_API_KEY' )

# Detectar rostos com imagem local
with open(join(dirname(__file__), '../images/henrique3.jpg'),'rb') as image_file:
	Resultados = VR.detect_faces(images_file=image_file)

#Mostra o resultado no formato json
print(json.dumps(Resultados))
