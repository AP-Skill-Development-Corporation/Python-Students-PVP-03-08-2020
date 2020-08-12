# Even or odd
def even(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"


def unique(l):
    li = []
    for i in l:
        if l.count(i) == 1:
            li.append(i)
    print(li)