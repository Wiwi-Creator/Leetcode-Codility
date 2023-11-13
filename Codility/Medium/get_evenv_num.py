def max_even_sum(A, K):
    evens = sorted([x for x in A if x % 2 == 0], reverse=True)
    odds = sorted([x for x in A if x % 2 == 1], reverse=True)

    prefix_evens = [0] + [sum(evens[:i+1]) for i in range(len(evens))]
    prefix_odds = [0] + [sum(odds[:i+1]) for i in range(len(odds))]

    max_sum = -1
    for i in range(0, min(K, len(evens)) + 1):
        if K - i <= len(odds):
            current_sum = prefix_evens[i] + prefix_odds[K-i]
            if current_sum % 2 == 0:
                max_sum = max(max_sum, current_sum)

    return max_sum


# 測試A, K
print(max_even_sum([4, 9, 8, 2, 6], 3))  # 18
