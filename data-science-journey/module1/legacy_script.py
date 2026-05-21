import sys

def f(l):
    s = 0
    n = 0
    for x in l:
        if x != None:
            s = s + x
            n = n + 1
    if n == 0:
        return 0
    return s / n

def g(l, t):
    r = []
    for x in l:
        if x > t:
            r.append(x)
    return r

def main():
    data = [10, 20, None, 30, None, 40, 50]
    print("moyenne:", f(data))
    print("sup a 25:", g([x for x in data if x != None], 25))

if __name__ == "__main__":
    main()