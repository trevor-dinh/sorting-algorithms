trace_debug = True


def quicksort(arr, l, h):
    if h-l > 0:
        p = partition(arr, l, h)
        quicksort(arr, l, p-1)
        quicksort(arr, p+1, h)


def partition(arr, l, h):
    p = h
    firsthigh = l
    for i in range(l, h):
        if arr[i] < arr[p]:
            arr[i], arr[firsthigh] = arr[firsthigh], arr[i]
            firsthigh += 1
    arr[p], arr[firsthigh] = arr[firsthigh], arr[p]
    return firsthigh


if __name__ == '__main__':
    a = [i for i in range(10, 0, -1)]
    print(a)
    quicksort(a, 0, len(a)-1)
    print(a)
