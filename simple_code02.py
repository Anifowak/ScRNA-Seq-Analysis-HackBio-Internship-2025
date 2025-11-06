#To translate DNA to Protein
def dna_to_protein(dna_seq):
    """
    Translates a DNA sequence into a protein sequence.

    Parameters:
        dna_seq (str): A string representing the DNA sequence (e.g. 'ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')

    Returns:
        str: The translated protein sequence
    """
     # DNA codon table
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'stop', 'TAG':'stop',
        'TGC':'C', 'TGT':'C', 'TGA':'stop', 'TGG':'W',
    }

    # Clean sequence
    dna_seq = dna_seq.upper().replace(" ", "")

    # Translate in codons
    protein = ""
    for i in range(0, len(dna_seq) - 2, 3):
        codon = dna_seq[i:i+3]
        protein += codon_table.get(codon, '?')  # '?' for invalid codons

    return protein

# Example usage:
print(dna_to_protein("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"))




#Hamming distance between slack username and twitter
def hamming_distance(str1, str2):
    """
    Calculates the Hamming distance between two strings.
    Pads the shorter string with underscores '_' to match lengths.

    Parameters:
        str1 (str): First string
        str2 (str): Second string

    Returns:
        int: Hamming distance between the two strings
    """

    # Pad shorter string
    max_len = max(len(str1), len(str2))
    str1 = str1.ljust(max_len, '_')
    str2 = str2.ljust(max_len, '_')

    # Compute distance
    distance = sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))
    return distance

# Example usage:
slack_username = "Akinjide"
twitter_handle = "Anifowose"

print("Hamming Distance:", hamming_distance(slack_username, twitter_handle))
