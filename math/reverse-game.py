# Reverse Game
#
# https://www.hackerrank.com/challenges/reverse-game/problem

t = int(input().strip())
for _ in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]

    # il faut calculer uniquement la position de k
    for i in range(n):
        if k < i:
            break
        k = n - 1 - k + i
    print(k)

    """ méthode triviale (imite le jeu): trop longue
    a = [i for i in range(n)]
    for i in range(n):
        b= list(reversed(a[i:]))
        a = a[:i] + b
    print(a.index(k))
    """