from transformers import pipeline

ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

entities = ner(text)

personas = []
organizacijas = []

for entity in entities:
    if entity['entity'] == 'B-PER':
        personas.append(entity['word'])
    elif entity['entity'] == 'B-ORG':
        organizacijas.append(entity['word'])

print("Personvārdi:", personas)
print("Organizācijas:", organizacijas)
