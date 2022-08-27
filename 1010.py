a = []
b = []

x = input()
y = input()

for i in x.split():
    a.append(float(i))
for j in y.split():
    b.append(float(j))

totalPago = (a[1]*a[2]) + (b[1]*b[2])

print('VALOR A PAGAR: R$ %.2f' % totalPago)
