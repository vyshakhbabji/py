import sys

from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
from Bio.Seq import Seq
from Bio import SeqIO

def read_file(file):
    buf = open(file)
    arrList = list(SeqIO.parse(buf, "fasta"))
    buf.close()
    return [(ele.description, ele.seq.tostring()) for ele in arrList]

def assignment29():
    buff = read_file("/home/sulab/py/rosalind_loca.txt")
    newMatrix = matlist.pam250
    replaceMatrix = pairwise2.align.localds(buff[0][1], buff[1][1], newMatrix, -5, -5)
    start,end = replaceMatrix[0][3:]
    print int(replaceMatrix[0][2])
    print replaceMatrix[0][0][start:end].replace('-','')
    print replaceMatrix[0][1][start:end].replace('-','')

assignment29()
