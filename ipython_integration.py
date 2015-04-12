from pCore.LogFileWriter import XHTMLLogFileWriter
from IPython.display import HTML
from StringIO import StringIO
htmlLogFile = XHTMLLogFileWriter(fileName='/tmp/pdynamo_log')
htmlLogFile.file = StringIO()


# Display log as a table in IPython
def display_summary(pdynamo_object):
    value = ''
    try:
        items = iter(pdynamo_object)
    except:
        items = [pdynamo_object]
    for item in items:
        item.Summary(htmlLogFile)
        value += htmlLogFile.file.getvalue()
    htmlLogFile.file.truncate(0)
    return HTML(value)


# Display molecules
from pBabel import SMILES_FromSystem
from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole


def display_molecule(molecule):
    smiles_molecule = SMILES_FromSystem(molecule, log=None)
    return Chem.MolFromSmiles(smiles_molecule.replace('%', ''))

# print water.connectivity.bonds.ToMapping()
# print water.atoms.FormulaString()
