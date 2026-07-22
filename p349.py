def intersection(nums1,nums2):
    result=[]
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if(nums1[i]==nums2[j]):
                if nums1[i] not in result:
                    result.append(nums1[i])
    return result
nums1=[4,9,5]
nums2=[9,4,9,8,4]
print(intersection(nums1,nums2))
