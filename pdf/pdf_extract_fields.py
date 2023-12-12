#! /usr/bin/env python3

# import PyPDF2

# with open('DnD_5E_CharacterSheet_FormFillable.pdf', 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     form_data = reader.get_form_text_fields()

# import json

# form_data_json = json.dumps(form_data)

# with open('extracted_character_sheet_form_data.json', 'w') as json_file:
#     json_file.write(form_data_json)

import PyPDF2,json

pdf_file = 'DnD_5E_CharacterSheet_FormFillable.pdf'
json_file = 'extracted_character_sheet_form_data.json'

def extract_data_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        fields = pdf.get_form_text_fields()
        return fields

form_data = extract_data_from_pdf(pdf_file)
form_data_json = json.dumps(form_data)

with open(json_file, 'w') as json_file:
    json_file.write(form_data_json)
