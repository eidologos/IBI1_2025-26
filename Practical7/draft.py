from Bio import SeqIO
import re

# 输入/输出文件路径（请根据实际文件位置修改！）
input_fa = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_fa = "stop_genes.fa"
# 定义起始密码子和终止密码子
start_codon = 'ATG'
stop_codons = {'TAA', 'TAG', 'TGA'}

# 存储符合条件的基因（id: (基因名, 存在的终止密码子, 序列)）
valid_genes = {}

# 读取FASTA文件，处理每个序列
for record in SeqIO.parse(input_fa, "fasta"):
    # 提取基因名（FASTA标题行第一个空格前的内容，为标准基因名）
    gene_name = re.split(r'\s+', record.description)[0]
    seq = str(record.seq).upper()  # 序列转大写，避免大小写问题
    found_stops = set()  # 存储该基因中找到的读码框内终止密码子

    # 寻找所有ATG起始位点，遍历读码框
    for start_pos in range(len(seq) - 2):
        if seq[start_pos:start_pos+3] == start_codon:
            # 从起始密码子后按3个一组读密码子，寻找终止密码子
            for pos in range(start_pos + 3, len(seq) - 2, 3):
                codon = seq[pos:pos+3]
                if codon in stop_codons:
                    found_stops.add(codon)
                    break  # 找到一个即可，无需继续遍历当前读码框
        if found_stops:  # 已找到至少一个终止密码子，停止遍历该基因
            break

    # 仅保留至少含一个读码框内终止密码子的基因
    if found_stops:
        # 标题行格式：>基因名 [终止密码子1,终止密码子2,...]
        new_id = f"{gene_name} [{','.join(sorted(found_stops))}]"
        record.id = new_id
        record.description = new_id  # 清空原描述，仅保留指定内容
        valid_genes[new_id] = record

# 将符合条件的基因写入新FASTA文件
SeqIO.write(valid_genes.values(), output_fa, "fasta")
print(f"处理完成！共找到 {len(valid_genes)} 个含读码框内终止密码子的基因，结果已保存至 {output_fa}")