from rdkit import Chem
# Define the molecule and the substructure to search for
benzene = Chem.MolFromSmiles("c1ccccc1")
ethanol = Chem.MolFromSmiles("CCO")
# Perform the substructure search
match = ethanol.HasSubstructMatch(benzene)
print("Benzene ring found in ethanol:", match)