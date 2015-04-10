from Bio import Entrez
from Bio import SeqIO

def genebank(x,y):

        Entrez.email = "vyshakh.babji@gmail.com"
        handle1 = Entrez.efetch(db="nucleotide", id=x, rettype="fasta")
        seq1 = handle1.read()
        handle2 = Entrez.efetch(db="nucleotide", id=y, rettype="fasta")
        seq2 = handle2.read()
        file1 = open("/home/sulab/py/neu1.txt",'w')
        file2 = open("/home/sulab/py/neu2.txt",'w')
        file1.write(seq1)
        file2.write(seq2)
        file1.close()
        file2.close()


genebank("JX069768.1","NM_001168970.1")
