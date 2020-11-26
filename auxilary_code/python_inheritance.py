class A:
    val1 = 1
    val2 = 1


class B(A):
    val2 = 2


class C(A):
    val3 = 2


if __name__ == '__main__':
    print(A.val1)
    print(A.val2)
    print(B.val1)
    print(B.val2)
    print(C.val1)
    print(C.val2)
    print(C.val3)
