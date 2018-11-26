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
    print("quicksort: pivot = arr[{}] ({}), l = arr[{}] ({}), h = arr[{}] ({})".format(p, arr[p], l, arr[l], h, arr[h]))
    for i in range(l, h):
        print("loop {}".format(i))
        if arr[i] < arr[p]:
            if trace_debug:
                print("arr[{}] ({}) is less than arr[{}] ({})".format(i,arr[i], p, arr[p]))
                print("In loop, swapping arr[{}] ({}) and arr[{}] ({})".format(i, arr[i], firsthigh, arr[firsthigh]))
            arr[i], arr[firsthigh] = arr[firsthigh], arr[i]
            firsthigh += 1
    arr[p], arr[firsthigh] = arr[firsthigh], arr[p]
    print("arr at end of quicksort: {}".format(arr))
    return firsthigh


if __name__ == '__main__':
    a = [i for i in range(30, 0, -1)]
    random.shuffle(a)
    print(a)
    quicksort(a, 0, len(a)-1)
    print(a)
