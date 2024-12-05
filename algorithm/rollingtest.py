s1 = "Harry Potter and the Prisoner of Azkaban part two and hallows"
s2 = "Harry Potter and the Prisoner of Azkaban"

s1Split = s1.split()
s2Split = s2.split()

for i in range(len(s2Split)):
    print(s1, " : ", ' '.join(s2Split[i: i + len(s1Split)]))