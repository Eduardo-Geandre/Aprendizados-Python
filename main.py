from datetime import date

current_date = date.today()

data_nascimento= int(input("Ano de nascimento:"))
data_actual = current_date.year
idade =data_actual-data_nascimento

print(idade)

if idade <=18:
    print('Voce é menor de idade, não pode entrar')

else:
    print('Voce é de maior, boa festa')
    print('Bem vindo a festa xx')


