def to_rna(dna):
    dna_to_rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
        }
    try:
        return ''.join([dna_to_rna[char] for char in dna])
    except KeyError:
        return ''

