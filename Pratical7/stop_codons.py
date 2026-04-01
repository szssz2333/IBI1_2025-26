import re
gene_name=''
gene_end_codon,gene_end=[],[]
with open(r"C:\Users\shizh\Desktop\IBI1\Week7 字符串\Pratical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') as f, open(r'C:\Users\shizh\Desktop\IBI1\Week7 字符串\Pratical7\stop_genes.fa','w') as out:

#open file and ready to write the new file    
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
            if eff_seq[j:j+3] in ['TAA','TAG','TGA']:
                gene_end_codon.append(eff_seq[j:j+3])
                gene_end.append(j)
        if not gene_end_codon:       
            continue       
        gene_name=i.split()[0]
        gene_end_codon=set(gene_end_codon)
        out.write(f">{gene_name} {" ".join(gene_end_codon)}\n{eff_seq[0:max(gene_end)]}\n")
        gene_end_codon,gene_end=[],[]

print('successfully generated the file')



