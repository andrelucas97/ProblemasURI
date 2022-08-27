a = []

x = input()

for i in x.split():
    a.append(float(i))

areaT = (a[0] * a[2]) / 2
areaC = 3.14159 * a[2]**2
areaTz = ((a[0]+a[1])*a[2]) / 2
areaQ = a[1]**2
areaR = a[0]*a[1]

print('TRIANGULO: %.3f' % areaT)
print('CIRCULO: %.3f' % areaC)
print('TRAPEZIO: %.3f' % areaTz)
print('QUADRADO: %.3f' % areaQ)
print('RETANGULO: %.3f' % areaR)
