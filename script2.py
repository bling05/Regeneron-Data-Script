output=open("output.txt", "w")
with open("Chi_DE_Gr_UK_Swe_pad-bwa_GROM-bwa-pad_SNV_count_pc80_ge25.csv") as input:
    data = input.readlines()
    data = set([x[:-2] for x in data])

with open("nextseq_550.txt") as to_compare:
    data2 = to_compare.readlines()
    for line in data2:
        read_depth = line.split()[1]
        if read_depth in data:
            output.write(line)
