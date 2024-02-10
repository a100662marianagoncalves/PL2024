import sys

csv = sys.stdin.read().splitlines()

modalidades = set()
aptos = 0
inaptos = 0
atletas = len(csv) - 1
escaloes_etarios = {}


for linha in csv[1:]:
    dados = linha.split(',')
    modalidade = dados[8].lower()
    aptidao = dados[12]
    idade = int(dados[5])

    modalidades.add(modalidade) 

    if aptidao == 'true':
        aptos += 1
    else:
        inaptos += 1

    escalao_etario = (idade // 5) * 5
    escaloes_etarios[escalao_etario] = escaloes_etarios.get(escalao_etario, 0) + 1

modalidades_ordenadas = sorted(modalidades)
print('Modalidades:', modalidades_ordenadas)
print('Percentagem de atletas aptos:', aptos / atletas * 100, '%')
print('Percentagem de atletas inaptos:', inaptos / atletas * 100, '%')
print('Distribuição de atletas por escalão etário:')
for escalao, quantidade in sorted(escaloes_etarios.items()):
    print(f'{escalao}-{escalao + 4}: {quantidade} atletas')
