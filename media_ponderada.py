materias = {}


# Adicionando matérias, notas e pesos
r = "sim"
while r == "sim":
    r = input("Deseja adicionar uma nova matéria? (sim/não): ")
    if r == "sim":
        print("Ótimo, vamos adicionar uma nova matéria.")
        nome_materia = input("Digite o nome da nova matéria: ")
        nota_materia = int(input("Digite a nota da nova matéria: "))
        peso_materia = int(input("Digite o peso da nova matéria: "))
        materias[nome_materia] = (nota_materia, peso_materia)
    elif r == "não":
        print("Tudo bem, vamos calcular a média ponderada com as matérias atuais.")
    else:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
     

# Exibindo as matérias adicionadas, juntamente com seus respectivos pesos e notas     
n = 0
while n < len(materias):
        print("==================================================================")
        for materia, (nota, peso) in materias.items():
            n += 1
            print(f"Matéria: {materia}, Nota: {nota}, Peso: {peso}")


# Função para calcular a média ponderada
def media_ponderada(materias):
    part_1 = sum(nota * peso for nota, peso in materias.values())
    part_2 = sum(peso for _, peso in materias.values())
    resultado = part_1 / part_2 if part_2 != 0 else 0
    return resultado


# Armazenando o resultado da média ponderada e exibindo-o para o usuário
resultado = media_ponderada(materias)
print(f"A média ponderada de suas notas é {round(resultado, 2)}")