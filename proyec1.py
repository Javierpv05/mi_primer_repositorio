def pregunta_4 ( numero: int ) :
    while numero<1 or numero>3:
        numero=int(input('introdusca un numero[1-3] :'))
    suma= 0
    if numero==1:
        i=1
        while i<10:
            suma +=i
            i +=1
    elif numero ==2:
        j =10
        while j<100:
            suma += j
            j +=1
    elif numero ==3:
        k =100
        while k<1000:
            suma +=k
            k +=2
    return suma

numero=int(input('introdusca un numero[1-3] :'))
print('la suma de los numeros es :' ,pregunta_4(numero))