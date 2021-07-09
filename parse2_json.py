import json
  
# archivo en memoria
f = open('a.json')
  
#json a diccionario
data = json.load(f)

#salida de transcribe. Obtener el nombre del trabajo
print(data['jobName'])

#imprimir resultado del audio en texto
print(data['results']['transcripts'][0]['transcript'])

#obtener cada palabra y el valor de confianza
for i in data['results']['items']:
    print("palabra: " + i['alternatives'][0]['content'] + " - confianza: " + i['alternatives'][0]['confidence'])

# liberar de memoria
f.close()