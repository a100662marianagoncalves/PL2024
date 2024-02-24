import re

def tpc3(nome_arquivo):
    soma_atual = 0
    on_ativo = False

    # Utilizamos uma expressão regular para encontrar todas as ocorrências de "ON", "OFF", "=" e números
    padrao = re.compile(r'(ON|OFF|=|\d+)')

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            # Iterar sobre todas as correspondências encontradas na linha
            for correspondencia in padrao.finditer(linha):
                comando = correspondencia.group(1)

                if comando == 'ON':
                    on_ativo = True
                elif comando == 'OFF':
                    on_ativo = False
                elif on_ativo and comando != '=':
                    soma_atual += int(comando)

                # Imprimir a soma_atual sempre que encontramos o caractere '='
                if comando == '=':
                    print(f"Soma atual: {soma_atual}")

    return soma_atual

resultado = tpc3("teste.txt")
#print(f"Soma final: {resultado}")