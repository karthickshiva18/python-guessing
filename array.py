# Python program to find the maximum for
# each and every contiguous subarray of
# size k

# Method to find the maximum for each
# and every contiguous subarray of s
# of size k
def printMax(arr, n, k, x=print(str(max) + " ", end="")):
    max = 0

    for i in range(n - k + 1):
        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        x


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    k = 3
    printMax(arr, n, k)