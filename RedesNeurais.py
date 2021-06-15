import random

class Ent():
    def __init__(self, valor, peso):
        self.valor = int(valor)
        self.peso = dict(peso)

def custo(valorResultado, ValorDesejado):
    return round(((valorResultado - ValorDesejado) ** 2), 2)


def pesoGerado(quantiaPeso):
    pesos = {}
    for nPeso in range(quantiaPeso):
        pesos[f'Peso{nPeso}'] = round(random.random(), 2)
    return pesos


def gerarListaEntidades(quantiaEntidades, quantiaPesoXEntidade):
    entidade = []
    for nEntidade in range(quantiaEntidades):
        vars()[f'e{str(nEntidade)}'] = {
            "nome": f'Acesso {str(nEntidade)}',
            "valor": round(random.random(), 2),
            "pesos": pesoGerado(quantiaPesoXEntidade),
        }
        entidade.append(vars()[f'e{str(nEntidade)}'])
    return entidade

def soma(entidade, pes):
    print(f'Peso do Somatório escolhido = {pes}')
    constante = 0
    valorSoma = 0
    for e in entidade:
        valorSoma += e['valor'] * e['pesos'][pes]
    return round(valorSoma + constante, 2)

def listaEntidadeG(entidade):
    for item in entidade:
        print(item)
    print("\n")

def listaEntidade(entidade):
    for item in entidade:
        print(f'\n{item["nome"]}:\n valor = {item["valor"]},\n pesos = {item["pesos"]} ')
    print('\n')

def pesoAleatorio(entrada):
    return f'Peso{str(random.randint(0, len(entrada["pesos"]) - 1))}'


def pesoAleatorio(valor):
    return f'Peso{str(random.randint(0, int(valor) - 1))}'


def run():
    quantiaEntidade = 10
    quantiaPeso = 10

    print('\n')
    print(f'Acessos: {quantiaEntidade}\nPesos por entrada: {quantiaPeso}\n')
    entidade = gerarListaEntidades(quantiaEntidade, quantiaPeso)
    listaEntidade(entidade)
    somatorio = soma(entidade, pesoAleatorio(quantiaPeso))
    print(f'Valor de Ativação: {somatorio}')
    custos = custo(somatorio, 1)
    print(f'Valor de Custo: {custos}')
    print('\n')

    print(f'----------------------------------Info---------------------------------------')
    print(f'Alunos: Ivison Vinicyus Correia de Menezes,Wallas Henrique Rodrigues de Souza')
    print(f'Matriculas: 201751159681,201751151591')
    print(f'-----------------------------------------------------------------------------')

if __name__ == '__main__':
    run()