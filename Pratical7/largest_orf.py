seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
end_codon=['UAA','UAG','UGA']
max_length,length=0,0
sq=''
for i in range(len(seq)-2):
    if seq[i:i+3]=='AUG':
        for j in range(i,len(seq)-2,3):
            sq=seq[j:j+3]
            if sq in end_codon:
                length=j-i+3
            if length>max_length:
                max_length=length
print(f"The longest ORF has {max_length} nucleotides")
