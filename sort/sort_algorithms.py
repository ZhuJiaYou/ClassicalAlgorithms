def bubble_sort(arr):
    for i in range(1, len(arr)):  # NOTICE THE <1>
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]







if __name__ == '__main__':
    a = [2, 8, 5, 7, 3, 0]
    bubble_sort(a)
    print(a)
