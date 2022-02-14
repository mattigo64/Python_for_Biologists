genomic_dna = open("genomic_dna.txt").read()

exons_local = open("exons.txt")
coding_sequence = ""
for line in exons_local:
    positions = line.split(",")

    start = int(positions[0])
    stop = int(positions[1])
    exon = genomic_dna[start:stop]
    coding_sequence = coding_sequence + exon
    print("coding sequence is : " + coding_sequence)
