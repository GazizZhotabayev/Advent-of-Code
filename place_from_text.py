import csv
with open('C:\\Users\\GazizZhotabayev\\Desktop\\Transaction Data.csv') as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    next(reader, None)
    txt = [row[0] for row in reader]
    

import spacy
nlp = spacy.load("en_core_web_sm")

BLOCKWORDS = '''redkite imperial halfords diageo kingfisher uber hotel'''.split()

places = []
for i, line in enumerate(txt):
    
    #remove punctuation, leave only alphanumeric chars & whitespace
    line = ''.join(e if e.isalnum() else ' ' for e in line )  
    
    #remove words which confuse Spacy
    line = ' '.join([word for word in line.split() if word.lower() not in BLOCKWORDS])
    
    doc = nlp(line)
    
    #extract geo-political entities
    extract = ' '.join(f'{ent.text[0].upper()}{ent.text[1:]}' for ent in doc.ents if ent.label_ == 'GPE')
    places.append(' '.join(set(extract.split())))


with open('C:\\Users\\GazizZhotabayev\\Desktop\\Cleansed Transaction Data.csv', "wt", newline='') as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerow(["Original", "Places Extracted"])  # write header
    for transaction, place in zip(txt, places):
        writer.writerow([transaction, place])