
def matpow(mat1,mat2,r1,c2,r2):
	mat1 = mat1
	mat2 = mat2
	result = []
	r1=r1
	c2=c2
	r2=r2

	for r_1 in range(r1):
		sum = []
		for c_2 in range(c2):
			s = 0
			for r_2 in range(r2):
				s = (mat1[r_1][r_2] * mat2[r_2][c_2] + s)%1000000007
			sum.append(s)
		result.append(sum)
	return result

def matmul(A,m,n):
	m=m
	A=A
	identity = []
	for i in range(m):
		x = [0] * i
		x.append(1)
		x.extend([0] * (m - i - 1))
		identity.append(x)

	while(n>0):
		if n%2==0:
			A=matpow(A,A,m,m,m)
			n//=2
		else:
			n-=1
			identity=matpow(A,identity,m,m,m)
	return identity


for _ in range(int(input())):
	m, n = map(int, input().split())
	A = []
	for i in range(m):
		row = [int(x) for x in input().split()]
		A.append(row)
	res = matmul(A, m, n)

	for r in res:
		for i in range(m):
			print(r[i] % 1000000007, end=" ")
		print()
