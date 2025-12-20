def prefix_to_infix(prefix):
    stack = []
    for c in reversed(prefix):
        if c.isalnum():
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"({op1}{c}{op2})")
    return stack[-1]



prefix_exp = input()

result = prefix_to_infix(prefix_exp)
print("Infix expression:", result)
