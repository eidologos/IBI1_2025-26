import matplotlib
matplotlib.use('MacOSX') 
import matplotlib.pyplot as plt
#Import the dictionary
gene_expression={"TP53":12.4,"EGFR":15.1,"BRCA1":8.2,"PTEN":5.3,"ESR1":10.7}
print("the initial dictionary:",gene_expression)
gene_expression["MYC"]=11.6 #add new gene
print("updated dictionary with MYC:",gene_expression)
#draw the bar chart
gene=list(gene_expression.keys())
exp_value=(gene_expression.values())
plt.bar(gene,exp_value,color="blue")
plt.title("Gene Expression Level")
plt.xlabel("Gene name")
plt.xticks(rotation=0)
plt.ylabel("Expression Level")
plt.tight_layout()
plt.show()

#modifiable variable:gene of interest
gene_interest="TP53"
if gene_interest in gene_expression:
    print("the expression of",gene_interest,"is :",gene_expression[gene_interest])
else:
    print(gene_interest,"is not in the dictionary")
average=sum(exp_value)/len(exp_value) #calculate the average value
print("the average of gene expression values is:",average)





