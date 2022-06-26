"""
recebendi dados do usuário

Imput() --> Todo dado recebido vida inpu é do tipo string

em Python, string é tudo que estiver entre:
--aspas simples :
- Aspas duplas:
- Aspas simples triplas:
- Aspas duplas triplas:
"""
"""
Exemplos 
- Aspas simples -> 'Angelina Joeli' 
- Aspas duplas -> "Angelina Joeli"
- Aspas simples triplas '''Angelina Joeli'''    - Aspas duplas triplas """


# Entrada de dados

print('qual seu nome?')
nome = input()  #Input -> entrada
# Exemplo antigo 2. x
# print('seja bem vindo(a) %s' % nome)
# Exemplo de print moderno 3 print('seja bem-vindo(a) {0}'. format(nome))
#Exemplo de print Atual
print(f'seja bem-vindo(a) {nome}')
print("Qual a sua idade?")

idade = input()

# Processamento

# Saída de dados
# Exemplo antigo 2.X print("O (a) %s tem, %s anos" % (nome, idade))
print(F'A {nome} tem {idade} anos ')

"""
# int(idade) ==> cast
Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'A {nome} nasceu em {2022 - int(idade)}')