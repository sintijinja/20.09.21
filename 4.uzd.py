saraksts = 4
saraksts = [int(4)for 4 in input("2 3 8 6")]
saraksts = [int(4)for 4 in input("2 3 8 6").split()]
for i in range(len(saraksts)):
  if saraksts[i] == saraksts[i+1]:
    print(saraksts[i],saraksts[i+1])
    