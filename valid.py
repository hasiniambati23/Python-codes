opcl = dict(('()', '[]', '{}'))
stack = []
s='{(}'
for i in s:
    if i in opcl:
        stack.append(i)
    elif len(stack) == 0 or i != opcl[stack.pop()]:
        print(False)

print(len(stack) == 0)