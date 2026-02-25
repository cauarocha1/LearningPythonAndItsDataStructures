# Leitura da linha de identificadores de transações
entrada = input()

# TODO: Crie uma lista com as transações sem duplicatas, mantendo a ordem da primeira ocorrência
lista_transacoes = entrada.split()

resultado = []

for transacao in lista_transacoes:
    if transacao not in resultado:
        resultado.append(transacao)
    
print(' '.join(resultado))

#LearningPythonAndItsDataStructures