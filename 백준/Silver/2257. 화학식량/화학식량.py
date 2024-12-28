import sys
string = list(sys.stdin.readline().rstrip())
alpha = { 'H' : 1, 'C' : 12, 'O' : 16 } #1
stack = []
for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
    elif string[i] in alpha:
        stack.append(alpha[string[i]])
    elif string[i] == ')':
        tmp = 0
        while stack and stack[-1] != '(':
            p = stack.pop()
            tmp += p
        stack.pop()
        stack.append(tmp)
    else:
        stack.append(stack.pop() * int(string[i]))
print(sum(stack))