import random

tovar, prov = map(int, input().split())
a = list(map(int, input().split()))


def quick_sort(s):
    if len(s) > 1:
        pivot = random.choice(s)
        less = [x for x in s if x > pivot]
        equal = [x for x in s if x == pivot]
        greater = [x for x in s if x < pivot]
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return s


an = quick_sort(a)
for _ in range(prov):
    x, y = map(int, input().split())
    b = an[:x]
    print(sum(b[-y:]))