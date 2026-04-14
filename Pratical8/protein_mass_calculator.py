def calculate_protein_mass(sequence):
    amino_acid_masses = {
        'G': 57.02,
        'A': 71.04,
        'S': 87.03,
        'P': 97.05,
        'V': 99.07,
        'T': 101.05,
        'C': 103.01,
        'I': 113.08,
        'L': 113.08,
        'N': 114.04,
        'D': 115.03,
        'Q': 128.06,
        'K': 128.09,
        'E': 129.04,
        'M': 131.04,
        'H': 137.06,
        'F': 147.07,
        'R': 156.10,
        'Y': 163.06,
        'W': 186.08
    }
    
    total_mass = 0
    
    for amino_acid in sequence:
        if amino_acid not in amino_acid_masses:
            raise ValueError(f'Amino acid {amino_acid} is not found')
        else:
            total_mass += amino_acid_masses[amino_acid]
    
    return total_mass

sequence = input("Please enter the amino acid sequence: ")

try: 
    total_mass=calculate_protein_mass(sequence)
    print(f'The total mass is {total_mass}')
except ValueError as e:
    print(f'Error: {e}')

# Examples

sequence1='AC'

