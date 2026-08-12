def wealth(accounts):
    max_wealth=0
    for i in range(len(accounts)):
        cur_wealth=0
        for j in range(len(accounts[i])):
            cur_wealth+=accounts[i][j]
        if cur_wealth > max_wealth:
            max_wealth=cur_wealth
    return max_wealth
accounts = [[1,5],[7,3],[3,5]]
print(wealth(accounts))
