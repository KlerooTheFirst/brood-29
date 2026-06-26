import string

def filterText(text, criteria):
    return ''.join(ch for ch in text if ch not in criteria )

# Replace the letter j with i and u with v (standard historical runic simplifications).
def clean_input_text(raw_text):
    low_text = raw_text.lower()
    filtered = filterText(low_text,string.punctuation)
    runical_simplification = filtered.replace("j", "i").replace("u", "v")
    return runical_simplification.translate(str.maketrans('', '', '0123456789'))
    
    
