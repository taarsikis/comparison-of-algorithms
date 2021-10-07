counter = 0

def merge(left, right):
    global counter
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        counter += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def mergesort(arr):
    global counter
    counter += 1
    if len(arr) > 1:
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        return merge(left, right)
    else:
        return arr

def main(arr):
    arr = mergesort(arr)
    return arr,counter


if __name__ == "__main__":
    a = [5,4,3,2,1]
    print(main(a))
