from criticalpath import Node

p = Node("project")

a = p.add(Node("A", duration=3))
c = p.add(Node("C", duration=2))
d = p.add(Node("D", duration=3))

e = p.add(Node("E", duration=1))
b = p.add(Node("B", duration=5))
h = p.add(Node("H", duration=3))
f = p.add(Node("F", duration=4))


g = p.add(Node("G", duration=1))
j = p.add(Node("J", duration=4))
i = p.add(Node("I", duration=5))
l = p.add(Node("L", duration=2))

k = p.add(Node("K", duration=5))

p.link(a, e).link(e, g).link(e, h).link(g, k)
p.link(c, b).link(b, j).link(c, h).link(h, j).link(h, i)
p.link(d, h).link(h, i).link(d, f).link(f, i).link(f, l)


# all tasks A-K must be completed within 10 weeks
# you're allocated 4 workers per week
# the most workers on a given task is 2 per week
# the most workers on all tasks for a given week is 5
# putting an additional worker on a task (2 total) adds a $100 charge
# charge $200 per worker per week
# if you use an extra worker (5 total) it is a $300 charge for the week

p.update_all()
print(p.get_critical_path())

