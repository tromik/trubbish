import math

i = 1
n = 250000
fnd = 25000

def findPrime(i, n, fnd):
    # count starts at 1 because 2 is the first prime
    count = 1
    primes = []
    logsum = 0
    while i < n:
        i = i + 2 # Generate odd numbers greater than 1
        j = 1 # Start j at 1 as prime can be divisible by 1 and itself
        prime = True
        for j in primes: # Only need to loop through primes less than the candidate
            # if the remainder is 0 candidate is not a prime and can exit check
            if i != j and i % j == 0:
                prime = False
                break
        # If the candidate comes out of the loop still prime increment the counter
        if prime:
            count = count + 1 # Increment prime counter
            primes.append(i) # Add prime to list of primes for next loop
            logsum = logsum + math.log(i)
            print 'Log sum: ' + str(logsum) + ' | Current prime: ' + str(i) + ' | Ratio: ' + str(logsum/n)
            if count == fnd:
                return i
                break

if not findPrime(i, n, fnd):
    print 'Could not reach the ' + str(fnd) + 'th prime with maximum limit of ' + str(n)
else:
    print str(findPrime(i, n)) + ' is the ' + str(fnd) + 'th prime'
