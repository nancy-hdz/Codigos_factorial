def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >key:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
arr = [103, 23, 53, 24, 83, 44, 29, 23, 14, 8]
insertion_sort(arr)
print("Lista ordenada", arr)