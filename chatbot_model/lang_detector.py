from langdetect import detect, DetectorFactory
from googletrans import Translator

DetectorFactory.seed = 42  #For reproducibility of langdetect result

indian_languages = {'hi', 'en', 'mr', 'pa', 'ta', 'te', 'bn', 'gu', 'kn', 'ml'}

hinglish_keywords = ["aap", "kaun", "ho", "kya", "kyu", "kyun", "hai", "nahi", "kaise", "kaun", "bahut"]

def is_hinglish(query):
    query_tokens = query.lower().split()
    for token in query_tokens:
        if token in hinglish_keywords:
            return True
    return False

def detect_language(query):
    try:
        lang = detect(query)
        if lang not in indian_languages and is_hinglish(query):
            return 'hi'
        return lang if lang in indian_languages else 'en'
    except Exception as e:
        print(f"Error detecting language: {e}")
        return 'en'

def translate_to_english(query, query_lang):
    translator = Translator()
    if query_lang != 'en':
        translated = translator.translate(query, src=query_lang, dest='en')
        return translated.text
    return query

def translate_to_original(response, query_lang):
    translator = Translator()
    if query_lang != 'en':
        translated = translator.translate(response, src='en', dest=query_lang)
        return translated.text
    return response
    
def process_query(query):
    query_lang = detect_language(query)
    if query_lang:
        translated_query = translate_to_english(query, query_lang)
        return translated_query
    else:
        return query  

queries = [
    "aap kaun ho?",  #Hinglish
    "आप कौन हो?",   #Hindi
    "Who are you?",  #English
    "तू कोण आहेस?" #Marathi
]

#for query in queries:
    #print(f"\nOriginal query: {query}")
    #processed_query = process_query(query)
    #print(f"Processed query: {processed_query}")      