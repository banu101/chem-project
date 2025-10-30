from rdkit import Chem
# Define the molecule and the substructure to search for
benzene = Chem.MolFromSmiles("c1ccccc1")
ethanol = Chem.MolFromSmiles("CCO")
# Perform the substructure search
match = ethanol.HasSubstructMatch(benzene)
print("Benzene ring found in ethanol:", match)

#Code for the first step of the task
def substructure_search(list1, arg2):
    """
    Docstring: This is an optional documentation string explaining what the function does.
    """
    output = []
    base = Chem.MolFromSmiles(arg2)
    for _, value in enumerate(list1):
        search = Chem.MolFromSmiles(value)
        match = search.HasSubstructMatch(base)
        if match:
            output.append(value)

    return output

print(substructure_search(["CCO", "c1ccccc1", "CC(=O)O", "CC(=O)Oc1ccccc1C(=O)O"], "c1ccccc1"))