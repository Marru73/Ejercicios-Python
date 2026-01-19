
def fibonacci_lista(limite):
    fib = [0, 1]
    
    while fib[-1] + fib[-2] < 1000:
        fib.append(fib[-1] + fib[-2])

    return fib

print(fibonacci_lista(1000))


"""
while True:
    k = fibonacci[i] + fibonacci[j]

    if k >= 1000:
        print(fibonacci)
        break
    else:
        fibonacci.append(k)
        i += 1
        j += 1
"""