# Media ponderada

hist = int(input("Sua nota em história: "))
math = int(input("Sua nota em matemática: "))
bio = int(input("Sua nota em biologia: "))


def media_ponderada(hist_n, math_n, bio_n):
    p_hist = 6
    p_math = 9
    p_bio = 8
    part_1 = (hist_n*p_hist) + (math_n*p_math) + (bio_n*p_bio)
    part_2 = (p_hist + p_math + p_bio)
    resultado = part_1/part_2
    return resultado

resultado = media_ponderada(hist, math, bio)

print(f"A média ponderada de suas notas é {round(resultado, 2)}")