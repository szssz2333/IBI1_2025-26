import matplotlib.pyplot as plt

gene={'TP53':12.4,'EFGR':15.1,'BRCA1':8.2,'PTEN':5.3,'ESR1':10.7}
print(gene)
gene['MYC']=11.6
print(gene)

x=gene.keys()
y=gene.values()

plt.bar(x, y)
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels")
for j,k in zip(gene.keys(),gene.values()):
    plt.text(j,k,k,ha='center',va='bottom')
plt.show()

print(zip(gene.keys(),gene.values()))

gene_interested='TP53'
if gene_interested in x:
    print('expression is:',gene[gene_interested])
else:
    print('Error:No gene exists')

sum=0
avg=0
for i in y:
    sum+=i
avg=sum/len(gene)
print('average=',avg)