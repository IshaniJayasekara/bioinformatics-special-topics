'''
Implementation of python oop concepts inheritance, polymorphism and encapsulation

Author - Ishani Jayasekara
Date - 8/2/2023
'''

from practical3_lab4_Q2 import Sequence

# subclass DNAseq
class DNAseq(Sequence):

    # constructor
    def __init__(self, sequence, gene_id, gene_name, species_name, subspecies_name):
        super().__init__(sequence, gene_id, gene_name, species_name, subspecies_name)
        self.AT_content = self.get_AT_content()
        self.transcribed_seq = self.transcribe_sequence()
        Sequence.Sequence_count += 1


    # instance method to translate sequence
    def transcribe_sequence(self):
        self.transcribed_seq = self.sequence.replace("T", "U")
        return self.transcribed_seq

    # instance method to get AT content
    def get_AT_content(self):
        AT_count = 0
        for base in self.sequence:
            if (base == "A") or (base == "T"):
                AT_count += 1
        seq_len = len(self.sequence)
        self.AT_content = (AT_count / seq_len) * 100
        return self.AT_content

# subclass MRNAseq
class MRNAseq(Sequence):
    # private class attribute
    _Amino_acid_codons = {}

    # constructor
    def __init__(self, sequence, gene_id, gene_name, species_name, subspecies_name, translated_seq=None):
        super().__init__(sequence, gene_id, gene_name, species_name, subspecies_name)
        self.AT_content = self.get_AT_content()
        self.translated_seq = translated_seq
        Sequence.Sequence_count += 1

    # instance method to get AT content
    def get_AT_content(self):
        AU_count = 0
        for base in self.sequence:
            if (base == "A") or (base == "U"):
                AU_count += 1
        seq_len = len(self.sequence)
        self.AT_content = (AU_count / seq_len) * 100
        return self.AT_content

    @classmethod
    def upload_codons(cls, text_file):
        with open(text_file,"r") as file:
            for line in file:
                if (line[0] != "#") and (line != "\n"):
                    codon = line.strip().split("\t")[0]
                    cls._Amino_acid_codons[codon] = line.strip().split("\t")[2]

    # instance method to translate sequence
    def translate_sequence(self):
        count = 0
        self.translated_seq =""
        while count < len(self.sequence):
            codon = self.sequence[count:count+3]
            if (codon=="UAG") or (codon=="UGA") or (codon=="UAA"):
                break
            self.translated_seq += MRNAseq._Amino_acid_codons[codon]
            count += 3
        return self.translated_seq

# subclass ProteinSeq
class ProteinSeq(Sequence):

    # constructor
    def __init__(self, sequence, gene_id, gene_name, species_name, subspecies_name,reviwed_status, uniprot_id):
        super().__init__(sequence, gene_id, gene_name, species_name, subspecies_name)
        self.reviewed_status = reviwed_status
        self.uniprot_id = uniprot_id
        self.hydrophobicity = self.get_hydrophibicity()
        Sequence.Sequence_count += 1

    # instance method to get hydrophobicty
    def get_hydrophibicity(self):
        Hydrophobic_amino_acids = ["A", "I", "L", "M", "F", "W", "Y", "V"]
        haa_count = 0
        for aa in self.sequence:
            if aa in Hydrophobic_amino_acids:
                haa_count += 1
        seq_len = len(self.sequence)
        self.hydrophobicity = (haa_count/seq_len)*100
        return self.hydrophobicity

