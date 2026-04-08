import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
input_fasta="Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
start_codon="ATG"
valid_stop_codons=["TAA","TAG","TGA"]
def parse_fasta(file_path):
    with open(file_path, "r") as f:
        sequences = {}
        current_seq_name = None
        current_seq = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_seq_name is not None:
                    sequences[current_seq_name] = "".join(current_seq)
                current_seq_name = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)
        if current_seq_name is not None:
            sequences[current_seq_name] = "".join(current_seq)
    return sequences
def find_stop_codons(sequences):
    stop_genes = {}
    for gene_name, sequence in sequences.items():
        if sequence.startswith(start_codon):
            for i in range(0, len(sequence)-2, 3):
                codon = sequence[i:i+3]
                if codon in valid_stop_codons:
                    stop_genes[gene_name] = sequence
                    break
    return stop_genes
sequences = parse_fasta(input_fasta)
stop_genes = find_stop_codons(sequences)
with open(output_fasta, "w") as f:
    for gene_name, sequence in stop_genes.items():
        f.write(f">{gene_name}\n")
        for i in range(0, len(sequence), 60):
            f.write(sequence[i:i+60] + "\n")
print(f"Number of genes with valid stop codons: {len(stop_genes)}")
labels = ["Genes with valid stop codons", "Genes without valid stop codons"]
sizes = [len(stop_genes), len(sequences) - len(stop_genes)]
colors = ["lightblue", "lightcoral"]
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
plt.axis("equal")
plt.title("Distribution of Genes with Valid Stop Codons")
plt.show()  