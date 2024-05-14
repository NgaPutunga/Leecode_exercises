# 第一题: fibonacci 数列，给一个 positive 的数 n，返回 fib(n)， 要求用 recursive 和 iterative 的方法分别实现，
# 写完以后让分析了一下这两种方法的优缺点，什么时候用 recursive，什么时候用 iterative

# Comment: 对比代码会发现递归显得更整洁，函数里面调用函数自身，循环代码显得比较多，但是函数调用是有时间和空间的消耗的：
# 每一次函数调用，都需要在内存栈中分配空间以保存参数、返回地址及临时变量，这些空间的占用只有在递归退出时才会释放，当递归
# 调用的层级太多的时候，就会超出栈的容量，从而导致调用栈溢出。而且往栈里压入数据和弹出数据都需要时间，所以不难理解递归的
# 实现效率不如循环
# 所以论效率，递归必然是低的。程序中函数的开销很大，而所有递归都可以通过循环来实现。它的优势不在于效率，而在于便于理解，一种直观的理解

def fib_recu(n):
    if n == 1 or n == 2:
        return 1
    return fib_recu(n-2) + fib_recu(n-1)

def fib_iter(n):
    n1, n2 = 1, 1
    for i in range(n-2):
        n1, n2 = n2, n1 + n2  # move n1, n2 by this equation
    return n2

def fib_series(n):
    if n == 1:
        fibs = [1]
        return fibs
    if n == 2:
        fibs = [1, 1]
        return fibs
    fibs = [1, 1]
    for i in range(n-2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs