def nok(a, b):
    for i in range(1, a*b+1):
        if i%a == 0 and i%b == 0:
            print(f'Общее кратное: {i}')
            break

nok(2, 4)
nok(2, 5)
nok(3, 2)
nok(2, 9)
