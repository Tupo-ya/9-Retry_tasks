def is_easy(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    return flag


n = 15

easy_nums = []
for i in range(1, n+1):
    if is_easy(i):
        easy_nums.append(i)

print(easy_nums)
