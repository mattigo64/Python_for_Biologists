exons_location = open("exons.txt")

genomic_file = open("genomic_dna.txt").read()

coding_sequence = ""

for line in exons_location:
    
    positions = line.split(',')
    start = int(positions[0])
    stop = int(positions[1])

    exon = genomic_file[start:stop]
    coding_sequence = coding_sequence + exon

output = open("coding_sequence.txt", "w")
output.write(coding_sequence)
output.close()
