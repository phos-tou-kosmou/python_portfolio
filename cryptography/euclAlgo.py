A:    int = 0
B:    int = 0
p:    int = 0
q:    int = 0
temp: int = 0
fin:  int = 0

A = int(input("Please enter an integer"))
B = int(input("Again"))

if A < B:
	q = A//B
	p = B*q - A
else:
	q = B//A
	p = B*q - A

print(p, q)
