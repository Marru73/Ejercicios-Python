def generapares(limite):
    num = 1

    while num<limite:
        yield num * 2
        num += 1
        
devuelvePares = generapares(10)

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))