

def insertion_sort(l):
    n = len(l)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if l[j-1] > l[j]:
                l[j-1], l[j] = l[j], l[j-1]
            else:
                break

    return l


def bubble_sort(l):
    n = len(l)
    # 0 1 2 3 4 5
    for i in range(0, n):
        # 0 1 2 3 4 5
        for j in range(0, n-1-i):
            # 8 3 6 5 1 2
            # [0] 3 8 6 5 1 2
            # [1] 3 6 8 5 1 2
            # [2] 3 6 5 8 1 2
            # [3] 3 6 5 1 8 2
            # [4] 3 6 5 1 2 8
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l



if __name__ == '__main__':
    print(bubble_sort([8, 3, 6, 5, 1, 2]))
    print(bubble_sort([1, 2, 3, 4, 5, 6]))
    print(bubble_sort([6, 5, 4, 3, 2, 1]))
