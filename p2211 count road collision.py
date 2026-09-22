def count_colli(directions):
    left = 0
    right = len(directions) - 1
    collision = 0

    while left <= right and directions[left] == 'L':
        left += 1
    while left <= right and directions[right] == 'R':
        right -= 1
    while left <= right:
        if directions[left] != 'S':
            collision += 1
        left += 1
    return collision
directions = "LLRLRSLRR"
collission = count_colli(directions)
print("No Of Collision :", collission)
