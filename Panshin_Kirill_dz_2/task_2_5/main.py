price = [18.4, 35.28, 50.47, 15.55, 78.2, 30.89, 40.41, 90.36, 110.85, 60.47, 25.52, 20.3, 35.58,
         20.62, 130.11, 70.82, 60.34, 30.02, 80.47, 67.32]
price[4] = 78.02
price[11] = 20.03
for i in range(0, len(price)):
    num = price[i]
    r = int((price[i] * 100) // 100)
    kk = int((price[i] * 100) % 100)
    num = str(num)
    sym = num[-2:]
    sym = sym[0]
    if kk < 10 and sym != 0:
        num = num * 100
        num = str(num)
        kk = num[-2:]
    print(f'{r} руб {kk} коп', end=", ")
print(price)
price = sorted(price)
print(price)
print(price[:5])
price = sorted(price, reverse=True)
print(price)

