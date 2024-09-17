import json

dict_obj='{"K1":"V1","K2":"V2","K3":"V3"}'

result=json.loads(dict_obj)
print(result) # {'K1': 'V1', 'K2': 'V2', 'K3': 'V3'}
print(result['K1'])