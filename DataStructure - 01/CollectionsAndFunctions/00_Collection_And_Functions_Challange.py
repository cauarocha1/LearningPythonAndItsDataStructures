# Le a linha de lancamentos do stdin
entrada = input().strip()

# Inicialize o saldo do dia
saldo = 0.0

# Divide os lancamentos pela virgula
lancamentos = entrada.split(',')

for lancamento in lancamentos:
    tipo, valor = lancamento.strip().split()
    valor = float(valor)
    saldo += valor if tipo == 'R' else -valor

# Imprima o saldo final com duas casas decimais
print(f"{saldo:.2f}")
