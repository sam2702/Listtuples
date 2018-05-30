List = []

n = int(raw_input())

for i in range(0, n):
    A =raw_input().split()
    
    if A[0] == 'insert':
        List.insert(int(A[1]), int(A[2]))
    elif A[0] == 'print':
        print (List)
    elif A[0] == 'remove':
        List.remove(int(A[1]))
    elif A[0] == 'append':
        List.append(int(A[1]))
    elif A[0] == 'sort':
        List.sort()
    elif A[0] == 'pop':ist
        List.pop()
    elif A[0] == 'reverse':
        List.reverse()
