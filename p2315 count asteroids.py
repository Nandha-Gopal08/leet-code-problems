def ast_colli(asteroids):
    stack = []
    for ast in asteroids:
        while(stack and ast < 0 and stack[-1] > 0):
            if stack[-1] < -ast:
                stack.pop()
                continue
            elif stack[-1] == -ast:
                stack.pop()
                ast = 0
                break
            else:
                ast = 0
                break
        if ast != 0:
            stack.append(ast)
    return stack
asteroids = [5,10,-5]
print(ast_colli(asteroids))
