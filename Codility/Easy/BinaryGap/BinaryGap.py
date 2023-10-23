

def solution(N):
    # 將N轉為二進制並去除開頭的'0b'
    binary_representation = bin(N)[2:]
    # 初始設定最大間隔為0
    max_gap = 0
    # 初始設定目前間隔為0
    current_gap = 0
    
    for bit in binary_representation:
        if bit == '1':
            # 若遇到1，則檢查目前間隔是否大於最大間隔
            if current_gap > max_gap:
                max_gap = current_gap
            # 重置目前間隔
            current_gap = 0
        else:
            # 若遇到0，則間隔+1
            current_gap += 1
    return max_gap


# show test_cases
print(solution(9))
print(solution(529))