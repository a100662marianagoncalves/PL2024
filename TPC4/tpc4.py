import re

def lexer(sql_query):
    # Definindo padrões para os tokens
    patterns = [
        (r'\s+', 'SPACE'),  # Espaços em branco
        (r'SELECT', 'SELECT'),
        (r'FROM', 'FROM'),
        (r'WHERE', 'WHERE'),
        (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),  # Identificadores (ex: id, nome, salario)
        (r'>=', 'GREATER_THAN_OR_EQUAL'),
        (r'\d+', 'INTEGER'),  # Números inteiros
        (r',', 'COMMA'),
    ]

    # Criando a expressão regular combinada
    regex = '|'.join('(%s)' % pattern for pattern, _ in patterns)

    # Inicializando a posição atual
    pos = 0

    # Iterando sobre os tokens encontrados na entrada
    for match in re.finditer(regex, sql_query):
        for i, groupname in enumerate(pattern for pattern, _ in patterns):
            if match.group(i + 1):
                token_type = patterns[i][1]
                token_value = match.group(i + 1)

                # Ignorando espaços em branco
                if token_type != 'SPACE':
                    yield token_type, token_value

                # Atualizando a posição atual
                pos = match.end()
                break

# Exemplo de uso
sql_query = "SELECT id, nome, salario FROM empregados WHERE salario >= 820"
for token in lexer(sql_query):
    print(token)