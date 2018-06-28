#2d matrix or nested list
matrix=[
       [2, 3, 7, 8, 9],
       [3, 6, 7, 8, 6],
       [5, 8, 9, 4, 7],
       [0, 6, 9, 4, 5]

]
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
