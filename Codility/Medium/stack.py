def trans_string(S):
    stack = []
    for char in S:
        if stack and ((char == 'B' and stack[-1] == 'A') or (char == 'A' and stack[-1] == 'B') or (char == 'C' and stack[-1] == 'D') or (char == 'D' and stack[-1] == 'C')):
            stack.pop()
        else:
            stack.append(char)
    ans = ''.join(stack)
    return ans

a
sum = 0
for i in len(a)
    for i+1 in len(a):
        if i != i+1 
            sum + 1
        elif is == 
            sum = 0
            
(CBACsssD)
print(trans_string('CBACD'))      # 輸出: 'C'
print("------")
print(trans_string('CABABD'))     # 輸出: ''
print("------")
print(trans_string('ACBDACBD'))   # 輸出: 'ACBDACBD'
print("------")
print(trans_string('BCBCD'))   # 輸出: 'ACBDACBD'
# 這個算法的時間複雜度是O(n)，其中n是字符串S的長度。這是因為我們只遍歷字符串一次，並且堆疊操作(push和pop)的時間複雜度都是O(1)。