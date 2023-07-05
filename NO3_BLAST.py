import gget as gg
import pandas as pd


class NO3BLAST:
    def __init__(self, expression, fastafile):
        self.expression = expression
        self.fastafile = fastafile 
    def read_fasta(self): 
        self.fasta_read = []
        self.fasta_names = ""
        with open("self.fastafile", "r") as fasta:
            for i in fasta.readlines():
                if i.startswith(">"):
                    self.fasta_read.append(self.fasta_names)
                    self.fasta_names = i.strip()
                else:
                    self.fasta_read += i.strip()
        names = list(filter(None,[i[0] for i in 
                                   ([i.split("\t") for i in self.fasta_read])]))
        sequences = [i[1] for i in (list(filter(lambda n: n!=[''],
                                    [i.split("\t") for i in self.fasta_read])))]
        self.fastadf = pd.DataFrame([(i,j) for i,j in 
                                        zip(self.fasta_read, self.fasta_names)])

    def blastFasta(self):
        blastNO3 = []
        for i in range(len(self.fasta_read)):
            blastNO3.append(gg.blast(self.fasta_read[i]))
            return blastNO3