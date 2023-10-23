# Binary Gap

#### 原文 :
```markdown
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

#### 解析 :
```
題目要算出一個正整數 N 最大的 Binary Gap 若輸入超過 N 的範圍會直接回傳 0。

N的範圍大小為 [1..2,147,483,647]，最小為 1 , 最大為 2 ³¹-1

而 Binary Gap 指的就是 正整數 N用二進位表示時，被1前後夾起來裡連續為零的長度。

EX: 9，轉成二進制是 1001，在被前後兩個 1 夾起的 0 的長度是 2

所以 9 最大的 Binary Gap 就是 2。

1041的二進制是 100000010001，被 1 夾的連續零有兩段，一個是 5, 一個是 3

選最大的 Binary Gap 為 5。
```