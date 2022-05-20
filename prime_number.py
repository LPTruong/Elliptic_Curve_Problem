


# Kiểm tra số nguyên tố
def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True