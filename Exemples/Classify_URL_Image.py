__author__ = 'henrique.zinidasilva@student.hamk.fi'

import json
from watson_developer_cloud import VisualRecognitionV3

# Configuracao da API
VR = VisualRecognitionV3(version='2016-05-20', api_key = '9b367cc730c4e57599441b0b9b01bb612eb25a1a' )

#URL da imagem a ser classificada
url_image='http://3.bp.blogspot.com/-7Tl5bSuCbIk/VPPEvB_oJYI/AAAAAAAAAVE/n9aVLWKhxWo/s1600/locomotiva.jpg'


# Classificar uma imagem por URL
Resultados = VR.classify(images_url=url_image)

#Mostra o resultado no formato json
print(json.dumps(Resultados))

#Mostra o resultado individuais por classe
for i in Resultados['images'][0]['classifiers'][0]['classes']:
    print('\n Ha ' + str(i['score']*100) + ' % de chances da imagem conter(Classe): '+ i['class'])
