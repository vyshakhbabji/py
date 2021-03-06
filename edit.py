import sys
from Bio.Seq import Seq
from Bio import SeqIO


def read_file(file):
    buf = open(file)
    arrList = list(SeqIO.parse(buf, "fasta"))
    buf.close()
    return [(ele.description, ele.seq.tostring()) for ele in arrList]

def assignment27():
   
    buff = read_file("/home/sulab/py/rosalind_edit .txt")
    arr1, arr2 = buff[0][1], buff[1][1]
  
    len1 = len(arr1)
    len2 = len(arr2)
    
    dist=1
    place=1

    mat = [[None for i in range(len2+1)] for j in range(len1+1)]

    for i in xrange(len1+1):
        mat[i][0] = i

    for j in xrange(len2+1):
        mat[0][j] = j
        
    for i in xrange(1, len1+1):
        for j in xrange(1, len2+1):
            mat[i][j] = min(mat[i][j-1] + dist,mat[i-1][j] + dist,mat[i-1][j-1] + (place if arr1[i-1] != arr2[j-1] else 0))

    print mat[-1][-1]

assignment27()
