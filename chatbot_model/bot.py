from .lang_detector import detect_language, translate_to_english, translate_to_original
from .query_cleanup import preprocess_query
from .recognize_intent import detect_intent
from .generate_response import generate_response

def process_user_query(user_query):
    query_lang = detect_language(query=user_query)
    translated_query = translate_to_english(query=user_query, 
                                            query_lang=query_lang)

    cleaned_query_tokens = preprocess_query(query=translated_query)

    detected_intent = detect_intent(query_tokens=cleaned_query_tokens)
    #print(f"Intent recognized: {detected_intent}")
    response = generate_response(user_query_tokens=cleaned_query_tokens, 
                                 user_query=translated_query, 
                                 intent=detected_intent)
    
    if query_lang != 'en':
        if 'output' in response:
            response['output'] = translate_to_original(response['output'], query_lang)
        if 'Tips' in response:
            response['Tips'] = translate_to_original(response['Tips'], query_lang)
        if 'Suggestions' in response:
            if "http" in response['Suggestions']:
                parts = response['Suggestions'].split("http", 1)
                translated_text = translate_to_original(parts[0], query_lang)
                response['Suggestions'] = translated_text + " http" + parts[1]
            else:
                response['Suggestions'] = translate_to_original(response['Suggestions'], query_lang)

    return response

"""user_query = "Maha Kumbh Mela ke baare mein batao?"
print(f"User query: {user_query}")
response = process_user_query(user_query)
print(f"Bot response: {response}")"""