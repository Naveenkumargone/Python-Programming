L1 = [11, 21, 24, 12, 18]
L2 = [14, 44, 25, 37, 13]
L3 = []
L4 = []

for i in L1:
      if L1.index(i) %2 == 0:
            L3.append(i)
for i in L2:
      L4.append(L2[1])
      L4.append(L2[3])
      break
for i in L4:
      L3.append(i)

print(L3)


             