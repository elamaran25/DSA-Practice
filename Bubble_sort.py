def bubbleSort(arr):

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

arr = [ 2, 5, 1,2,7,3]
print(bubbleSort(arr))