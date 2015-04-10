f=open("/home/sulab/Downloads/rosalind_iprb.txt","r+")
num = f.readline().split(" ")
print num
k ,m,n = map(int, (num[0] ,num[1],num[2]))
print((k * (k - 1) + 2 * k * m + 2 * k * n + m * (m - 1) * .75 + 2 * m * n * .5)/(k + m + n) /(k + m + n - 1))

