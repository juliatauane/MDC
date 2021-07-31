import time
start_time = time.time()
a= int(input("Escreva o primeiro número:"))
b= int(input("Escreva o segundo número:"))
def mdc_recursivo(a,b): #função do mdc_recursivo
    if b > a: #se o número b for maior que o número a então

        return mdc_recursivo(b,a) #é feita a inversão para que o número a seja maior

    if b==0: # Critério de parada do return: se o número armazenado em b igual a zero, significa que o resto da divisão é igual a zero e o número armazenado em a é o maior divisor comum

        return a # Retorna o valor de a para

# função

    r= a%b #resto da divisão entre a e b é r

    return mdc_recursivo(b,r) # b e r retornam a função mdc_recursivo são armazenados em a e b

print("O mdc entre os dois números é:", mdc_recursivo(a,b))
print("--- %s seconds ---" % (time.time() - start_time))