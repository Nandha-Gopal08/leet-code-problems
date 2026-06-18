def findMedianSortedArrays( nums1, nums2):
    i=j=0
    merge=[]
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<=nums2[j]:
            merge.append(nums1[i])
            i+=1
        else:
            merge.append(nums2[j])
            j+=1
    while i<len(nums1):
        merge.append(nums1[i])
        i+=1
    while j<len(nums2):
        merge.append(nums2[j])
        j+=1
    n=len(merge)
    if n%2 == 1:
        return (float(merge[n // 2]))
    else:
        return (merge[n // 2 -1] + merge[n //2]) / 2
print(findMedianSortedArrays([1,2],[3,4]))
