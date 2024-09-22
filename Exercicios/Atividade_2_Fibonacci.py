def fibonacci(n):
    fib1, fib2 = 0, 1
    while fib1 < n:
        fib1, fib2 = fib2, fib1 + fib2
    return fib1 == n

numero = int(input("Informe um número: "))

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
