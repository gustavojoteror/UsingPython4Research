# Translation process is essentially a table lookup operation: python has dictionary for this
# the table below was given by the course, each three letter DNA corresponds to 1 aminoacid
table = {
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
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

print(table['CAA'])

# steps:
#       1. Check that the length of the sequence is divisible by 3
#       2. Look up each 3-letter string in table and store results
#       3. Contiue lookup until reaching the end of the sequence.

# module operator:
print("7/3: ",7/3)
print("7%3: ",7%3)
print("6/3: ",6/3)
print("6%3: ",6%3)

def translate(seq):
    #docstring: documentation of the function:
    """ Translate a string containing a nucleotide sequence into a string
    containing the corresponding sequence of amino acids. Nucleotides are tranlsated....
    :param seq
    :return: protein
    """
    table = {
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
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

    protein = ''
    # check that the sequence length is divisible by 3 (using the module operator (residual) 7 % 3 = 1, 6 % 3 = 0)
    if len(seq) % 3 == 0:
        #pass        # pass statement is like nothing happen but this compound statement (if statement) needs something
        #seg[0:3]     #slicing the string
        #list(range(0, len(seq), 3))       # If we want to print out the values we need to first turn that into a list.

        #loop over the sequence
        for i in range(0, len(seq), 3):
            # extract single codon
            codon    = seq[i:i+3]
            # look up the condon and stor the results
            protein +=table[codon]

    return protein

print(translate('ATA')) # solution should be I
print(translate('AAA')) # solution should be K

help(translate)     # to see the docstring or documentation of the function



