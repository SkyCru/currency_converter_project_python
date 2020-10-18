'''
NUEVO CONVERSOR DE DIVISA
'''
def converting(usd, divisa):
    ##Precio dólar
    usd = usd
    ##Aquí le pedimos al usuario que ingrese la cantidad en pesos de la divisa que desea convertir
    coin = input('INGRESA LA CANTIDAD EN PESOS'+ str(divisa))
    ##Convertimos el string que nos devuelve el input(output) a número flotante
    coin = float(coin)
    ##Hacemos la conversión, redondeamos números, y convertimos a string (cadena de texto), para concatenar. 
    result = coin / usd
    result = round(result,1)
    result = str(result)
    ##Mostramos el resultado
    print('Usted tiene $'+ result + ' dólares')

menu = """
HOLA! BIENVENIDO AL CONVERSOR DE DIVISA 💸

1 - PESOS MEXICANOS
2 - PESOS ARGENTINOS
3 - PESOS CHILENOS

ELIGE UNA OPCIÓN: """

options = input (menu)

if options == '1':
    converting(21.12, ' MEXICANOS: ')
    
elif options == '2':
    converting(77.51, ' ARGENTINOS: ')

elif options == '3':
    converting(793.50, ' CHILENOS: ')

else: 
    print("Error, please enter a valid number")
    