from rdkit import Chem


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

