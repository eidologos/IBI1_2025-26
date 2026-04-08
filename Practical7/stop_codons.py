from Bio import SeqIO
import re

input_fa = "/Users/zhanghanmeng/Downloads/IBI 1/IBI1_2025-26/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_fa = "/Users/zhanghanmeng/Downloads/IBI 1/IBI1_2025-26/Practical7/stop_genes.fa"
# define start codon and stop codons
start_codon = 'ATG'
stop_codons = {'TAA', 'TAG', 'TGA'}

# Store valid genes 
valid_genes = []

# Process each gene in the input FASTA file
for record in SeqIO.parse(input_fa, "fasta"):
    gene_name = record.description.split()[0]
    seq = str(record.seq).upper()
    found_stops = set()

    seq_len = len(seq)
    for start_pos in range(seq_len - 2):
        if seq[start_pos : start_pos + 3] == start_codon:
            # record the upstream codons for the current ORF
            for pos in range(start_pos + 3, seq_len - 2, 3):
                codon = seq[pos : pos + 3]
                if codon in stop_codons:
                    found_stops.add(codon)
                    break  # found a stop codon, break out of the current ORF
   
    if found_stops:
        stops_str = ",".join(sorted(found_stops))
        new_header = f"{gene_name}:{stops_str}"

        
        record.description = new_header
        record.id = ""
        valid_genes.append(record)  

# Write the valid genes to the output FASTA file
SeqIO.write(valid_genes, output_fa, "fasta")

print("Processing completed!")
print(f"Total genes found with stop codons in ORFs: {len(valid_genes)}")
print(f"Results saved to: {output_fa}")