'''
Aquí crearemos un conversor de divisa usd a mxn
'''
##Aquí le pedimos al usuario que ingrese la cantidad en dólares estadounidenses que desea convertir
usd = input('INGRESE LA CANTIDAD EN DÓLARES ESTADOUNIDENSES: ')

##Convertimos el string que nos devuelve el input(output) a número flotante
usd = float(usd)

#Precio dólar
mxn = 22.32

##Hacemos la conversión, redondeamos números, y convertimos a string (cadena de texto), para concatenar. 
result = usd * mxn
result = round(result,1)
result = str(result)

##Mostramos el resultado
print(result)



