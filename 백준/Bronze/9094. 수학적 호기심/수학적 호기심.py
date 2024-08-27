from itertools import combinations

if __name__ == "__main__":

    case_number = int(input())
    def count_valid_pairs(n, m):
        count = 0
        for combo in combinations(range(1,n), 2):
            numerator = combo[0]**2 + combo[1]**2 + m
            mother = (combo[0] * combo[1])
            if numerator % mother == 0:
                count += 1
        print(count)

    for _ in range(case_number):
        l = list(map(int, input().split()))
        count_valid_pairs(l[0], l[1])