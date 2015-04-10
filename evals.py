n = 815826
dnaString = "CGTTACAAG"
arrLen= "0.000 0.068 0.137 0.182 0.261 0.296 0.370 0.415 0.478 0.571 0.623 0.653 0.744 0.792 0.838 0.915 1.000"
length = map(float,  arrLen.split())
result = []
for i in length:
    len1 = i * .5
    len2 = (1 - i) * .5
    totalLen = 1
    for c in dnaString:
        if "GC".find(c) >= 0:
           totalLen *= len1
        else:
            totalLen *= len2
    result.append((n - len(dnaString) + 1) * totalLen)
print(" ".join(str(round(i,3)) for i in result))

