import json
  
# archivo en memoria
f = open('test.json')
  
#json a diccionario
data = json.load(f)
  
# recorrer json. Listo todos los elementos contenidos en errors.
for i in data['errors']:
    print(i)
  
#listo de cada error el status
for j in data['errors']:
    print(j['status'])

#de cada error me quedo con el detalle
for j in data['errors']:
    print(j['detail'])

# liberar de memoria
f.close()