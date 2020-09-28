'''
Aquí crearemos un conversor de divisa mxn a usd
'''
##Aquí le pedimos al usuario que ingrese la cantidad en pesos mexicanos que desea convertir
mxn = input('INGRESE LA CANTIDAD A CONVERTIR EN PESOS MEXICANOS:')
##Convertimos el string que nos devuelve el input(output) a número flotante
mxn = float(mxn)
##Precio dólar
usd = 22.32
##Hacemos la conversión, redondeamos números, y convertimos a string (cadena de texto), para concatenar. 
result = mxn / usd
result = round(result,1)
result = str(result)
##Mostramos el resultado
print('Usted tiene $'+ result + ' dólares')
