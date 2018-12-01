trace_debug = True
import random


def quicksort(arr, l, h):
    if h-l > 0:
        p = partition(arr, l, h)
        quicksort(arr, l, p-1)
        quicksort(arr, p+1, h)


def partition(arr, l, h):
    p = h
    firsthigh = l
    print("quicksort: arr = {}, pivot = arr[{}] ({}), l = arr[{}] ({}), h = arr[{}] ({})".format(arr[l:h+1],
        p, arr[p], l, arr[l], h, arr[h]))
    for i in range(l, h):
        print("loop {}".format(i))
        if arr[i] < arr[p]:
            if trace_debug:
                print("arr[{}] ({}) is less than arr[{}] ({})".format(
                    i, arr[i], p, arr[p]))
                print("In loop, swapping arr[{}] ({}) and arr[{}] ({})".format(
                    i, arr[i], firsthigh, arr[firsthigh]))
            arr[i], arr[firsthigh] = arr[firsthigh], arr[i]
            firsthigh += 1
            if trace_debug:
                print("firsthigh is now {}".format(firsthigh))
    arr[p], arr[firsthigh] = arr[firsthigh], arr[p]
    print("arr at end of quicksort call: {}".format(arr[l:h+1]))
    return firsthigh


if __name__ == '__main__':
    a = [3, 7, 8, 5, 2, 1, 9, 5, 4]
    # random.shuffle(a)
    print(a)
    quicksort(a, 0, len(a)-1)
    print(a)
