import docx 

doc= docx.Document('IE.docx')

wholedoc=""

for para in doc.paragraphs:
	wholedoc += para.text

print(wholedoc)
