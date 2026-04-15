def mostrar_titulo(titulo):
    print("+" + "-" * (len(titulo) + 2) + "+")
    print("| " + titulo + " |")
    print("+" + "-" * (len(titulo) + 2) + "+")

def ler_inteiro(mensagem):
    return int(input(mensagem))

def mostrar_icones(qtd, icone="🍬", max_exibir=20):
    if qtd <= max_exibir:
        return " ".join([icone] * qtd)
    return " ".join([icone] * max_exibir) + f" ... (+{qtd - max_exibir})"

def mostrar_grupos(inteiro, divisor, icone="🍬", largura_max=60):
    grupo = "[" + " ".join([icone] * divisor) + "]"
    grupos = []
    largura_atual = 0
    grupos_exibidos = 0

    for _ in range(inteiro):
        trecho = grupo if grupos_exibidos == 0 else " " + grupo

        if largura_atual + len(trecho) > largura_max:
            break

        grupos.append(trecho)
        largura_atual += len(trecho)
        grupos_exibidos += 1

    resultado = "".join(grupos)

    if grupos_exibidos < inteiro:
        restante = inteiro - grupos_exibidos
        resultado += f" ... (+{restante} grupos)"

    return resultado if resultado else "(nenhum)"

def desenhar_etapa(numero, divisor, inteiro, resto, etapa=""):
    icone = "🍬"

    largura = 80
    rotulo = 8
    largura_conteudo = 46

    itens = mostrar_icones(numero, icone, max_exibir=20)
    grupos = mostrar_grupos(inteiro, divisor, icone, largura_max=largura_conteudo)
    sobras = mostrar_icones(resto, icone, max_exibir=12)

    print("=" * largura)
    if etapa:
        print(f"{etapa:^{largura}}")
        print("-" * largura)

    print(f"{'Número':<{rotulo}}: {numero}")
    print(f"{'Itens':<{rotulo}}: {itens}")
    print(f"{'Grupos':<{rotulo}}: {grupos}")
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