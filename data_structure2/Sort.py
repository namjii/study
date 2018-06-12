

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


def find_left(l, left, right, pivot):
    while left != right or left_hit:
        if l[left] > l[pivot]:
            left_hit = left
        else:
            left += 1


def quick_sort(l):
    pivot = int(len(l)/2)  # random
    left = 0
    right = len(l) - 1
    left_hit = None
    right_hit = None

    while left < right:
        print("left = {}".format(left))
        print("right = {}".format(right))
        print("pivot = {}".format(pivot))
        if not left_hit:
            if l[left] > l[pivot]:
                left_hit = left
                print("left_hit = {}".format(left_hit))
            else:
                left += 1

        if not right_hit:
            if l[right] < l[pivot]:
                right_hit = right
                print("right_hit = {}".format(right_hit))
            else:
                right -= 1

        if left_hit is not None and right_hit is not None:
            print("change")
            l[left_hit], l[right_hit] = l[right_hit], l[left_hit]
            left_hit = None
            right_hit = None
            left += 1
            right -= 1

    # if left >= right:
        # if l[left] < l[pivot]:
    if left <= pivot:
        l[left], l[pivot] = l[pivot], l[left]
        pivot = left
    else:
        l[right], l[pivot] = l[pivot], l[right]
        pivot = right

    print("len left = {}".format(l[:pivot]))
    if len(l[:pivot]) > 1:
        l[:pivot] = quick_sort(l[:pivot])
    print("len right = {}".format(l[pivot:]))
    if len(l[pivot:]) > 1:
        l[pivot:] = quick_sort(l[pivot:])
    return l

if __name__ == '__main__':
    # print(bubble_sort([8, 3, 6, 5, 1, 2]))
    # print(bubble_sort([1, 2, 3, 4, 5, 6]))
    # print(bubble_sort([6, 5, 4, 3, 2, 1]))

    # print(quick_sort([3, 8, 0, 2, 1, 4]))
    # print(quick_sort([9, 8, 3, 1, 4]))
    # print(quick_sort([1, 2, 3, 4, 5]))
    # print(quick_sort([5, 3, 7, 6, 2, 1, 4]))
    print(quick_sort([2, 3, 5, 4, 9, 1]))
