primes = []
primesUnderN = []
largestN = 2


def sqrt(n):
    '''Returns the integer square root of a number.'''
    return int(n**.5)


def isPrime(n):
    '''Checks whether or not a number is prime.'''
    if n < 2:
        return False

    for x in range(2, sqrt(n) + 1):
        if n % x == 0:
            return False

    return True


def populatePrimes(num):
    '''calculates new prime numbers and adds them to the memoized list.'''
    global primes
    global primesUnderN
    global largestN
    total = largestN
    for x in range(largestN, num):
        if isPrime(x):
            total += 1
            primes.append(x)
        primesUnderN.append(total)
    largestN = num


def plotPrimes(num):
    '''plots prime numbers from 0 to num on a graph and returns a bytestream'''
    import matplotlib.pyplot as plt
    from io import BytesIO
    global primes
    global primesUnderN
    global largestN

    plt.close()

    plt.xlabel("N")
    plt.ylabel("Primes under N")

    if num > largestN:
        print("Processing primes from {} to {}".format(largestN, num))
        populatePrimes(num)
        plt.plot(primesUnderN, color='blue', label="Number of Primes")
        plt.scatter(primes, primes, color='red', label="Primes")
    else:
        print("Memoized!")
        plt.plot(primesUnderN[:num], color='blue', label="Primes", linestyle='dashed')

        primeSlice = [x for x in primes if x <= num]
        plt.scatter(primeSlice, primeSlice, color='red', label="Highest Prime", marker='*')

    plt.legend(loc='upper left')

    plt.xlim(0, num)
    plt.ylim(ymin=0)

    bitsAndBytes = BytesIO()

    plt.savefig(bitsAndBytes, format="png")
    bitsAndBytes.seek(0)

    return bitsAndBytes
