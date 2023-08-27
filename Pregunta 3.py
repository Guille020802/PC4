#Pregunta 3

import shutil

import requests

url =  'https://unsplash.com/es/fotos/fk4tiMlDFF0'

response = requests.get(url)

with open ('perrito.jpg', 'wb') as f:
    f.write( response.content)
    pass


