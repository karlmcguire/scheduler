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
