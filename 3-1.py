problem_size = 1000
num = 0

while problem_size > 0:
    problem_size = problem_size // 2
    num += 1

print('{}: {}'.format(problem_size,num))
