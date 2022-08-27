nome = input()
salarioFixo = float(input())
vendaReal = float(input())

total = salarioFixo + (0.15 * vendaReal)

print('TOTAL = R$ %.2f' % total)
