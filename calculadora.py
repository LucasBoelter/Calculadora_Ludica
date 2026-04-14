def mostrar_titulo(titulo):
    print("+" + "-" * (len(titulo) + 2) + "+")
    print("| " + titulo + " |")
    print("+" + "-" * (len(titulo) + 2) + "+")

def ler_inteiro(mensagem):
    return int(input(mensagem))

def desenhar_etapa(numero, divisor, inteiro, resto, etapa=""):
    icone = "🍬"
    itens = " ".join([icone] * numero)
    grupo = "[" + " ".join([icone] * divisor) + "]"
    grupos = " ".join([grupo] * inteiro)
    sobras = " ".join([icone] * resto)

    largura = 80
    rotulo = 8

    print("=" * largura)
    if etapa:
        print(f"{etapa:^{largura}}")
        print("-" * largura)

    print(f"{'Número':<{rotulo}}: {numero}")
    print(f"{'Itens':<{rotulo}}: {itens}")
    print(f"{'Grupos':<{rotulo}}: {grupos if grupos else '(nenhum)'}")
    print(f"{'Resto':<{rotulo}}: {sobras if sobras else '(vazio)'}")
    print("=" * largura)



# Testes numeros
import random;
dividendo = random.randint(10,99);
divisor = random.randint(0,10);

# Apresentação
titulo = "Calculadora ludica"
mostrar_titulo(titulo)

# Coleta de dados
# dividendo = ler_inteiro("Dividendo: ")
# divisor = ler_inteiro(f"Divisor para {dividendo} / ")


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
resultado = "".join(lista_final)


casas_decimais = 2

if resto_proximo > 0:
    resultado += ","

    for casa in range(casas_decimais):
        numero_da_lista = resto_proximo * 10
        inteiro = numero_da_lista // divisor
        resto = numero_da_lista % divisor

        desenhar_etapa(numero_da_lista, divisor, inteiro, resto, etapa=f"Casa decimal {casa + 1}")

        resultado += str(inteiro)
        resto_proximo = resto

        if resto_proximo == 0:
            break

print("Resultado final:",resultado)