def back_com(s,t):
    def build(string):
        stack = []
        for ch in string:
            if ch == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return stack
    return build(s) == build(t)
s = "a#c"
t = "b"
print(back_com(s,t))
