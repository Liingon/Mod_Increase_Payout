#!/usr/bin/python

import os
import xml.etree.ElementTree as ET

gamePath = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Project Hospital"
diagnosePath = "\\ProjectHospital_Data\\StreamingAssets\\Database\\Diagnoses"
path = gamePath + diagnosePath
modifier = 1.5

# Loop through all Dignoses files
def loopFiles( path ):
    for file in os.listdir(path):
        if file.startswith("Diagnoses") and file.endswith(".xml"):
            parseFile(os.path.join(path, file))

# Find all instances of GameDBMedicalCondition, increase InsurancePayment, then print to output file
def parseFile( file ):
    filename = os.path.basename(file)
    tree = ET.parse( file )
    root = tree.getroot()
    
    for elem in root.iter('GameDBMedicalCondition'):
        InsurancePayment = elem.find('InsurancePayment')
        InsurancePayment.text = modify(InsurancePayment.text)
    
    tree.write("mod_content/Database/Mod" + filename)

# Modify a value
def modify( value ):
    value = int(value)
    value = value * modifier
    return str(int(value))

loopFiles( path )