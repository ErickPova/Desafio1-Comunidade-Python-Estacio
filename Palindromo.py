def isPalindrome(typedWord):
    # Remova espaços em branco e torne a string minúscula para facilitar a comparação
    typedWord = typedWord.replace(" ", "").lower()
    reversedText = typedWord[::-1]
    
    # Compare a string original com a string invertida
    return typedWord == reversedText


questionValidation = input("Você sabe o que é um Palíndromo? (sim/não): ").lower()

if questionValidation == "sim":
    text = input("Ótimo! Agora, insira uma palavra ou frase para verificar se é um palíndromo: ")
    if isPalindrome(text):
        print(f"A palavra/frase '{text}' é um palíndromo!")
    else:
        print(f"A palavra/frase '{text}' não é um palíndromo.")
else:
    print("Irei te explicar então: \n")
    print('Um palíndromo é uma palavra, frase ou sequência que pode ser lida da mesma forma de trás para frente, ignorando espaços, pontuação e diferenciação entre maiúsculas e minúsculas. Alguns exemplos famosos incluem "Subi no ônibus", "Ame o poema" e "Anilina".')







