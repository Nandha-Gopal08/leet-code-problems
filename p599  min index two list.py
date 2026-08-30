def common_min(list1, list2):
    min_sum = float('inf')
    result = []
    
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                cur_min = i + j

                if cur_min < min_sum:
                    min_sum = cur_min
                    result=[list1[i]]
                elif cur_min == min_sum:
                    result.append(list1[i])

    return result

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]

print(common_min(list1, list2))
