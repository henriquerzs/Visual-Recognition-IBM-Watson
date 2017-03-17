__author__ = 'henrique.zinidasilva@student.hamk.fi'

import json
from watson_developer_cloud import VisualRecognitionV3
from os.path import join, dirname

# Configuracao da API
VR = VisualRecognitionV3(version='2016-05-20', api_key = 'YOUR_API_KEY' )

#Criando novas classes
with open(join(dirname(__file__), '../images/beagle.zip'), 'rb') as beagle, \
    open(join(dirname(__file__), '../images/golden-retriever.zip'), 'rb') as goldenRetriever, \
    open(join(dirname(__file__), '../images/cats.zip'), 'rb') as cats, \
    open(join(dirname(__file__), '../images/husky.zip'), 'rb') as husky:


    print(json.dumps(VR.create_classifier('dogs', beagle_positive_examples=beagle, goldenRetriever_positive_examples=goldenRetriever, husky_positive_examples=husky, negative_examples=cats), indent=4))



#A resposta sera algo similar ao texto abaixo

# {
#     "status": "training",
#     "name": "dogs",
#     "created": "2017-03-16T13:09:25.753Z",
#     "classes": [
#         {
#             "class": "husky"
#         },
#         {
#             "class": "goldenRetriever"
#         },
#         {
#             "class": "beagle"
#         }
#     ],
#     "owner": "*********-5dcb-*****-****-67**15a7**",
#     "classifier_id": "dogs_89945619"
# }


#OBTENDO LISTA DE CLASSIFICADORES E INFORMACOES ESPECIFICAS SOBRE UM CLASSIFICADOR JA CRIADO
print(VR.list_classifiers())
print(json.dumps(VR.get_classifier('dogs_89945619'), indent=2))

#Teste com o classificador geral(default) e com o novo classificador criado
print(json.dumps(VR.classify(images_url='https://i.ytimg.com/vi/bx7BjjqHf2U/maxresdefault.jpg'), indent=2))
print(json.dumps(VR.classify(images_url='https://i.ytimg.com/vi/bx7BjjqHf2U/maxresdefault.jpg',classifier_ids='dogs_89945619'), indent=2))