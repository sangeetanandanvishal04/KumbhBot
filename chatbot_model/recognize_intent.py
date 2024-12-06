from fuzzywuzzy import fuzz

intent_keywords = {
    "event_info": ["event", "function", "sangam"],
    "weather_info": [
        "weather", "forecast", "temperature", "rain", "climate", "sunny", 
        "cloudy", "wind", "storm", "humidity", "cold", "sunrise", "sunset", 
        "flood"
    ],
    "pincodes": ["pincode", "pincodes"],
    "transportation_info": [
        "train", "trains", "metro", "express"
    ],
    "emergency_help": [
        "help", "emergency", "police", "ambulance", "doctor", "hospital", 
        "medical", "fire", "rescue", "lost", "security", "vaccination", 
        "safety", "aid", "contact", "COVID-19", "precautions", "healthcare"
    ],
    "hotel_info": [
        "hotel", "stay", "accommodation", "room", "guesthouse", "tent", 
        "campsite", "lodge", "food", "house", "restaurant", "cafes", 
        "dining", "langar", "meals"
    ],
    "general_info": [
        "mela", "history", "festival", "dates", "schedule", 
        "location", "pilgrimage", "tradition", "culture", "significance", 
        "kumbh", "shahi", "bath", "snan", "akharas", "attractions", 
        "people", "attendance", "duration", "ritual", "bathing", "river", "timings", 
        "participate", "participation", "parking", "disabled", "rent", "schedule", "guidelines", 
        "celebrate", "transportation", "transport", "bus", "route", "shuttle", "taxi", "cab", "flight", 
        "airport", "travel", "elderly", "bike", "car"
    ]
}

def detect_intent(query_tokens, threshold=90):
    #First, check for exact matches
    for intent, keywords in intent_keywords.items():
        for keyword in keywords:
            if keyword.lower() in query_tokens:
                return intent
    
    #Fuzzy matching if no exact match is found
    for intent, keywords in intent_keywords.items():
        for keyword in keywords:
            for token in query_tokens:
                match_score = fuzz.partial_ratio(keyword.lower(), token)
                if match_score >= threshold:
                    return intent
    return "general_info"

"""queries = [
    "Can you tell me about the hotel options near the river?",  # hotel_info
    "I need the train schedule for Kumbh Mela.",  # transportation_info
    "What's the weather like today?",  # weather_info
    "I need emergency help. Call the police!",  # emergency_help
    "What is the history of the Kumbh Mela?",  # general_info
    
    # General Information
    "What is Kumbh Mela, and why is it celebrated?",  # general_info
    "When will the Kumbh Mela take place in Prayagraj?",  # general_info
    "What is the significance of the Kumbh Mela in Hindu culture?",  # general_info
    "How long does the Kumbh Mela last?",  # general_info
    "What are the main attractions at the Kumbh Mela?",  # general_info
    "Where is Kumbh Mela held in Prayagraj?",  # general_info
    "What is the difference between the Ardh Kumbh, Maha Kumbh, and Kumbh Mela?",  # general_info
    "What is the history of Kumbh Mela in Prayagraj?",  # general_info
    "How many people attend the Kumbh Mela?",  # general_info
    "What safety measures are in place during the Kumbh Mela?",  # general_info,
    
    # Rituals and Bathing (Snan)
    "What are the important bathing dates during the Kumbh Mela?",  # general_info(dates, time etc)
    "What is Shahi Snan, and who participates in it?",  # general_info
    "What is the significance of bathing at the Sangam during Kumbh Mela?",  # general_info
    "What is the best time to take a dip in the river at Kumbh Mela?",  # general_info
    "Is there a specific ritual I should follow during the bathing?",  # general_info
    "Which river should I bathe in during the Kumbh Mela?",  # general_info
    "How can I ensure my safety while bathing at the Kumbh Mela?",  # general_info
    "Do I need to register for the Shahi Snan or other rituals?",  # general_info
    "Can women participate in the bathing rituals?",  # general_info
    "What are the key Akharas and how do they participate in Kumbh Mela?",  # general_info
    
    # Travel and Transportation
    "How can I reach Prayagraj for the Kumbh Mela?",  # general_info
    "What are the nearest airports to Prayagraj?",  # general_info
    "Are there special trains or buses to Prayagraj for Kumbh Mela?",  # general_info
    "How can I travel within the Kumbh Mela area?",  # general_info
    "Are there parking facilities available near the Kumbh Mela site?",  # general_info
    "Can I book a private taxi or cab service in Prayagraj?",  # general_info
    "How can I navigate the Kumbh Mela grounds without getting lost?",  # general_info
    "Is there public transportation available from the Kumbh Mela site to nearby hotels?",  # general_info
    "Are there special transportation services for the elderly or disabled?",  # general_info
    "Can I rent a bike or car for local transportation in Prayagraj?",  # general_info
]

true_intents = [
    "hotel_info",  # Query 1
    "transportation_info",  # Query 2
    "weather_info",  # Query 3
    "emergency_help",  # Query 4
    "general_info",  # Query 5
    
    # General Information
    "general_info",  # Query 6
    "general_info",  # Query 7
    "general_info",  # Query 8
    "general_info",  # Query 9
    "general_info",  # Query 10
    "general_info",  # Query 11
    "general_info",  # Query 12
    "general_info",  # Query 13
    "general_info",  # Query 14
    "general_info",  # Query 15
    
    # Rituals and Bathing (Snan)
    "general_info",  # Query 16
    "general_info",  # Query 17
    "general_info",  # Query 18
    "general_info",  # Query 19
    "general_info",  # Query 20
    "general_info",  # Query 21
    "general_info",  # Query 22
    "general_info",  # Query 23
    "general_info",  # Query 24
    
    # Travel and Transportation
    "transportation_info",  # Query 25
    "transportation_info",  # Query 26
    "transportation_info",  # Query 27
    "transportation_info",  # Query 28
    "transportation_info",  # Query 29
    "transportation_info",  # Query 30
    "transportation_info",  # Query 31
    "transportation_info",  # Query 32
    "transportation_info",  # Query 33
    "transportation_info"   # Query 34
]

# Test the intent recognizer and calculate accuracy
correct_predictions = 0

for query, true_intent in zip(queries, true_intents):
    query_tokens = word_tokenize(query.lower())
    detected_intent = detect_intent(query_tokens)
    
    print(f"\nOriginal query: {query}")
    print(f"True intent: {true_intent}")
    print(f"Detected intent: {detected_intent}")
    
    if detected_intent == true_intent:
        correct_predictions += 1

# Calculate accuracy
total_queries = len(queries)
accuracy = (correct_predictions / total_queries) * 100
print(f"\nAccuracy of intent recognizer: {accuracy:.2f}%")"""