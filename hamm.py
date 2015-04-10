f=open("/home/sulab/Downloads/rosalind_hamm.txt","r+")
st = f.readlines()
a = st[0]
b = st[1]
print(sum(1 if c != d else 0 for c, d in zip(a, b)))

