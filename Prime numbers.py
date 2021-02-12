#  Prime Numbers

def isPrime(number):
    i = 2
    count = 2
    while(i <= number/2):
        if(number % i == 0) : count+=1
        i+=1
    if(count >= 3) : return False
    return True

print(isPrime(16))