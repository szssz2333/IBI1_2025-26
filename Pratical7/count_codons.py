import re
import matplotlib.pyplot as plt
gene_end,lengths=[],[]
seqs,codons={},{}
end_codon=input(f'Please enter an end codon(TGA/TAA/TAG)')
while end_codon not in ['TAA','TAG','TGA']:
    print('input error: not in range,you should type one in TGA/TAA/TAG')
    end_codon=input(f'Please enter an end codon(TGA/TAA/TAG)')
#input
with open(r"C:\Users\shizh\Desktop\IBI1\Week7 字符串\Pratical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') as f:
    new_f=re.split('>',f.read())
    while '' in new_f:
        new_f.remove('')
    for i in range(len(new_f)):                    
        new_f[i]=new_f[i].replace('\n','')
#split the file according to genes, remove \n
    for i in new_f:
        orf=re.search(r'ATG.*$',i.split()[-1])
        if not orf:
            continue
        eff_seq=orf.group()
        for j in range(0,len(eff_seq)-2,3):
            if eff_seq[j:j+3] == end_codon:
                gene_end.append(j)
        if not gene_end:       
            continue
        gene_name=i.split()[0]       
        eff_orf=eff_seq[0:max(gene_end)]        
        seqs[gene_name]=eff_orf                
        gene_end=[]        
#make a dic that contains names and sequences of required genes       
    for i in seqs.keys():  
        for j in range(0,len(seqs[i])-2,3):
            if seqs[i][j:j+3] not in ['TAA','TAG','TGA']:
                codons[seqs[i][j:j+3]]=codons.get(seqs[i][j:j+3],0)+1
#count the number of each codon in the sequence
print(f'the longest ORFs with the end codon of {end_codon} contains {len(seqs[i])//3} codons in total')
print(f'the detailed codons are listed below:')
for co,num in codons.items():
     print(f'{co}:{num}')
labels=list(codons.keys())
sizes=list(codons.values())
plt.figure(figsize=(16,16))
plt.pie(sizes,labels=labels,autopct='%0.1f%%',textprops={'fontsize':8},radius=1.25,labeldistance=1.08,pctdistance=0.88,startangle=90,)
plt.title(f'The codon distribution in tatal in the longest ORFs containing end codon of {end_codon}',fontweight='bold',fontsize=16,y=1.06)           
plt.tight_layout()  
plt.savefig(f'codon_distribution.png',dpi=300)
plt.close()
#draw the figure
print('successfully generated and saved the figure!')


