import copy


def shell_sort(inp):
    arr = copy.deepcopy(inp)
    counter = 0
    n = len(arr)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = arr[i]
            j = i
            counter += 1
            while j >= h and arr[j - h] > t:
                counter += 1
                arr[j] = arr[j - h]
                j -= h

            arr[j] = t
        h = h // 2
    return arr, counter

if __name__ == "__main__":
    a = [5,4,3,2,1]
    print(shell_sort(a))
    print(a)