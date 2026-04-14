import random;

# sortear numero
# numero_sorteado = random.randint(900,20000);
numero_sorteado = 148923 
# numero_sorteado = 9426 
print(f"Cálculo: {numero_sorteado} / 3 = ?");


# tranformando em lista
lista_caracteres = list(str(numero_sorteado))

lista_final = []
resto_proximo = 0

for i in lista_caracteres:
    numero_da_lista = int(i)

    # verifica se tem resto_proximo e atualiza numero se necessário
    resto_proximo = int(resto_proximo*10)
    numero_da_lista = numero_da_lista + resto_proximo

    # calculando inteiro e resto
    inteiro = numero_da_lista//3
    resto = numero_da_lista%3
    
    # desenhando
    desenho_solto = " * "*numero_da_lista
    desenho_agrupado = "[ * * * ]"*inteiro + " *"*resto

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