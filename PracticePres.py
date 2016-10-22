
def isPrime(n):
    '''Returns whether n is prime.'''
    if n < 2:
        return False

    for x in range(2, n // 2):
        if n % x == 0:
            return False
    return True


def generatePrimes(n):
    primes = []
    primesUnderN = []
    total = 0
    for x in range(n):
        if isPrime(x):
            primes.append(x)
            total += 1
        primesUnderN.append(total)
    return primes, primesUnderN


def plotPrimes(n):
    import matplotlib.pyplot as plt
    from io import BytesIO

    primes, primesUnderN = generatePrimes(n)

    plt.close()

    plt.xlabel("N")
    plt.ylabel("Primes under N")

    plt.scatter(primes, primes, color='red')
    plt.plot(primesUnderN, color='blue')

    plt.xlim(0, n - 1)
    plt.ylim(ymin=0)

    bitsAndBytes = BytesIO()

    plt.savefig(bitsAndBytes, format="png")

    bitsAndBytes.seek(0)

    return bitsAndBytes

# plotPrimes(5001)
