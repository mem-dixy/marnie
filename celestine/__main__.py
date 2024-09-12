import math


X = 338 * math.sqrt(2)
Y = 140

A = X / math.sqrt(1)
B = X / math.sqrt(2)
C = X / math.sqrt(3)
D = X / math.sqrt(4)
E = Y * math.sqrt(2)
F = Y / math.sqrt(1)
G = Y / math.sqrt(2)
H = Y / math.sqrt(4)

print(round(A),round(B),round(C),round(D))
print(round(E),round(F),round(G),round(H))

shorter1 = 1 / math.sqrt(2)
double1 = shorter1 * 2.0
elipse1 = double1 / math.sqrt(3)
oval1 = 1.0

shorter1 = 1 / math.sqrt(4)
double1 = 1 / math.sqrt(1)
elipse1 = 1 / math.sqrt(3)
oval1 = 1 / math.sqrt(2)

oval1 = 1.0
elipse1 = math.sqrt(2) / math.sqrt(3)
shorter1 = math.sqrt(2) / math.sqrt(4)

double1 = 0
longer1 = 0
dimond1 = 0

mini = 0.251
lowest = 0.5

mini = 0.05
lowest = 0.1

def fix(numer: float) -> float:
	return abs(round(numer) - numer)


for index1 in range(1,4000):
	index = index1
	shorter = index * shorter1
	double = index * double1
	elipse = index * elipse1
	oval = index * oval1
	longer = index * longer1
	dimond = index * dimond1

	a = fix(index)
	b = fix(shorter)
	c = fix(double)
	d = fix(elipse)
	e = fix(oval)
	f = fix(longer)
	g = fix(dimond)

	a1 = round(index)
	b1 = round(shorter)
	c1 = round(double)
	d1 = round(elipse)
	e1 = round(oval)
	f1 = round(longer)
	g1 = round(dimond)

	z = a+b+c+d+e+f+g


#	if a < lowest and b<lowest and c<lowest:
	if b < lowest and z < mini:
		#lowest = z
		print(f"{e1}\t{d1}\t{b1}\t{e}\t{d}\t{b}\t{z}\t<<")
		#print(f"{index1}\t{a}\t{b}\t{c}\t{d}\t{e}\t{f}\t{g}\t{z}")
		#print(f"{index}\t{a1}\t{b1}\t{c1}\t{d1}\t{e1}\t{f1}\t{g1}\t<<")

print("done")
