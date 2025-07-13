import spacy
from rich.console import Console

console = Console()

def names_processing(text):
    """Extract person names from text using spaCy NLP.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        list: List of unique person names found in text
    """
    if not text or not isinstance(text, str):
        return []
        
    try:
        # Try to load the preferred model first
        try:
            nlp = spacy.load('en_core_web_md')
        except OSError:
            console.print("⚠️  en_core_web_md model not found, trying en_core_web_sm...", style="yellow")
            try:
                nlp = spacy.load('en_core_web_sm')
            except OSError:
                console.print("⚠️  No spaCy English model found, trying basic model...", style="yellow")
                try:
                    nlp = spacy.load('en')
                except OSError:
                    console.print("❌ No spaCy English model available. Install with: python -m spacy download en_core_web_sm", style="red")
                    return []
        
        # Filter out numeric characters from text for better name detection
        filtered_text = ''.join(char if not char.isdigit() else ' ' for char in text)
        
        # Process text with spaCy
        doc = nlp(filtered_text)
        names = [ent.text.strip() for ent in doc.ents if ent.label_ == "PERSON" and ent.text.strip()]
        
        # Return all found names as a flat list
        all_names = []
        for name in names:
            # Split compound names and add individual parts
            name_parts = [part.strip() for part in name.split() if part.strip().isalpha() and len(part.strip()) > 1]
            all_names.extend(name_parts)
            
        # Remove duplicates and return
        unique_names = list(set(all_names))
        return unique_names
        
    except Exception as e:
        console.print(f"❌ Error processing text for names: {e}", style="red")
        return []
