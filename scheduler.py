import collections

Task = collections.namedtuple("Task", "id weight depends")

A = Task(id="A", weight=3, depends=[])
C = Task(id="C", weight=2, depends=[])
D = Task(id="D", weight=3, depends=[])

E = Task(id="E", weight=1, depends=[A])
B = Task(id="B", weight=5, depends=[C])
H = Task(id="H", weight=3, depends=[C, D])
F = Task(id="F", weight=4, depends=[D])

G = Task(id="G", weight=1, depends=[E])
J = Task(id="J", weight=4, depends=[E, B, H])
I = Task(id="I", weight=5, depends=[H, F])
L = Task(id="L", weight=2, depends=[F])

K = Task(id="K", weight=5, depends=[G])

# all tasks A-K must be completed within 10 weeks
# you're allocated 4 workers per week
# the most workers on a given task is 2 per week
# the most workers on all tasks for a given week is 5
# putting an additional worker on a task (2 total) adds a $100 charge
# charge $200 per worker per week
# if you use an extra worker (5 total) it is a $300 charge for the week


