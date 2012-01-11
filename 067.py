with open('triangle.txt') as f:
    source = f.readlines()

# from source build a reversed triangle (base at the top)
triangle = []
for line in source[::-1]:
    level = []
    for i in line.split(' '):
        level.append(int(i))
    triangle.append(level)

# line by line percolate the max value to the bottom a.k.a triangle top
for level, line in enumerate(triangle[1:]):
    for index, value in enumerate(line):
        triangle[level+1][index] = max(triangle[level][index], triangle[level][index+1]) + value

print triangle[-1][0]
