import json
import ply.lex as lex

with open('stock.json', 'r') as json_file:
    produtos = json.load(json_file)["stock"]

tokens = (
    'OPERATION',
    'COIN',
    'ID',
    'COMMA',
    'POINT'
)

t_COMMA = r','
t_ignore = ' \t'

SALDO = 0.0
insert_coin = False
insert_product = False 

def process_product_selection(selected_product_id):
    global SALDO
    product_found = False
    for produto in produtos:
        if selected_product_id == produto['cod'] and SALDO >= produto['preco']:
            print(f"Pode retirar o produto dispensado {produto['nome']}")
            produto['quant'] -= 1
            SALDO -= produto['preco']
            print(f"Saldo = {SALDO:.2f}")  # Arredondamento para duas casas decimais
            return
        elif selected_product_id == produto['cod']:
            product_found = True
    if not product_found:
        print("Produto não encontrado.")


def process_coin_insertion(coin_value):
    global SALDO
    if coin_value.endswith('e'):
        SALDO += float(coin_value[:-1])
    else:
        SALDO += float(coin_value[:-1]) * 0.01
    print(f"Saldo atual = {SALDO:.2f}")  # Arredondamento para duas casas decimais

def process_operation(operation):
    global insert_coin, insert_product

    if operation == 'LISTAR':
        print("cod | nome | quantidade | preço")
        print("---------------------------------")
        for produto in produtos:
            print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']:.2f}")  # Arredondamento para duas casas decimais
    
    if operation == 'MOEDA':
        insert_coin = True
        insert_product = False  

    if operation == 'SELECIONAR':
        insert_product = True
        insert_coin = False 

def t_ID(t):
    r'[A-Z]\d+'
    if insert_product:
        process_product_selection(t.value)

def t_OPERATION(t):
    r'\b[A-Z]+\b'
    process_operation(t.value)

def t_POINT(t):
    r'\.'
    print(f"Saldo = {SALDO:.2f}")  # Arredondamento para duas casas decimais

def t_COIN(t):
    r'\d+[ec]'
    if insert_coin:
        process_coin_insertion(t.value)

def t_error(t):
    print("Caractere inválido '%s'" % t.value[0])
    t.lexer.skip(1)

#ler
lexer = lex.lex()

def read_input(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break

# Print de boas-vindas
print("Bem-vindo à Máquina de Venda!")

while True:
    user_input = input(">> ")
    if user_input == "SAIR":
        #Print de despedida
        print("Obrigado por usar a Máquina de Venda!")
        break
    read_input(user_input)
