a = []
x = input()

for i in x.split():
    a.append(int(i))

maior = a[0]
for j in range(1, len(a)):
    if a[j] > a[j-1]:
        maior = a[j]
print('%i eh o maior:' % maior)
