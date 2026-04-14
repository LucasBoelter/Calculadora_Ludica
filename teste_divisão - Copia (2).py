# Testes numeros
import random;
# dividendo = random.randint(900,20000);
# dividendo = 148923 
dividendo = 9426 

titulo = "Calculadora ludica"
print("+" + "-" * (len(titulo) + 2) + "+")
print("| " + titulo + " |")
print("+" + "-" * (len(titulo) + 2) + "+")

dividendo = input("Dividendo: ")
divisor = input("Divisor: " + dividendo + " / ")

dividendo = int(dividendo)
divisor = int(divisor)


print(f"Cálculo: {dividendo} / {divisor} = ?");

# tranformando em lista
lista_caracteres = list(str(dividendo))

lista_final = []
resto_proximo = 0

for i in lista_caracteres:
    numero_da_lista = int(i)

    # verifica se tem resto_proximo e atualiza numero se necessário
    resto_proximo = int(resto_proximo*10)
    numero_da_lista = numero_da_lista + resto_proximo

    # calculando inteiro e resto
    inteiro = numero_da_lista//divisor
    resto = numero_da_lista%divisor
    
    # desenhando
    desenho_solto = " * "*numero_da_lista
    grupo = "["+" * "*divisor+"]"
    desenho_agrupado = grupo*inteiro + " *"*resto

    info_com_resto = f"{int(resto_proximo/10)} e {numero_da_lista-resto_proximo} = {numero_da_lista}"
    info_sem_resto = str(numero_da_lista)

    print("="*100)
    if resto_proximo > 0:
        espaços = len(info_com_resto)
        print(f"{info_com_resto} {desenho_solto}")
        print(f"{" "*espaços} {desenho_agrupado}")
    else:
        espaços = len(info_sem_resto)
        print(f"{info_sem_resto} {desenho_solto}")
        print(f"{" "*espaços} {desenho_agrupado}")
        # print(info_sem_resto)


    # adiciona na lista
    if inteiro > 0:
        lista_final.append(str(inteiro))
    
    # atualiza o resto
    resto_proximo = resto
    if resto_proximo > 0:
        print("Sobrou:", resto_proximo)

# rearranjando numeros
resultado = ""
for i in lista_final:
    resultado = resultado + str(i);


print("="*100)
print("Resultado final:",resultado)