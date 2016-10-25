
i = 1
n = 10000

def findPrime(i, n):
    # count starts at 1 because 2 is the first prime
    count = 1
    while i < n:
        i = i + 2 # Generate odd numbers greater than 1
        j = 1 # Start j at 1 as prime can be divisible by 1 and itself
        prime = True
        while j < n:
            j = j + 1
            # if the remainder is 0 candidate is not a prime and can exit check
            if i != j and i % j == 0:
                prime = False
                break
        # If the candidate comes out of the loop still prime increment the counter
        if prime is True:
            count = count + 1
            if count == 1000:
                return i
                break


print str(findPrime(i, n)) + ' is the 1000th prime'
