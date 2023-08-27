# Pregunta 2

from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()

    font_list = figlet.getFonts()
    print("Fuentes disponibles:")
    for font in font_list:
        print(font)

    selected_font = input("Ingrese el nombre de la fuente (o presione Enter para aleatoria): ")
    if selected_font == "":
        selected_font = random.choice(font_list)

    text_to_print = input("Ingrese el texto a imprimir: ")

    figlet.setFont(font=selected_font)
    rendered_text = figlet.renderText(text_to_print)
    
    print("\nTexto impreso con la fuente seleccionada:")
    print(rendered_text)

if __name__ == "__main__":
    main()
    