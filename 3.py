divisors = []

n = 12

for i in range(1, n+1):
    if n%i==0:
        divisors.append(i)

print(f'Всего: {len(divisors)}\nДелители: {divisors}')