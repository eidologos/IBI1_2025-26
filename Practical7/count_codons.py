from Bio import SeqIO
import matplotlib.pyplot as plt
import os
from collections import defaultdict
input_fa = "/Users/zhanghanmeng/Downloads/IBI 1/IBI1_2025-26/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

# define start codon and stop codons
start_codon = "ATG"
all_stop_codons = {"TAA", "TAG", "TGA"}


while True:
    user_input = input("please enter the stop codon (TAA/TAG/TGA): ")
    if user_input in all_stop_codons:
        target_stop = user_input
        break
    print(f"❌ Invalid input! Please enter only one of TAA, TAG, or TGA, you entered: {user_input}")

print(f"already selected: {target_stop}")

# Store the counts of all codons
codon_counts = defaultdict(int)
# Count the number of genes that meet the criteria
gene_count = 0

for record in SeqIO.parse(input_fa, "fasta"):
    seq = str(record.seq).upper()
    seq_len = len(seq)
    # Store the ORF information for all target stop codons in this gene: (ORF length, list of upstream codons)
    orf_candidates = []

    # Traverse all possible ATG start sites
    for start_pos in range(seq_len - 2):
        if seq[start_pos : start_pos + 3] == start_codon:
            # Store the upstream codons for the current ORF
            upstream_codons = []
            # Traverse the sequence from the start site in steps of 3
            for pos in range(start_pos + 3, seq_len - 2, 3):
                codon = seq[pos : pos + 3]
                if codon == target_stop:
                    # Calculate the ORF length (including start and stop codons)
                    orf_length = pos + 3 - start_pos
                    # Store the ORF candidate information
                    orf_candidates.append((orf_length, upstream_codons.copy()))
                    break  
                else:
                    # If it's not the target stop codon, add it to the upstream codons list
                    upstream_codons.append(codon)

    # If there are ORF candidates for this gene, count the upstream codons of the longest ORF
    if orf_candidates:
        gene_count += 1
        # Sort the ORF candidates by length in descending order and take the longest one
        orf_candidates.sort(reverse=True, key=lambda x: x[0])
        longest_upstream = orf_candidates[0][1]
        # Count the codons in the longest ORF's upstream codon list
        for codon in longest_upstream:
            codon_counts[codon] += 1


print("statistical results：")
print(f"Total number of genes containing the stop codon {target_stop}: {gene_count}")
print(f"Termination codon {target_stop} upstream codon counts (sorted by frequency):")
#Output in descending order
sorted_codons = sorted(codon_counts.items(), key=lambda x: x[1], reverse=True)
for codon, count in sorted_codons:
    print(f"{codon}: {count}")

if not codon_counts:
    print(f"No gene containing the stop codon {target_stop} was found. Pie chart cannot be generated.")
else:
    max_count = max(codon_counts.values())
    threshold = max_count * 0.01
    # divide codons into main codons and others based on the threshold
    main_codons = {k: v for k, v in codon_counts.items() if v >= threshold}
    other_count = sum(v for k, v in codon_counts.items() if v < threshold)
    if other_count > 0:
        main_codons["Other"] = other_count

    plt.rcParams["font.sans-serif"] = ["PingFang SC", "SimHei", "Arial Unicode MS"]
    plt.rcParams["axes.unicode_minus"] = False

    # draw the pie chart
    fig, ax = plt.subplots(figsize=(14, 10), dpi=100)
    wedges, texts, autotexts = ax.pie(
        main_codons.values(),
        labels=main_codons.keys(),
        autopct="%1.1f%%",  
        startangle=90,
        labeldistance=1.05,
        pctdistance=0.9,
        textprops={"fontsize": 10}
    )

    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontweight("bold")
        autotext.set_fontsize(9)

    ax.set_title(f"stop codon {target_stop} upstream codon distribution\n(based on the longest ORF, total {gene_count} genes)",
        fontsize=16,
        pad=20,
        fontweight="bold")

    #save the pie chart to a file
    pie_filename = f"/Users/zhanghanmeng/Downloads/IBI 1/IBI1_2025-26/Practical7/{target_stop}_codon_distribution.png"
    plt.tight_layout()
    plt.savefig(pie_filename, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Pie chart generated and saved successfully!")
    print(f"saved to {pie_filename}")