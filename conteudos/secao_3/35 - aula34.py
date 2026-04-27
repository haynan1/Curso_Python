'''
Repetições
while (enquanto)
Executa uma ação enquanto um condição for verdadeira.
Loop infinito -> Quando um código não tem fim.
'''

condicao = True

while condicao:
    nome = input("Qual o seu nome: ")
    print(f"Seu nome é {nome} !")
    

    if nome == "sair":
        break

print("Acabou !")



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# ESTRUTURA DE REPETIÇÃO - WHILE
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
WHILE = "ENQUANTO for verdadeiro, continue repetindo."
Se não houver parada, vira loop infinito.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
O laço WHILE é uma estrutura de repetição usada quando não sabemos
quantas vezes algo deve se repetir.

Ele executa um bloco de código ENQUANTO uma condição for verdadeira.

Estrutura básica:

while condicao:
    bloco_de_codigo

Fluxo de funcionamento:

1) O Python verifica a condição.
2) Se for True → executa o bloco.
3) Volta para o início.
4) Testa novamente.
5) Repete até a condição ser False.

LOOP INFINITO

Se a condição nunca se tornar False,
o programa ficará executando para sempre.
Isso é chamado de LOOP INFINITO.

Exemplo clássico:

condicao = True
while condicao:
    print("Nunca vai parar")

Esse código nunca termina porque a variável condicao
nunca muda para False.

COMO PARAR UM LOOP?

Podemos usar:

1) Alteração da condição.
2) A palavra reservada BREAK.

O BREAK força a saída imediata do loop,
mesmo que a condição ainda seja verdadeira.

No código enviado:

- A condição começa como True.
- O loop pede o nome.
- Se o usuário digitar "sair", o BREAK encerra o laço.
- Depois disso, o programa continua normalmente.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um programa que peça números ao usuário.
O programa deve continuar pedindo números até que o usuário digite 0.
Ao final, mostre a soma de todos os números digitados.
"""

# soma = 0  # cria uma variável acumuladora iniciando com 0
# while True:  # loop infinito controlado por break
#     numero = int(input("Digite um número (0 para sair): "))  # pede um número
#     if numero == 0:  # verifica se o usuário quer sair
#         break  # encerra o loop
#     soma += numero  # acumula o número digitado
# print(f"Soma total: {soma}")  # mostra o resultado final

"""
Explicação do código resolvido:

1) Criamos a variável soma para armazenar os valores.
2) Usamos while True para criar um loop contínuo.
3) Se o número for 0, usamos break para sair.
4) Caso contrário, somamos o número à variável soma.
5) Ao sair do loop, exibimos o resultado final.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Peça ao usuário uma senha.
Enquanto a senha for diferente de "1234",
continue pedindo novamente.
Quando acertar, mostre "Acesso permitido".
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Peça ao usuário vários números.
O programa deve parar quando o usuário digitar um número negativo.
Ao final, mostre:

- Quantos números foram digitados
- A média dos números
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie um programa que simule um menu:

1 - Dizer Olá
2 - Mostrar Data Fictícia
3 - Sair

O programa deve continuar rodando até que o usuário escolha a opção 3.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Peça um número ao usuário.
Mostre a tabuada desse número de 1 a 10.
Após mostrar, pergunte se ele deseja calcular outra tabuada.
Se responder "sim", repita.
Se responder "não", encerre.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# while True:  # inicia loop infinito
#     senha = input("Digite a senha: ")  # pede senha
#     if senha == "1234":  # verifica se está correta
#         print("Acesso permitido")  # mensagem de sucesso
#         break  # encerra o loop
#     else:
#         print("Senha incorreta")  # mensagem de erro


# Exercício 2 - Médio

# soma = 0  # acumulador
# contador = 0  # contador de números
# while True:  # loop contínuo
#     numero = float(input("Digite um número (negativo para sair): "))  # pede número
#     if numero < 0:  # condição de parada
#         break  # sai do loop
#     soma += numero  # soma os valores
#     contador += 1  # conta quantos números foram digitados
# if contador > 0:  # evita divisão por zero
#     media = soma / contador  # calcula média
#     print(f"Quantidade: {contador}")  # mostra quantidade
#     print(f"Média: {media}")  # mostra média
# else:
#     print("Nenhum número válido foi digitado")  # caso especial


# Exercício 3 - Difícil

# while True:  # loop do menu
#     print("1 - Dizer Olá")
#     print("2 - Mostrar Data Fictícia")
#     print("3 - Sair")
#     opcao = input("Escolha uma opção: ")  # recebe opção
#     if opcao == "1":
#         print("Olá!")  # opção 1
#     elif opcao == "2":
#         print("01/01/2099")  # data fictícia
#     elif opcao == "3":
#         print("Encerrando...")  # mensagem de saída
#         break  # encerra o loop
#     else:
#         print("Opção inválida")  # caso erro


# Exercício 4 - Difícil

# while True:  # loop principal
#     numero = int(input("Digite um número para ver a tabuada: "))  # recebe número
#     for i in range(1, 11):  # percorre de 1 até 10
#         print(f"{numero} x {i} = {numero * i}")  # mostra multiplicação
#     resposta = input("Deseja calcular outra tabuada? (sim/não): ")  # pergunta
#     if resposta.lower() == "não":  # verifica se quer sair
#         break  # encerra o loop
