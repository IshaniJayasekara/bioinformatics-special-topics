'''
Create sequence class and Create objects using Sequence class
Input - multi-fasta file
Output - sequence objects

Author - Ishani Jayasekara
Date - 8/2/2023
'''

class Sequence:

    # class attribute
    Sequence_count = 0

    # constructor method
    def __init__(self, sequence, gene_id, gene_name, species_name, subspecies_name):
        self.sequence = sequence
        self.gene_id = gene_id
        self.gene_name = gene_name
        self.sequence_type = self.get_seq_type()
        self.sequence_length = len(sequence)
        self.species_name = species_name
        self.subspecies_name = subspecies_name
        Sequence.Sequence_count += 1

    @staticmethod
    def fasta_split(fasta_file):
        seq_dict = {}
        sequence = ""
        with open(fasta_file, "r") as file:
            for line in file:
                if line[0] == ">":
                    header = line.strip().split("-")
                    gene_name = header[0][1:]
                    sequence = ""
                elif line != "\n":
                    sequence += line.strip()
                seq_dict[gene_name] = [gene_name] + header[1:] + [sequence]
        return seq_dict

    # instance method to get the sequence type
    def get_seq_type(self):
        Amino_acid_list = ["K", "N", "R", "S", "I", "M", "Q", "H", "P", "L", "E", "D", "V", "Y", "W", "F"]
        if any(aa in self.sequence for aa in Amino_acid_list):
            self.sequence_type = "Protein"
        elif "T" in self.sequence:
            self.sequence_type = "DNA"
        else:
            self.sequence_type = "RNA"
        return self.sequence_type

    # instance method to get the character count
    def get_character_count(self):
        character_count = {}
        for base in self.sequence:
            if base not in character_count.keys():
                character_count[base] = 1
            elif base in character_count.keys():
                character_count[base] += 1
        return character_count

# main method
if __name__ == "__main__":

    # sequence dictionary using multi-fasta file
    fasta_file = "OSDREB_sequences.fasta"
    seq_dict = Sequence.fasta_split(fasta_file)
    print(seq_dict)

    # object creation
    values = seq_dict["DREB1A_CDS"]
    DREB1A_CDS = Sequence(values[-1], values[1], values[0], values[2], values[3])

    values = seq_dict["DREB1B_CDS"]
    DREB1B_CDS = Sequence(values[-1], values[1], values[0], values[2], values[3])

    values = seq_dict["DREB2A_CDS"]
    DREB2A_CDS = Sequence(values[-1], values[1], values[0], values[2], values[3])

    values = seq_dict["DREB2B_CDS"]
    DREB2B_CDS = Sequence(values[-1], values[1], values[0], values[2], values[3])

    # DREB1A details
    print("Gene id :", DREB1A_CDS.gene_id, "\nSequence length :", len(DREB1A_CDS.sequence),
          "\nSequence type : ", DREB1A_CDS.get_seq_type())

    # base count
    print(DREB1A_CDS.get_character_count())

