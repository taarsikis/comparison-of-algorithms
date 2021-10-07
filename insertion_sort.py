import copy


def insertion_sort(array):
    arr = copy.deepcopy(array)
    counter = 0

    for index in range(1, len(arr)):
        currentValue = arr[index]
        currentPosition = index

        counter += 1
        while currentPosition > 0 and arr[currentPosition - 1] > currentValue:
            counter += 1
            arr[currentPosition] = arr[currentPosition - 1]
            currentPosition = currentPosition - 1

        arr[currentPosition] = currentValue
    return arr, counter


if __name__ == "__main__":
    a = [5,4,3,2,1]
    print(insertion_sort(a))
