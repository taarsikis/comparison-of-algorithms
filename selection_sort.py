import copy


def selection_sort(L):
    arr = copy.deepcopy(L)
    counter = 0
    for i in range(len(arr)):

        min_index = i
        for j in range(i+1, len(arr)):
            counter += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr, counter

if __name__ == "__main__":
    a = [5,4,3,2,1]
    print(selection_sort(a))
