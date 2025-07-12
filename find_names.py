import spacy

def names_processing(text):
    try:
        nlp = spacy.load('en_core_web_md')
        # Filter out numeric characters from text for better name detection
        filtered_text = ''.join(char if not char.isdigit() else ' ' for char in text)
        doc = nlp(filtered_text)
        names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        # Return all found names as a flat list
        all_names = []
        for name in names:
            all_names.extend(name.split())
        return list(set(all_names))  # Remove duplicates
    except Exception as e:
        print(f"Ошибка обработки текста: {e}")
        return []
