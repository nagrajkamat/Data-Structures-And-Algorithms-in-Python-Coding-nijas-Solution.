import itertools
str = input()
x = list(itertools.permutations(str))
for i in x:
    for j in i:
        print(j, end ="")
    print()
