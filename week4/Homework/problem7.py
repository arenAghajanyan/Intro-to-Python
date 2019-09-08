l4=[[10, 20, 40], [40, 50, 60], [70, 80, 90]]
l5=[[l4[x][y] for y in range(2)] for x in range(3)]
l5[0].append(100)
l5[1].append(100)
l5[2].append(100)
print(l4)
print(l5)