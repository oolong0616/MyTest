# 廖雪峰培训学习
def add_end(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a =b
        b=a+b

        n = n + 1
    return 'done'

if __name__ == '__main__' :
    add_end(20)