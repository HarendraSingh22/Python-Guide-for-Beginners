# rows for the triangle, exclusing the first one
number = int(input('Enter the limit for bell triangle '))

# decrales empty 2D list
bell = [[None]*(number+1) for _ in range(number+1)]
bell[0][0] = 1

# Computes the new value using previos value
for i in range(1, number+1):
    bell[i][0] = bell[i-1][i-1]
    for j in range(1, i+1):
        bell[i][j] = bell[i-1][j-1] + bell[i][j-1]

# display the triangle
for i in range(number+1):
    for j in range(0, i+1):
        print(bell[i][j], end=' ')
    print('\n')