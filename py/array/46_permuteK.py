# import sys

# 输入n,k, 1到n全排列中，求第k个序列
# class Solution:
# seq_list返回的最终序列列表，seq当前序列列表
def back_track(seq_list, step, seq, n):
    if step == n:
        seq_list.append(''.join(map(str, seq.copy())))
        print(seq_list)
        return
    # 关键点2
    for i in range(1, n+1):
        if i not in seq:
            seq.append(i)
            back_track(seq_list, step+1, seq, n)
            seq.pop()


def k_in_n(n, k):
    # 1. 初始化及特殊处理
    seq_list = []
    n_list = [i+1 for i in range(n)]
    seq = []
    # 关键点1
    step = 0


    # 2. 遍历回溯
    # for i in range(n):
    #     seq = []
    #     back_track(seq_list, seq, i, n)
    back_track(seq_list, 0, seq, n)

    # 3. 返回结果值
    return seq_list[k - 1]


if __name__ == "__main__":
    # n = int(sys.stdin.readline().strip())
    # k = int(sys.stdin.readline().strip())

    # solution = Solution()
    print(k_in_n(3, 3))
