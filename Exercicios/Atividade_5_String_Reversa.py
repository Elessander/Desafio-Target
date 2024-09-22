def inverter_string(string):
    invertida = ""
    for i in range(len(string) - 1, -1, -1):
        invertida += string[i]
    return invertida

entrada = input("Digite uma string: ")
print(f"String invertida: {inverter_string(entrada)}")
