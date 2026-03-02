soma = 0
for i in range(50, 4, -1):
    if i % 2 != 0:
        print(i)
    soma += i
print(f"soma total é de:", soma)