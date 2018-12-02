def dailyTemperatures(t):
    wait = [0] * len(t)
    stack = []
    for i in range(len(t)):
        while len(stack) > 0:
            if t[i] > t[stack[-1]]:
                old = stack.pop()
                wait[old] = i - old
            else:
                break
        stack.append(i)
    return wait