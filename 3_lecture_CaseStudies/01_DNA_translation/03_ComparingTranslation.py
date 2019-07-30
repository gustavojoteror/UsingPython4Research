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


def read_seq(inputfile):
    """
    Reads and returns the input sequence with special characters removed.
    :param inputfile:
    :return:
    """
    with open(inputfile, 'r') as f:     # compound statement
        seq       =  f.read()           #we read the whole file at once
    seq = seq.replace('\n', '')   # a string is immutable, therefore we need to assign it to a variable
    seq = seq.replace('\r', '')   # \r is a carriage return
    return seq

prt_seq = read_seq('protein.txt')
dna_seq = read_seq('dna.txt')

print(prt_seq)
print(dna_seq)

dna_trans = translate(dna_seq)
print(dna_trans)        # is empty because the length of the sequence is not dividisble by 3.
# checking the website where the data was taken we see that the sequence starts at 21 and goes till 938
#   the data is numerated from 1 to 1157 so be careful because python starts at 0.

dna_trans = translate(dna_seq[20:938])
print(dna_trans)                        # now we are getting a translation but is it correct?

print(dna_trans == prt_seq)             # NO! But the only difference is a underscore at the end that is that data
                                        # telling us that the dna sequence is finished.

print(dna_trans[0:-1] == prt_seq)
print(dna_trans[:-1] == prt_seq)

