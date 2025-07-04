import spacy

def names_processing(text):
    nlp = spacy.load('en_core_web_sm')
    text_cap = ' '.join(word.capitalize() if word.islower() else word for word in text.split())
    doc = nlp(text)
    names = [ent.text.lower() for ent in doc.ents if ent.label_ == "PERSON"]
    i = 1
    if names:
        print("Names:")
        for name in names:
            print(f"{i}. {name}")
            i += 1
    return None

if __name__ == "__main__":
    text = input("Enter text: ")
    names_processing(text)
