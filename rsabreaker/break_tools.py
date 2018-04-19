def prime_factors_to_list(int_to_factors):
    factor_rest = int_to_factors
    prime_factor_list = [[0, 0]]
    while factor_rest != 1:
        divisor = 2
        for i in range(2, factor_rest + 1):
            if factor_rest % i == 0:
                divisor = i
                break
        factor_rest //= divisor
        is_in_list = False
        for i in range(0, len(prime_factor_list)):
            if prime_factor_list[i][0] == divisor:
                is_in_list = True
                prime_factor_list[i][1] += 1
                break
        if not is_in_list:
            prime_factor_list.append([divisor, 1])
    return prime_factor_list


def phi(a):
    prime_list = prime_factors_to_list(a)
    result = 1
    for i in range(1,len(prime_list)):
        result *= (prime_list[i][0] ** (prime_list[i][1] - 1)) * (prime_list[i][0] - 1)
    return result


def euclidean_algorithm(n, m):
    if n == 0 or m == 0:
        print("Numbers have not be equal to 0!")
    start_a = m
    start_b = n

    if start_b < 1:
        start_b *= -1

    if start_a < 1:
        start_a *= -1

    result_list = None
    if start_a > start_b:
        result_list = [[start_a, start_a // start_b, start_b, start_a % start_b]]
    else:
        result_list = [[start_b, start_b // start_a, start_a, start_b % start_a]]

    while result_list[-1][2] != 1 and result_list[-1][3] != 0:
        a = result_list[-1][2]
        b = result_list[-1][3]
        c = result_list[-1][2] % result_list[-1][3]
        result_list.append([a, a // b, b, c])
    return result_list


def extended_euclidean_algorithm(euclidean_list):
    ls = list(euclidean_list)
    ls.__delitem__(-1)
    ls = list(reversed(ls))
    ld = [[1, ls[0][0], ls[0][1], ls[0][2]]]

    for i in range(1, len(ls)):
        if i % 2 == 1:
            r = ld[i - 1][2] * ls[i][1]
            y = ld[i - 1][0] + r
            d = ld[i - 1][1]
            x = ld[i - 1][2]
            a = ls[i][0]
            ld.append([y, d, x, a])
        else:
            r = ld[i - 1][0] * ls[i][1]
            y = ld[i - 1][0]
            d = ls[i][0]
            x = ld[i - 1][2] + r
            a = ld[i - 1][3]
            ld.append([y, d, x, a])

    ld[-1][2] *= -1
    return ld


if __name__ == "__main__":

    el = euclidean_algorithm(3917, 9792)
    print(el)
    invert_list = extended_euclidean_algorithm(el)
    print(invert_list)
