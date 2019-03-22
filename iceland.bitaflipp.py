from itertools import combinations


def main():
    n = int(input())
    str_bits = input().split()
    bits = list(map(int, str_bits))
    count = list()
    zeros = list()
    last_count = 0
    last_bit = 1
    for i, bit in enumerate(bits):
        next_bit = bits[i + 1] if len(bits) >= i + 2 else 1
        count.append(last_count + bit)
        last_count = count[-1]
        if bit == 0 and (next_bit != 0 or last_bit != 0):
            zeros.append(len(count)-1)
        last_bit = bit
    if count[-1] == n:
        print(n - 1)
        return
    elif count[-1] == n - 1:
        print(n)
        return
    best_sum = count[-1]
    for i, j in combinations(zeros, 2):
        range_sum = count[j] - count[i]
        range_size = j - i + 1
        flipped_sum = count[-1] - range_sum - range_sum + range_size
        best_sum = max(best_sum, flipped_sum)
    print(best_sum)

main()