
a = []
b = []


def numberCopy(A='algorithm', B='altruistic'):
    u = 0
    t = 0
    for i in range(0, len(A)):
        for j in range(t, len(B)):
            if A[i] == B[j]:
                a.append(i)
                b.append(j)
                t = j
                break


def operation(A='algorithm', B='altruistic'):
    copy = 0
    replace = 0
    delete = 0
    insert = 0
    i = 0
    j = 0
    try:
        while i != len(A):
            if a[copy] == i and b[copy] == j:
                copy += 1
                i += 1
                j += 1
            elif a[copy] != i and b[copy] != j:
                replace += 1
                i += 1
                j += 1
            elif a[copy] != i and b[copy] == j:
                delete += 1
                i += 1
            elif a[copy] == i and b[copy] != j:
                insert += 1
                j += 1
    except Exception:
        x = len(A[i:])
        y = len(B[j:])
        if x == y:
            replace += x
        elif x > y:
            replace += y
            delete += x - y
        else:
            replace += x
            insert += y - x
    print 'copy = %s' % copy
    print 'replace = %s' % replace
    print 'delete = %s' % delete
    print 'insert = %s' % insert
    return (replace + delete + insert)


if __name__ == '__main__':
    A = raw_input()
    B = raw_input()
    numberCopy(A, B)
    print operation(A, B)
