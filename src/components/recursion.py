
import time

def factorial(n):

# 0! = 1
# 1! = 1
# 5! = 5 x 4 x 3 x 2 x 1


    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
#5 * f(4)
#5 x 4 x f(3)
#5 x 4 x 3 * f(2)
#5 x 4 x 3 x 2 x f(1)
#5 x 4 x 3 x 2 x 1 x f(0) aka 1


print(factorial(5))


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib (n-2)
    

start_time = time.time()
print(fib(20))
end_time = time.time()
print("Time taken:", end_time - start_time)

    


def fibo(n, memo={}):
    #1 1 2 3 5 8

    #find fib by adding (n-1) + (n-2)

    #base case is 0 when n = 0 and 1 when n = 1

    if n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibo_num = fibo(n-1, memo) + fibo (n-2, memo)
        memo[n] = fibo_num
        return fibo_num

start_time = time.time()
print(fib(20))
end_time = time.time()
print("Time taken:", end_time - start_time)

    