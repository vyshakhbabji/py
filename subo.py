from Bio import SeqIO

def hamming_distance(a,b):
	return (sum(1 if c != d else 0 for c, d in zip(a, b)))

match = 'CAAAAGGTAGCATTTACCGGCGCCCGACCATCAGATAAG'

with open('/home/sulab/Downloads/rosalind_subo.txt') as ip:
    seq = [fasta.seq for fasta in SeqIO.parse(ip, 'fasta')]

print seq[0]
print seq[1]

print [sum([hamming_distance(seq[j][i:i+len(match)],match) <4 for i in range(len(seq[j]) - len(match) + 1)]) for j in range(len(seq))]

