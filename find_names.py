import spacy

def names_processing(text):
    try:
        nlp = spacy.load('en_core_web_md')
        prev_names = []
        for name in text:
            if '0123456789' not in text:
                prev_names.append(name)
        doc = nlp(''.join(prev_names))
        names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        return names[0].split() if names else []
    except Exception as e:
        print(f"Ошибка обработки текста: {e}")
        return []