'''
Flag (Bandeira) - Marcar um local
Nome = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade

'''

# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo")
else:
    print("Não faça algo")

if passou_no_if is None:
    print("Não passou no if")
else:
    print("Passou no if")


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# FLAG (BANDEIRA), NONE, IS, IS NOT E ID
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
Flag marca estado.
None marca ausência.
is compara identidade.
== compara valor.
id mostra identidade.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
📌 O que é uma FLAG (Bandeira)?

Uma "flag" é uma variável usada para marcar um estado.
Normalmente usamos valores booleanos (True ou False).

Exemplo mental:
condicao = False

Se algo acontecer:
condicao = True

Ela serve para indicar se algo ocorreu ou não.


📌 O que é None?

None significa "ausência de valor".
Não é 0.
Não é False.
Não é string vazia.
É um tipo especial que indica que a variável não aponta para nenhum valor ainda.

Exemplo:
passou_no_if = None

Isso significa:
"Ainda não sabemos se passou no if."


📌 Diferença entre == e is

==  → Compara VALOR
is  → Compara IDENTIDADE (mesmo objeto na memória)

Exemplo:
a = 10
b = 10

a == b → True (mesmo valor)
a is b → Pode ser True ou False dependendo da otimização

Já com None:
Sempre use:

variavel is None
variavel is not None

Nunca use:
variavel == None  ❌


📌 Função id()

id(variavel) mostra o endereço (identidade) do objeto na memória.
É como perguntar:
"Quem você é na memória do Python?"


📌 Entendendo o seu código

Você criou:

condicao = False
passou_no_if = None

Depois:

if condicao:
    passou_no_if = True

Como condicao é False,
o bloco do if não executa.

Logo:
passou_no_if continua sendo None.

Depois você verifica:

if passou_no_if is None:

Ou seja:
"Se nunca entrou no if, então mostre que não passou."

Isso é um exemplo clássico de uso de flag com None.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um programa que:

1) Comece com a variável status = None
2) Se a idade for maior ou igual a 18, status vira True
3) Caso contrário, permanece None
4) Depois informe se a pessoa foi aprovada na verificação
"""

# idade = 20                         # Define a idade
# status = None                      # Inicializa a flag como None

# if idade >= 18:                    # Verifica se idade é maior ou igual a 18
#     status = True                  # Marca que passou na condição

# if status is None:                 # Verifica se nunca entrou no if
#     print("Não aprovado")          # Se ainda é None, não passou
# else:
#     print("Aprovado")              # Caso contrário, passou

"""
Explicação do código resolvido:

1) status começa como None (ainda não sabemos o resultado)
2) Se idade >= 18, mudamos status para True
3) Se não entrar no if, status continua None
4) Depois usamos "is None" para verificar identidade
5) Isso garante uma checagem segura e correta
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Crie uma variável chamada encontrou.
Ela deve começar com None.

Se numero for igual a 10, marque encontrou como True.
Depois informe se encontrou ou não usando "is None".
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie duas variáveis:

a = 100
b = 100

Mostre:
1) O id de cada uma
2) Se a == b
3) Se a is b

Explique nos comentários a diferença entre igualdade e identidade.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie uma variável chamada login_autorizado = None.

Se usuario for "admin" e senha for "1234",
marque login_autorizado como True.

Depois verifique usando:
if login_autorizado is None

Explique por que é mais seguro usar "is None"
do que "== None".
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Simule um sistema onde:

1) pagamento_confirmado começa como None
2) Se valor_pago >= valor_total, marque como True
3) Se não pagar o suficiente, continue None
4) No final informe:
   - "Pagamento confirmado"
   - "Pagamento pendente"

Use corretamente a verificação com is None.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# numero = 10                        # Define o número
# encontrou = None                   # Inicializa a flag

# if numero == 10:                   # Verifica igualdade de valor
#     encontrou = True               # Marca que encontrou

# if encontrou is None:              # Verifica identidade com None
#     print("Não encontrou")         # Se ainda for None
# else:
#     print("Encontrou")             # Caso contrário


# Exercício 2 - Médio

# a = 100                            # Cria variável a
# b = 100                            # Cria variável b

# print(id(a))                       # Mostra identidade de a
# print(id(b))                       # Mostra identidade de b

# print(a == b)                      # Compara valores (igualdade)
# print(a is b)                      # Compara identidade (mesmo objeto)

# == verifica se os valores são iguais
# is verifica se apontam para o mesmo local na memória


# Exercício 3 - Difícil

# usuario = "admin"                  # Define usuário
# senha = "1234"                     # Define senha
# login_autorizado = None            # Inicializa flag

# if usuario == "admin" and senha == "1234":  # Verifica credenciais
#     login_autorizado = True                 # Marca autorização

# if login_autorizado is None:       # Verificação segura de ausência
#     print("Acesso negado")
# else:
#     print("Acesso permitido")

# Usar "is None" é mais seguro porque None é um objeto único.
# Estamos verificando identidade, não apenas valor.


# Exercício 4 - Difícil

# valor_total = 100                  # Valor esperado
# valor_pago = 80                    # Valor informado
# pagamento_confirmado = None        # Inicializa flag

# if valor_pago >= valor_total:      # Verifica pagamento suficiente
#     pagamento_confirmado = True    # Marca confirmação

# if pagamento_confirmado is None:   # Verifica se não confirmou
#     print("Pagamento pendente")
# else:
#     print("Pagamento confirmado")
