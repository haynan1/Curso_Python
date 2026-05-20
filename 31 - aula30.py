"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

    Resumindo, deixe seu código legivel, e de fácil
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# CONSTANTES, LEGIBILIDADE E COMPLEXIDADE
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
Constante é regra fixa.
Código limpo simplifica.
Menos condição, menos confusão.
Legibilidade é evolução.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
🔎 O QUE É UMA CONSTANTE?

Em Python não existe uma palavra reservada chamada "constante",
mas por convenção usamos LETRAS MAIÚSCULAS para representar valores
que NÃO DEVEM MUDAR durante a execução do programa.

Exemplo:
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

Esses valores representam regras fixas do sistema.

----------------------------------------

🔎 POR QUE USAR CONSTANTES?

1) Evita números mágicos espalhados pelo código
2) Facilita manutenção
3) Aumenta legibilidade
4) Deixa claro o propósito do valor

----------------------------------------

🔎 COMPLEXIDADE EM CONDIÇÕES

Quando colocamos muitas condições dentro de um único if,
o código fica difícil de entender.

Exemplo ruim:
if velocidade > 60 and local >= 99 and local <= 101:

Melhor prática:
Criar variáveis booleanas com nomes claros:

vel_carro_pass_radar_1
carro_passou_radar_1
carro_multado_radar_1

Isso deixa o código:
- Mais legível
- Mais organizado
- Mais fácil de testar
- Mais fácil de manter

----------------------------------------

🔎 IDEIA PRINCIPAL

Divida sua lógica em partes pequenas.
Dê nomes claros.
Evite if gigantes.
Deixe o código "explicativo".

Código bom parece texto.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Sistema de Radar

Dado:
velocidade do carro
local do carro
velocidade máxima permitida
local do radar
alcance do radar

Crie variáveis booleanas para verificar:
1) Se o carro passou da velocidade
2) Se o carro está na área do radar
3) Se o carro deve ser multado

Mostre mensagens apropriadas.
"""

# velocidade = 61  # velocidade atual do carro
# local_carro = 100  # posição atual do carro

# RADAR_1 = 60  # velocidade máxima permitida
# LOCAL_1 = 100  # posição do radar
# RADAR_RANGE = 1  # alcance do radar

# Verifica se a velocidade ultrapassou o limite
# vel_carro_pass_radar_1 = velocidade > RADAR_1

# Verifica se o carro está dentro da área de alcance do radar
# carro_passou_radar_1 = (
#     local_carro >= (LOCAL_1 - RADAR_RANGE)
#     and
#     local_carro <= (LOCAL_1 + RADAR_RANGE)
# )

# Verifica se deve ser multado
# carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

# if vel_carro_pass_radar_1:
#     print("Velocidade do carro passou do radar 1")

# if carro_passou_radar_1:
#     print("Carro passou pelo radar 1")

# if carro_multado_radar_1:
#     print("Carro multado no radar 1")

"""
📌 O QUE FOI FEITO?

1) Criamos constantes em MAIÚSCULO.
2) Criamos variáveis booleanas com nomes descritivos.
3) Evitamos colocar tudo direto dentro do if.
4) Separarmos responsabilidades.

Isso reduz a complexidade cognitiva.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie um sistema que verifique se uma pessoa pode entrar
em uma festa.

IDADE_MINIMA = 18
idade_pessoa = ?

Crie uma variável booleana:
pode_entrar

Mostre a mensagem apropriada.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Sistema de limite de banco.

LIMITE_SAQUE = 500
saldo = ?
valor_saque = ?

Crie variáveis booleanas que verifiquem:

1) Se o valor do saque é menor ou igual ao limite
2) Se o saldo é suficiente
3) Se o saque pode ser realizado

Mostre mensagens apropriadas.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Sistema de controle de temperatura industrial.

TEMP_MAXIMA = 80
TEMP_MINIMA = 10
temperatura_atual = ?

Crie verificações booleanas para:

1) Temperatura acima do máximo
2) Temperatura abaixo do mínimo
3) Temperatura dentro da faixa segura

Mostre mensagens apropriadas.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Sistema com DOIS radares.

RADAR_1 = 60
LOCAL_1 = 100

RADAR_2 = 80
LOCAL_2 = 200

RADAR_RANGE = 2

Dado:
velocidade
local_carro

Crie todas as variáveis booleanas necessárias para:
- Detectar passagem no radar 1
- Detectar passagem no radar 2
- Detectar multa em cada radar

Organize o código de forma limpa e legível.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# IDADE_MINIMA = 18  # constante com idade mínima
# idade_pessoa = 20  # exemplo de idade

# pode_entrar = idade_pessoa >= IDADE_MINIMA  # verifica se atende à regra

# if pode_entrar:
#     print("Pode entrar na festa")
# else:
#     print("Não pode entrar na festa")


# Exercício 2 - Médio

# LIMITE_SAQUE = 500  # limite máximo permitido por saque
# saldo = 1000  # saldo disponível
# valor_saque = 400  # valor desejado

# saque_dentro_limite = valor_saque <= LIMITE_SAQUE  # verifica limite
# saldo_suficiente = saldo >= valor_saque  # verifica saldo
# saque_autorizado = saque_dentro_limite and saldo_suficiente  # validação final

# if saque_autorizado:
#     print("Saque realizado com sucesso")
# else:
#     print("Saque não autorizado")


# Exercício 3 - Difícil

# TEMP_MAXIMA = 80  # limite superior
# TEMP_MINIMA = 10  # limite inferior
# temperatura_atual = 50  # exemplo

# acima_maximo = temperatura_atual > TEMP_MAXIMA  # verifica excesso
# abaixo_minimo = temperatura_atual < TEMP_MINIMA  # verifica mínimo
# dentro_faixa = not acima_maximo and not abaixo_minimo  # faixa segura

# if acima_maximo:
#     print("Temperatura acima do permitido")
# elif abaixo_minimo:
#     print("Temperatura abaixo do permitido")
# elif dentro_faixa:
#     print("Temperatura dentro da faixa segura")


# Exercício 4 - Difícil

# RADAR_1 = 60
# LOCAL_1 = 100

# RADAR_2 = 80
# LOCAL_2 = 200

# RADAR_RANGE = 2

# velocidade = 85
# local_carro = 200

# passou_vel_radar_1 = velocidade > RADAR_1
# passou_area_radar_1 = (
#     local_carro >= (LOCAL_1 - RADAR_RANGE)
#     and
#     local_carro <= (LOCAL_1 + RADAR_RANGE)
# )
# multado_radar_1 = passou_vel_radar_1 and passou_area_radar_1

# passou_vel_radar_2 = velocidade > RADAR_2
# passou_area_radar_2 = (
#     local_carro >= (LOCAL_2 - RADAR_RANGE)
#     and
#     local_carro <= (LOCAL_2 + RADAR_RANGE)
# )
# multado_radar_2 = passou_vel_radar_2 and passou_area_radar_2

# if multado_radar_1:
#     print("Multado no radar 1")

# if multado_radar_2:
#     print("Multado no radar 2")
