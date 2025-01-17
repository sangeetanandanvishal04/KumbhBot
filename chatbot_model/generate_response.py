import requests 
import json
import re

pincode_data = {
    "Achhola": "212303",
    "Agriculture Institute": "211007",
    "Ahmadganj": "211003",
    "Ahmedpur Asrauli": "212208",
    "Ahmedpur Pawan": "212208",
    "Akorha": "212301",
    "Aladadpur": "228411",
    "Alam Chand": "212213",
    "Allahabad Fort": "211005",
    "Allahabad Kty.": "211002",
    "Allahabad New Cantt.": "211001",
    "Allapur": "211006",
    "Alopi Bagh": "211006",
    "Andawa": "211007",
    "Annapurna": "211003",
    "Atala": "211003",
    "Aurangabad": "211003",
    "Badraon": "212106",
    "Baharia": "212109",
    "Bamrauli": "211012",
    "Bamhrauli": "212201",
    "Beli": "211004",
    "Beli Colony": "211004",
    "Bhagwatpur": "211012",
    "Bhita": "211003",
    "Bilhaur": "209202",
    "Chak Jagadishpur": "211008",
    "Chak Mundera": "211011",
    "Chaufatka": "211004",
    "Civil Lines": "211001",
    "Colonelganj": "211002",
    "Dandi": "211008",
    "Daraganj": "211006",
    "Dhoomanganj": "211011",
    "Doomiaganj": "211011",
    "Gauhania": "212507",
    "Ghodedeeh": "211008",
    "Gohari": "211011",
    "Govindpur": "211004",
    "GTB Nagar": "211011",
    "Gulabganj": "211002",
    "Handia": "221503",
    "Himmatganj": "211002",
    "Iradatganj": "211004",
    "Jhusi": "211019",
    "Kalindipuram": "211004",
    "Kareli": "211016",
    "Katra": "211002",
    "Keedganj": "211003",
    "Kidwai Nagar": "211008",
    "Koraon": "212306",
    "Lukerganj": "211001",
    "Mau Aima": "212507",
    "Meja": "212303",
    "Mumtaz Nagar": "211003",
    "Mutthiganj": "211003",
    "Naini": "211008",
    "Niranjanpur": "211005",
    "Phaphamau": "211013",
    "Prayagraj": "211001",
    "Prayagraj Chowk": "211003",
    "Rajapur": "211002",
    "Rajrooppur": "211011",
    "Rambagh": "211003",
    "Rewa Road": "211008",
    "Sadar Bazar": "211001",
    "Shahganj": "211003",
    "Shivkuti": "211008",
    "Soraon": "212502",
    "Subedarganj": "211011",
    "Tagore Town": "211002",
    "Teliyarganj": "211004",
    "Triveni Road": "211019",
    "Zero Road": "211003",
    "Bamrauli Airforce Station": "211012",
    "Arail": "211008",
    "Begumsarai": "211011",
    "Baraut": "221502",
    "Chheoki": "211007",
    "Gangotri Nagar": "211019",
    "Govindpur Colony": "211004",
    "Indira Nagar": "211011",
    "Madhopur": "212402",
    "Mandhata": "212303",
    "Mandauri": "212303",
    "Manauri Airforce Station": "212212",
    "New Yamuna Bridge": "211003",
    "Sulem Sarai": "211011",
    "Chowk": "211003",
    "Manjhanpur": "212206",
    "Karchana": "212301",
    "Kydganj": "211003",
    "Karachhana": "211004",
    "Sirsa": "212302",
    "Khaspur": "221502",
    "Kaurihar": "212208",
    "Kotwa": "211003",
    "Lalgopalganj": "212412",
    "Manoharpur": "212208",
    "Nandipur": "211006",
    "Nayapurwa": "211006",
    "Rajatalab": "221311",
    "Sarainayat": "212403",
    "Sikandra": "212217",
    "Sundarpur": "221005",
    "Uttam Nagar": "211002"
}

verification_links = {
    "hotel_info" : "https://prayagraj.nic.in/accommodation/",
    "transportation_info" : "https://www.irctc.co.in/nget/train-search",
    "weather_info" : "https://www.accuweather.com/en/in/up/uttar-pradesh-weather#google_vignette",
    "general_info" : "https://prayagraj.nic.in/kumbh2019/",
    "emergency_help" : "https://prayagraj.nic.in/helpline/",
    "pincodes" : "https://prayagraj.nic.in/std-pin-codes/",
}

helplines = {
    "CM Helpline": "1076",
    "Police Control Room (DIAL 112)": "112",
    "Child Helpline": "1098",
    "Women Helpline": "1091",
    "Crime Stopper": "1090",
    "Ambulance Helpline (General)": "102",
    "Ambulance Helpline (Emergency)": "108"
}

zones = {
    "zone_1": ["Triveni Sangam", "Saraswati Ghat", "Ram Ghat", "Naini Bridge", "Maha Kumbh"],
    "zone_2": ["Bade Hanuman Ji Temple", "Patalpuri Temple", "Siddheshwari Peeth", "Mankameshwar Temple"],
    "zone_3": ["Allahabad Fort", "Anand Bhawan Museum", "Chandra Shekhar Azad Park", "Khusro Bagh"],
    "zone_4": ["Parmarth Niketan Ashram", "Swaminarayan Ashram", "Shringverpur", "Akshayavat"],
    "zone_5": ["Nag Vasuki Temple", "Alopi Devi Temple", "Mata Bharadwaj Temple", "Sankat Mochan Hanuman Temple"]
}

#After finalising everthing we put the events inside PostgreSQL database.
events = {
    "zone_1": ["Shahi Snan at 7:00 AM on Triveni Sangam", "Evening aartis at 5:00 PM at Ram Ghat"],
    "zone_2": ["Special poojas and blessings ceremonies", "Gatherings honoring Shiva and Hanuman"],
    "zone_3": ["Historical exhibitions from 7:00 AM to 6:00 PM in Allahabad Fort", 
               "Educational tours in Anand Bhawan Museum", 
               "Cultural events in Khusro Bagh during daytime"],
    "zone_4": ["Meditation sessions from 7:00 AM to 9:00 AM in Parmarth Niketan Ashram", 
               "Spiritual learning sessions in Swaminarayan Ashram", 
               "Evening satsangs in Parmarth Niketan Ashram"],
    "zone_5": ["Ceremonies dedicated to Nag Vasuki in morning", 
               "Special blessings and poojas in Alopi Devi Temple"]
}

def formatized_response(status, output, tips=None, suggestions=None):
    if tips is None:
        tips = "No specific tips available."

    if suggestions is None:
        suggestions = "Ask query related to Maha Kumbh Mela 2025 https://prayagraj.nic.in/tourism/"    

    response = {
        "status": status,
        "output": output,
        "Tips": tips,
        "Suggestions": suggestions
    }
    return response

def fallback_response():
    output = "I'm sorry, I didn't quite catch that."
    tips = "Try asking about hotels, transportation, weather, or emergency services."
    suggestions = f"Visit our Kumbh Mela website for more help: {verification_links['general_info']}"

    return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

def extract_location_and_get_events(user_query):
    potential_locations = [loc for zone in zones.values() for loc in zone]
    found_location = None

    for loc in potential_locations:
        if re.search(rf'\b{re.escape(loc)}\b', user_query, re.IGNORECASE):
            found_location = loc
            break

    if found_location:
        for zone, locations in zones.items():
            if found_location in locations:
                event_list = events.get(zone, [])
                output = f"{found_location} lies inside {zone.replace('_', ' ')}."

                if event_list:
                    output += " These are the events occurred in this zone:\n"
                    output += ", \n".join(event_list)
                else:
                    output += " No specific events are listed for this zone."
                
                tips = "Use your nearby location or temple name to get event details near the location."
                suggestions = f"Visit our Kumbh Mela website for more help: {verification_links['general_info']}"
                return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)
    else:
        output = "Oops!, We are unable to recognize the location or temple name."
        tips = "Try to use your nearby location name or temple name to get event details near the location."
        suggestions = f"Visit our Kumbh Mela website for more help: {verification_links['general_info']}"
        return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

def get_emergency_help():
    helpline_info = "\n".join([f"{name}: {number}" for name, number in helplines.items()])

    output = f"Emergency helpline numbers: {helpline_info}"
    tips = "Save these numbers for quick access during emergencies."
    suggestions = f"Get more helpline numbers: {verification_links["emergency_help"]}."

    return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

def get_pincode_details(user_query_tokens):
    ignore_tokens = {"pincode", "of", "in", "for", "the", "is", "what", "tell", "me", 
                     "be", "location", "give"}

    filtered_tokens = [word for word in user_query_tokens if word not in ignore_tokens]

    for location in pincode_data:
        if all(token in location.lower() for token in filtered_tokens):

            output = f"Pincode of the {location}: {pincode_data[location]}."
            tips = "Ensure correct spelling of location names for better results."
            suggestions = f"Find other pincodes here: {verification_links['pincodes']}"

            return formatized_response("success", output, tips, suggestions)

    output = f"Oops!, We could not find the pincode for that {location}.\n"
    tips = "Ensure correct spelling of location names for better results."
    suggestions = f"Visit the following link for more details: {verification_links['pincodes']}"

    return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

#user_query = ["pincode", "of", "akorha"]
#user_query = ["what", "is", "the", "pincode", "for", "new", "yamuna", "bridge"]
#output = get_pincode_details(user_query_tokens=user_query)
#print(output)

def get_weather_condition_description(condition):
    if condition < 300:
        return "Thunderstorms expected. Stay indoors and avoid open areas."
    elif condition < 400:
        return "Light rain expected. Consider carrying an umbrella."
    elif condition < 600:
        return "Rainy weather forecasted. Wear waterproof clothes and shoes."
    elif condition < 700:
        return "Snowfall expected. Dress warmly if you're going outside."
    elif condition < 800:
        return "Foggy weather. Drive carefully and use fog lights if necessary."
    elif condition == 800:
        return "Clear sky and sunny weather. Enjoy outdoor activities."
    elif condition <= 804:
        return "Partly cloudy or overcast. You may not need sunglasses."
    else:
        return "Unpredictable weather. Check the forecast frequently."

def get_clothing_recommendation(temp):
    if temp > 25:
        return (
            "It's quite warm! Stay cool with light clothes like shorts and T-shirts. "
            "Consider carrying water to stay hydrated."
        )
    elif temp > 20:
        return (
            "The weather is moderate. A light jacket or sweater should be enough."
        )
    elif temp < 10:
        return (
            "It's cold outside! Bundle up with a scarf, gloves, and warm layers."
        )
    else:
        return (
            "The weather is unpredictable. Carry a sweater or light jacket just in case."
        )

def get_city_weather(city_name):
    weather_api_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "c97c53a710476e95969e857056e4d90c"

    params = {"q": city_name, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(weather_api_url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            return (
                f"Error: {data.get('message', 'Weather information not available. Please try again later.')}"
            )

        weather = data["main"]
        condition = data["weather"][0]["id"]
        description = data["weather"][0]["description"].capitalize()
        temp = weather["temp"]

        output = f"Temperature of {city_name}: {temp}°C. Description of condition of city: {description}."
        tips = get_weather_condition_description(condition)
        suggestions = f"{get_clothing_recommendation(temp)}."
        
        return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

    except Exception as e:
        output = f"Oops!, We are unable to get the weather report of the {city_name}"
        tips = "Try asking about hotels, transportation, or emergency services."
        suggestions = f"To get more detailed report, Visit: {verification_links['weather_info']}"

        return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

def search_hotels(user_query):
    try:
        URL = "http://127.0.0.1:8000/search-hotels"
        payload = {"user_query": user_query}

        response = requests.post(
            url=URL, 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(payload)
        )

        if response.status_code == 200:
            json_response = response.json()
            hotel_response = json_response.get('response')
            
            tips = "Make sure to book early to avoid the rush."
            suggestions = f"Explore more hotels here: {verification_links['hotel_info']}"

            return formatized_response(status="success", output=hotel_response, tips=tips, suggestions=suggestions)
            
        else:
            output = f"Oops!, Unable to find hotels matching your query."
            tips = "Try searching in different way to get result."
            suggestions = f"Check available accommodations here: {verification_links['hotel_info']}"

            return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)
    
    except requests.ConnectionError:
        output = "Check your internet connection."
        return formatized_response(status="failure", output=output)
    
    except Exception as e:
        output = "Oops!, Something ususual happen. Ask later."
        tips = "Try searching in different way to get result."
        suggestions = f"Check available accommodations here: {verification_links['hotel_info']}"
        return formatized_response(status="failure", output=output, suggestions=suggestions)

#response = search_hotels("family friendly hotels in Prayagraj")
#print(response)

#Used when train name or number is found.
def get_response_with_name_number_of_trains(payload):
    url = "https://trains.p.rapidapi.com/v1/railways/trains/india"
    headers = {
        "x-rapidapi-key": "148445fc61msh5cc83372fbe7949p1b2863jsn8772d938a54e",
        "x-rapidapi-host": "trains.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        train_data = response.json()
        output_list = []

        for train in train_data:
            train_info = {
                "Train Number": train.get("train_num"),
                "Train Name": train.get("name"),
                "From Station": train.get("train_from"),
                "To Station": train.get("train_to"),
                "Departure Time": train["data"].get("departTime"),
                "Arrival Time": train["data"].get("arriveTime"),
                "Classes Available": train["data"].get("classes"),
                "Running Days": [day for day, available in train["data"]["days"].items() if available == 1]
            }
            output_list.append(train_info)

        output = {
            "trains": output_list
        }
        tips = "Book tickets early to avoid waiting lists."
        suggestions = f"Use the Indian Railways website (IRCTC) to book tickets. Get more details: {verification_links['transportation_info']}"

        return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

def get_pnr_status(pnr):
    url = f"https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/{pnr}"
    headers = {
        "x-rapidapi-key": "148445fc61msh5cc83372fbe7949p1b2863jsn8772d938a54e",
        "x-rapidapi-host": "pnr-status-indian-railway.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        output = f"Here, pnr status of train is: {response.json()}"
        tips = "Keep your PNR number handy during travel."
        suggestions = "Use IRCTC app for quick PNR status updates."

        return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)
    else:
        output = "Failed to retrieve PNR status."
        tips = "Verify the PNR number is correct or not."
        suggestions = "Use IRCTC app for quick PNR status updates."

        return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

#Used when station name start and destination is found.(Not subscribed)
def get_train_from_and_to(start, destination):
    url = "https://indian-railways-train-fetcher.p.rapidapi.com/get_train_info"
    querystring = {"start": start, "destination": destination}
    headers = {
        "x-rapidapi-key": "148445fc61msh5cc83372fbe7949p1b2863jsn8772d938a54e",
        "x-rapidapi-host": "indian-railways-train-fetcher.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        trains = response.json()
        filtered_trains = [train for train in trains if train['train_to'] in ['ALD', 'Prayagraj', 'CPA']]

        if not filtered_trains:
            output = f"Sorry, We are unable to get train from {start} to Prayagraj(Allahabad)."
            tips = "Try to ask your query about train using name and number of the trains."
            suggestions = f"Use IRCTC app for quick PNR status updates. Get more details: {verification_links['transportation_info']}"

            return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

        result = []
        for train in filtered_trains:
            result.append({
                "Train Number": train["train_num"],
                "Train Name": train["name"],
                "Departure": train["data"]["departTime"],
                "Arrival": train["data"]["arriveTime"],
                "Classes Available": ', '.join(train["data"]["classes"]),
                "Operating Days": ', '.join([day for day, running in train["data"]["days"].items() if running == 1])
            })

        output = f"Here are some trains related to your query: {result}"
        tips = "Always double-check train schedules before travel."
        suggestions = "Visit IRCTC for more train details."

        return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

    else:
        output = f"Oops!, Something unusual happened to fetch the relevant details."
        tips = "Try to ask your query about train using name and number of the trains."
        suggestions = f"Visit IRCTC app to get more accurate details. Get more details: {verification_links['transportation_info']}"

        return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

def get_transport_info(tokens):
    train_name = None
    train_number = None
    source = None
    destination = None
    pnr = None

    valid_destinations = ['prayagraj', 'allahabad', 'kumbh']

    for i, token in enumerate(tokens):
        if token.isdigit() and len(token) == 5:
            train_number = token
        elif token.isdigit() and len(token) == 10:
            pnr = token
        elif token.lower() == 'express' and i >= 1:
            train_name = tokens[i-1]
        elif token.lower() in valid_destinations:
            destination = 'Prayagraj'
            if i >= 2:
                if tokens[i-1].lower() == "to":
                    source = tokens[i-2]
                elif i >= 3 and tokens[i-2].lower() == "to":
                    source = tokens[i-3]
            break

    if train_number:
        payload = {"search": train_number}
        return get_response_with_name_number_of_trains(payload=payload)
    elif train_name:
        payload = {"search": train_name}
        return get_response_with_name_number_of_trains(payload=payload)
    elif pnr:
        return get_pnr_status(pnr)
    elif source and destination:
        return get_train_from_and_to(source, destination)
    else:
        return fallback_response()

#tokens = ['Can', 'take', 'train', '11056', 'to', 'Prayagraj']
#tokens = ['Show', 'me', 'AC', '2A', 'trains', 'from', 'gorakhpur', 'to', 'prayagraj']
#tokens = ['Does', 'the', 'Chauri', 'Express', 'go', 'to', 'Prayagraj']
#print(get_transport_info(tokens))

def get_general_info(user_query: str):
    url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"
    payload = {
        "messages": [{"role": "user", "content": user_query}],
        "system_prompt": "Answer questions related to the Maha Kumbh Mela in Prayagraj (Allahabad). Provide accurate and concise responses in 40-60 words.",
        "temperature": 0.5,
        "top_k": 3,
        "top_p": 0.9,
        "max_tokens": 128,
        "web_access": False
    }
    headers = {
        "x-rapidapi-key": "148445fc61msh5cc83372fbe7949p1b2863jsn8772d938a54e",
        "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        output = response.json().get('result')
        tips = "Plan your Kumbh Mela visit early to avoid crowds."
        suggestions = f"Visit the official Kumbh Mela website for more info {verification_links['general_info']}"

        return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

    else:
        output = "Failed to retrieve information related to your query."
        tips = "Try asking related to Maha Kumbh Mela and Prayagraj."
        suggestions = f"Visit the official Kumbh Mela website for more info {verification_links['general_info']}"

        return formatized_response(status="success", output=output, tips=tips, suggestions=suggestions)

#user_query = "Tell me some interesting facts about Kumbh Mela."
#response = get_general_info(user_query)
#print(response)    

def generate_response(user_query_tokens, user_query, intent):
    if intent == "hotel_info":
        return search_hotels(user_query=user_query)
    elif intent == "transportation_info":
        return get_transport_info(tokens=user_query_tokens)
    elif intent == "weather_info":
        return get_city_weather("Allahabad")
    elif intent == "general_info":
        return get_general_info(user_query=user_query)
    elif intent == "emergency_help":
        return get_emergency_help()
    elif intent == "pincodes":
        return get_pincode_details(user_query_tokens=user_query_tokens)
    elif intent == "event_info":
        return extract_location_and_get_events(user_query=user_query)
    else:
        return fallback_response()

queries = [
    "Can you tell me about the hotel options near the river?",
    "What's the weather like today?",
    "I need emergency help. Call the police!",
    "What is the history of the Kumbh Mela?",
    "Tell me something about food."
]

"""for query in queries:
    detected_intent = detect_intent(query)
    response = generate_response(query, detected_intent)
    print(f"\nOriginal query: {query}")
    print(f"Detected intent: {detected_intent}")
    print(f"Response:\n{response}")"""