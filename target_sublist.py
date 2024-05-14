# 第二题， 给一个 sorted 的 integer list, 和一个 target, 返回所有总和为 target 的
# sublist( 不用是相连的 sublist), for example, list=[1,2,3,4]，target = 4, return
# [[1,3], [4]]. 又问了一些 follow up，比如 list 为空，target=0 时，应该返回 [[]]；
# list 里有负数的情况

def tsublit(s, target):
    sum = 0
    for i in range(s):
        sum = sum + i

    return s


