from pCore.LogFileWriter import XHTMLLogFileWriter
from IPython.display import HTML
from StringIO import StringIO
htmlLogFile = XHTMLLogFileWriter(fileName='tmpfile')
htmlLogFile.file = StringIO()

# Display log as a table in IPython
def display_summary(pdynamo_object):
    pdynamo_object.Summary(htmlLogFile)
    value = htmlLogFile.file.getvalue()
    htmlLogFile.file.truncate(0)
    return HTML(value)
    

# Display molecules
from pBabel import SMILES_FromSystem

from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Draw

def display_molecule(molecule):
    molecule.BondsFromCoordinates3()
    smiles_molecule = SMILES_FromSystem(molecule, log=None)
    return Chem.MolFromSmiles(smiles_molecule)
