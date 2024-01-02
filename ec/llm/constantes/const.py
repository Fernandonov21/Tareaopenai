import re
TEMPERATURE = 0.1
MAX_TOKENS = 10

def CLEAN_TEXT(text:str) -> str:
    return re.sub(r'\s+', ' ', text).strip()
