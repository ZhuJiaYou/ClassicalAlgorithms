# stable
# time avg: O(n2), time worst: O(n2), time best: O(n)
# space: O(1)
def bubble_sort(arr):
    for i in range(1, len(arr)):  # NOTICE THE <1>
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# unstable
# time avg: O(n2), time worst: O(n2), time best: O(n2)
# space: O(1)
def selection_sort(arr):
    for i in range(len(arr)-1):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[mini] > arr[j]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]


# stable
# time avg: O(n2), time worst: O(n2), time best: O(n)
# space: O(1)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# unstable
# time avg: O(nlogn2), time worst: O(nlogn2), time best: O(nlogn)
# space: O(1)
def shell_sort(arr):
    k = len(arr) // 2
    while k > 0:
        for m in range(k):
            for n in range(m+k, len(arr), k):
                for p in range(n-k, -1, -k):
                    if arr[p] > arr[p+k]:
                        arr[p], arr[p+k] = arr[p+k], arr[p]
        k = k // 2


# stable
# time avg: O(nlogn), time worst: O(nlogn), time best: O(nlogn)
# space: O(n)
def merge_sort(arr):
    def merge(left, right):
        merged = []
        while left and right:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        return merged + left + right

    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge_sort2(arr):
    def merge(left, right):
        merged = []
        while left and right:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        return merged + left + right

    if len(arr) < 2:
        return
    merged = arr
    n = len(arr)
    size = 1
    while size < n:
        for i in range(0, n-size, size+size):
            merged[i:min(n, i+size+size)] = merge(merged[i:i+size], merged[i+size:min(n, i+size+size)])
        size += size
    # arr = merged




if __name__ == '__main__':
    a = [2, 8, 5, 7, 3, 0, 4]
    # bubble_sort(a)
    # selection_sort(a)
    # insertion_sort(a)
    # print(merge_sort(a))
    merge_sort2(a)
    print(a)
