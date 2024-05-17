# 第二题， 给一个 sorted 的 integer list, 和一个 target, 返回所有总和为 target 的
# sublist( 不用是相连的 sublist), for example, list=[1,2,3,4]，target = 4, return
# [[1,3], [4]]. 又问了一些 follow up，比如 list 为空，target=0 时，应该返回 [[]]；
# list 里有负数的情况

# 递归解法
import numpy as np
def tsublist(seq, target):
    sublist = []
    sub_sublist = []
    cnt = 0
    for i, si in enumerate(seq):   # 先取子序列中最大的值为si, 然后回溯下一个可能的值
        sub_sublist = []
        for j, sj in enumerate(seq[0:i]):  # 回溯左半序列
            target_si = target - si
            if sj == target_si:
                sublist.append([sj, si])
                cnt = cnt + 1
            elif sj < target_si:
                if len(tsublist(seq[0:j+1], target_si)) != 0:
                    tmp = [tsublist(seq[0:j+1], target_si), si]
                    #sub_sublist = np.ravel(tmp)
                    sub_sublist.append(tmp)
        if len(sub_sublist) != 0:
            sublist.append(sub_sublist)

                #sublist.append(sub_sublist, si)
   # if cnt == 0:
    #    sublist.append([])
    return sublist


