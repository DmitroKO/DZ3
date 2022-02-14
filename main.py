x = input("Ввидите текст:")
x = int(x)
left, right = divmod(x, 10000)
x1 = left
x = right
left, right = divmod(x, 1000)
x2 = left
x = right
left, right = divmod(x, 100)
x3 = left
x = right
left, right = divmod(x, 10)
x4 = left
x = right
left, right = divmod(x, 1)
x5 = left
print(x5 * 10000 + x4 * 1000 + x3 * 100 + x2 * 10 + x1 * 1)