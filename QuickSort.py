def quic_sort(arr):
    if len(arr)<2:
        return arr
    pivot=arr[0]
    left=[x for x in arr[1:] if x<pivot ]
    right=[x for x in arr[1:] if x>pivot ]
    return quic_sort(left) + [pivot] + quic_sort(right)


print(quic_sort([1,5,6,3,8,4,7,2]))
