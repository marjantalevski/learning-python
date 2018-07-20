def fibonacci_generator(n):
    i = 1
    nth = 1
    previous_value = 0
    store = 0
    fib = []
    while i <= n:
        fib.append(nth)
        store = previous_value
        previous_value = nth
        nth = store + nth
        i += 1
    return fib

try:        
    index = int(input("Enter the index of the last Fibonacci sequence number you want: "))
    print(fibonacci_generator(index))
except: 
    print("INVALID INPUT")
