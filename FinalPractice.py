import matplotlib.pyplot as plt


def isPrime(n):
    '''returns whether n is prime.'''
    if n < 2:
        return False

    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def listPrimes(n):
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
    primes, primesUnderN = listPrimes(n)
    plt.xlabel("N")
    plt.ylabel("Primes Under N")

    plt.plot(primesUnderN, color='blue')
    plt.scatter(primes, primes, color='red', marker='*')

    plt.xlim(0, n)
    plt.ylim(ymin=0)

    plt.savefig("T.Hacks!!!.png", type="png")
plotPrimes(50)
