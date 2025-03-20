# The following is an implementation of the AKS primality test, 
# a complex algorithm for determining whether a number is prime.

def is_prime_aks(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Step 1: Check if n is a perfect power
    def is_perfect_power(n):
        for b in range(2, int(n**0.5) + 1):
            a = 1
            while (a := a + 1) ** b <= n:
                if a ** b == n:
                    return True
        return False

    if is_perfect_power(n):
        return False

    # Step 2: Find the smallest r such that o_r(n) > log^2(n)
    def multiplicative_order(n, r):
        result = 1
        k = 1
        while k < r:
            result = (result * n) % r
            if result == 1:
                return k
            k += 1
        return r

    r = 2
    max_k = int((n**0.5).bit_length()**2)
    while r < n:
        if gcd(n, r) == 1 and multiplicative_order(n, r) > max_k:
            break
        r += 1

    # Step 3: Check if 1 < gcd(a, n) < n for some a <= r
    for a in range(2, r + 1):
        if 1 < gcd(a, n) < n:
            return False

    # Step 4: Check polynomial congruence
    def polynomial_congruence(n, r):
        for a in range(1, min(n, r)):
            left = (a + 1)**n % n
            right = (a**n + 1) % n
            if left != right:
                return False
        return True

    if not polynomial_congruence(n, r):
        return False

    # Step 5: If all checks pass, n is prime
    return True

# Helper function to compute gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
if __name__ == "__main__":
    number = 101
    print(f"Is {number} prime? {is_prime_aks(number)}")
