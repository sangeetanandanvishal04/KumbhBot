import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag
import string

"""try:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('averaged_perceptron_tagger_eng')
except:
    pass"""

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  

def preprocess_query(query):
    tokens = word_tokenize(query.lower())

    pos_tags = pos_tag(tokens)

    lemmatized_tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(pos_tag)) for token, pos_tag in pos_tags]

    tokens = [token for token in lemmatized_tokens if token not in string.punctuation]

    #tokens = [token for token in tokens if token.isalpha() and token not in stop_words]

    processed_tokens = [token for token in tokens if len(token) > 1]

    return processed_tokens

"""queries = [
    "Can you tell me about the hotel options near the river?",  # hotel_info
    "I need the train schedule for Kumbh Mela.",  # transportation_info
    "What's the weather like today?",  # weather_info
    "I need emergency help. Call the police!",  # emergency_help
    "What is the history of the Kumbh Mela?",  # general_info
]

for query in queries:
    print(f"\nOriginal query: {query}")
    cleaned_query = preprocess_query(query)
    print(f"Processed query: {cleaned_query}")"""