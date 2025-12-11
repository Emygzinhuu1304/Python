def criptografar(mensagem):
    vogais = {
        "A": "E", "E": "I", "I": "O", "O": "U", "U": "A",
        "a": "e", "e": "i", "i": "o", "o": "u", "u": "a"
    }

    resultado = ""

    for letra in mensagem:
        if letra in vogais:
            resultado += vogais[letra]
        else:
            resultado += letra

    return resultado


mensagem = input("Digite a mensagem: ")
mensagem_cripto = criptografar(mensagem)

print("Mensagem criptografada:")
print(mensagem_cripto)
