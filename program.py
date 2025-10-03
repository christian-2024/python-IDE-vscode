def saudacao(name):
    return f"Saudação, {name}! Meu primeiro projeto está rodando naturalmente."

def calcular_imposto(salario):
    aliquota = 0.00
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05
    return aliquota * salario

valor_salario = float(input())
valor_beneficios = float(input())

valor_imposto = calcular_imposto(valor_salario)

saida = valor_salario - valor_imposto + valor_beneficios
usuario = input("Qual o seu nome? ")
mensagem = saudacao(usuario)
print(mensagem)
print(f'{saida:.2f}')

