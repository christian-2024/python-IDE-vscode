def saudacao(name):
    return f"Saudação, {name}! Meu primeiro projeto está rodando naturalmente."

def calcular_imposto(salario):
    aliquota = 0.00
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05
    elif (salario >= 1100 and salario <= 2500):
        aliquota = 0.10
    else:
        aliquota = 0.15
    return aliquota * salario

print("Qual valor do salário:")
valor_salario = float(input())

print("Qual valor do Beneficio: ")
valor_beneficios = float(input())

valor_imposto = calcular_imposto(valor_salario)

saida = valor_salario - valor_imposto + valor_beneficios
usuario = input("Qual o seu nome? ")
mensagem = saudacao(usuario)
print(mensagem)
print(f'{saida:.2f}')

