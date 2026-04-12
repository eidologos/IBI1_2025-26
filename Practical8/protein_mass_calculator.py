AMINO_ACID_MASS = {
    'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07,
    'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04,
    'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04,
    'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08}

def calculate_protein_mass(aa_sequence):
    total_mass = 0.0
    #Iterate through the amino acid sequence and accumulate the mass of each amino acid.
    for i in aa_sequence:
        if i not in AMINO_ACID_MASS:
            raise ValueError(f"Error: Unknown amino acid symbol '{i}', cannot calculate mass of '{aa_sequence}'!")
        total_mass += AMINO_ACID_MASS[i]
    return total_mass


if __name__ == '__main__':
    print("Test the Calculator's Function")
    #example1:simple valid sequence with known amino acids
    example1 = 'GAS'
    try:
        mass1 = calculate_protein_mass(example1)
        print(f"Total mass of the amino acid sequence {example1}:{mass1:.2f} amu")
    except ValueError as e:
        print(e)

    #example2:longer valid sequence with multiple amino acids, testing cumulative mass calculation
    example2 = 'MAKELGASFRY'  
    try:
        mass2 = calculate_protein_mass(example2)
        print(f"Total mass of the amino acid sequence {example2}:{mass2:.2f} amu")
    except ValueError as e:
        print(e)

    #example3:invalid sequence containing an unknown amino acid symbol 'X', testing error handling
    example3 = 'GAXP'
    try:
        mass3 = calculate_protein_mass(example3)
        print(f"Total mass of the amino acid sequence {example3}:{mass3:.2f} amu")
    except ValueError as e:
        print(e)