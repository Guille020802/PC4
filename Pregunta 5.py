# Pregunta 5

def almacenar_en_txt(data):
    with open("bitcoin_prices.txt", "w") as archivo:
        for fecha, precio in data.items():
            archivo.write(f"{fecha}: {precio}\n")

# Supongamos que 'data' es un diccionario con datos de precio en formato {'fecha': precio}
data = {
    "2023-08-25": 50000,
    "2023-08-24": 51000,
    # ... y así sucesivamente
}

almacenar_en_txt(data)
print("Datos almacenados en bitcoin_prices.txt")

# CSV

import csv

def almacenar_en_csv(data):
    with open("bitcoin_prices.csv", "w", newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Fecha", "Precio"])
        for fecha, precio in data.items():
            writer.writerow([fecha, precio])

# Supongamos que 'data' es un diccionario con datos de precio en formato {'fecha': precio}
data = {
    "2023-08-25": 50000,
    "2023-08-24": 51000,
    # ... y así sucesivamente
}

almacenar_en_csv(data)
print("Datos almacenados en bitcoin_prices.csv")