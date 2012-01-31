"""
Probably not the most elegant but it works and it is fast :P

   i
    \
     j   l
   /   \ /
  q     k
 / \   /
r   o-m-n
     \
      p

"""

s = set(range(1,11))
solutions = []
for i in s:
    solution = []
    solution.append(i)

    for j in s - set(solution):
        solution.append(j)

        for k in s -set(solution):
            solution.append(k)
            line = sum(solution)
            first = (i, j, k)

            for l in s - set(solution):
                solution.append(l)
                m = line - l - k

                if m in s - set(solution):
                    solution.append(m)
                    second = (l, k, m)

                    for n in s - set(solution):
                        solution.append(n)
                        o = line - m - n

                        if o in s - set(solution):
                            solution.append(o)
                            third = (n, m, o)

                            for p in s - set(solution):
                                solution.append(p)
                                q = line - o - p

                                if q in s - set(solution):
                                    solution.append(q)
                                    fourth = (p, o , q)
                                    r = line - q - j

                                    if r in s - set(solution):
                                        fifth = (r, q, j)
                                        solutions.append( (first, second, third, fourth, fifth) )

                                    solution.remove(q)
                                solution.remove(p)
                            solution.remove(o)
                        solution.remove(n)
                    solution.remove(m)
                solution.remove(l)
            solution.remove(k)
        solution.remove(j)

formated = [''.join( map(lambda x: ''.join(map(str, x)), solution) )
        for solution in solutions
        if solution[0] == min(solution)]

print max(int(solution) for solution in formated if len(solution) == 16)
