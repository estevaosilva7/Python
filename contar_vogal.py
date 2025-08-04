def contar_vogal(texto):
    vogais = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "â", "ê", "ô", "ã", "õ"]
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

entrada = input("Digite uma frase: ")
total = contar_vogal(entrada)
print("Número de vogais é:", total)
