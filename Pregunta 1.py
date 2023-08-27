#Pregunta 1

import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raise an exception if there's an HTTP error
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
        return bitcoin_price
    except requests.RequestException as e:
        print("Error making request:", e)
        return None

def main():
    n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    bitcoin_price = get_bitcoin_price()

    if bitcoin_price is not None:
        total_cost = n * bitcoin_price
        print(f"El costo actual de {n:.4f} Bitcoins es: ${total_cost:,.4f}")

if __name__ == "__main__":
    main()