def desenhar_etapa(numero, divisor, inteiro, resto, etapa=""):
    icone = "🍬"
    itens = " ".join([icone] * numero)
    grupo = "[" + " ".join([icone] * divisor) + "]"
    grupos = " ".join([grupo] * inteiro)
    sobras = " ".join([icone] * resto)

    print("=" * 60)
    if etapa:
        print(etapa)
    print(f"Número : {numero}")
    print(f"Itens  : {itens}")
    print(f"Grupos : {grupos if grupos else '(nenhum grupo completo)'}")
    print(f"Resto  : {sobras if sobras else '(sem resto)'}")


def ler_inteiro(mensagem):
    return int(input(mensagem))

# Testes numeros
# import random;
# dividendo = random.randint(900,20000);
# dividendo = 148923 
# dividendo = 9426 

# Apresentação
titulo = "Calculadora ludica"
print("+" + "-" * (len(titulo) + 2) + "+")
print("| " + titulo + " |")
print("+" + "-" * (len(titulo) + 2) + "+")

# Coleta de dados
dividendo = ler_inteiro("Dividendo: ")
divisor = ler_inteiro(f"Divisor para {dividendo} / ")
# dividendo = input("Dividendo: ")
# divisor = input("Divisor: " + dividendo + " / ")

# dividendo = int(dividendo)
# divisor = int(divisor)

# teste por 0
if divisor == 0:
    print("Erro: não existe divisão por zero.")
    exit()

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
    
    desenhar_etapa(numero_da_lista, divisor, inteiro, resto)

    # adiciona na lista
    if inteiro > 0:
        lista_final.append(str(inteiro))
    
    # atualiza o resto
    resto_proximo = resto

# rearranjando numeros
resultado = ""
for i in lista_final:
    resultado = resultado + str(i);

casas_decimais = 5

if resto_proximo > 0:
    resultado += ","
    
    for _ in range(casas_decimais):
        numero_da_lista = resto_proximo * 10
        inteiro = numero_da_lista // divisor
        resto = numero_da_lista % divisor

        resultado += str(inteiro)
        resto_proximo = resto

        if resto_proximo == 0:
            break

print("="*100)
print("Resultado final:",resultado)