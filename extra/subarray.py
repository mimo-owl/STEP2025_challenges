import math, random

# Problem: L is an array of integers. K is an integer (1 <= K <= len(L)).
# Find a subarray of L such that 1) the length of the subarray is equal to or
# larger than K, and 2) the sum of the elements in the subarray is maximized.
#
# For example, if L is [2, -1, -1, -1, 4, -1, 3, 1] and K=3, the subarray
# [4, -1, 3, 1] maximizes the sum and the sum is 7.
#
# Input: L and K
# Output: The maximum sum

# [, 6, 7, 3, 4, 1]

# O(N^3) algorithm
def solve_n3(L, K):
    N = len(L)
    max_sum = -math.inf
    for k in range(K, N + 1):
        for i in range(0, N - k + 1):
            sum = 0
            for j in range(i, i + k):
                sum += L[j]
            max_sum = max(max_sum, sum)
    return max_sum


# O(N^2) algorithm
def solve_n2(L, K):
    N = len(L) # [1, 2, 3], K = 2, maxSum = 5
    #-----------------------#
    # Write your code here! #
    #-----------------------#
    curSum = sum(L[0:K]) # sum of [1, 2] = 3
    maxSum = curSum # 3
    # 左端を動かしていく
    for l in range(N - K + 1): # 3 - 2 + 1 = 2
        curSum = sum(L[l:l + K]) # 初期値として長さKの部分和
        maxSum = max(maxSum, curSum)
        # print(f"True: curSum = {curSum}, maxSum = {maxSum}, l = {l}, r = {l + K - 1}")
        # 右に伸ばしていく
        for r in range(l+K, N):
            curSum += L[r]
            maxSum = max(maxSum, curSum)
            # print(f"True: curSum = {curSum}, maxSum = {maxSum}, l = {l}, r = {r}")
    return maxSum


# O(N) algorithm
def solve_n(L, K):
    N = len(L) # 3
    #-----------------------#
    # Write your code here! #
    #-----------------------#

    # [1, 2, 3], K = 2

    l = 0 # 1
    r = K # 3
    curSum = sum(L[l:r]) # curSumを初期化。ここでは index r の値は和に含まれない。あとで足すので。 # sum of [1, 2] = 3
    maxSum = curSum # 3
    # print(f"curSum = {curSum}, maxSum = {maxSum}, l = {l}, r = {r-1}")

    # 左側を動かしていく
    while l < N - K + 1: # 3 - 2 + 1 = 2
        # 処理：右側が範囲外になるまで動かして和を見ていく

        # 右側が範囲外になった場合
        if r >= N: # r = 3
            l += 1 # 左側を更新
            r = min(N - 1, l + K - 1) # 右側は、更新された左側から測って長さKの位置に更新

            if l < N - K + 1:
                curSum = sum(L[l:r]) # curSumを初期化。l60と同様の理由で、rの値は和に含まれない。
            continue

        # 右側が範囲内の場合
        curSum += L[r] # 5
        maxSum = max(maxSum, curSum) # 5
        # print(f"curSum = {curSum}, maxSum = {maxSum}, l = {l}, r = {r}")
        r += 1 # 3 # 右側を１つ右に進める

    return maxSum


# For a given L and K, run the three algorithms (O(N^3), O(N^2) and O(N))
# and check that all the answers are equal.
def check_answers(L, K):
    answer_n3 = solve_n3(L, K)
    answer_n2 = solve_n2(L, K)
    answer_n = solve_n(L, K)
    if answer_n3 != answer_n2:
        print(L, K)
        print("Correct answer is %d but the O(N^2) algorithm answered %d" % (
            answer_n3, answer_n2))
        exit(0)
    if answer_n3 != answer_n:
        print(L, K)
        print("Correct answer is %d but the O(N) algorithm answered %d" % (
            answer_n3, answer_n))
        exit(0)


# Run tests.
def run_tests():
    # Add your test cases here.
    check_answers([1, -1, -1, -1, 3, 2], 1)
    check_answers([1, -1, -1, -1, 3, 2], 2)
    check_answers([1, -1, -1, -1, 3, 2], 3)
    check_answers([1, -1, -1, -1, 3, 2], 4)
    print("Default test cases passed!")

    # Generate many test cases and run.
    for iteration in range(1000):
        length = random.randint(1, 30)
        L = [random.randint(-10, 10) for i in range(length)]
        for K in range(1, length + 1):
            check_answers(L, K)
    print("All tests pass!")


if __name__ == "__main__":
    run_tests()
