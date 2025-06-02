import gradio as gr
import requests

API_KEY = "ΒΑΛΕ_ΕΔΩ_ΤΟ_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not city:
        return "⚠️ Πληκτρολόγησε όνομα πόλης!"
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "el"
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        
        emoji = "☀️" if "clear" in desc else "🌧️" if "rain" in desc else "⛅"
        
        result = f"""
🔍 Καιρός για: **{city.title()}**

{emoji} **{desc.title()}**
🌡️ Θερμοκρασία: {temp}°C  
💧 Υγρασία: {humidity}%  
🌬️ Άνεμος: {wind} m/s
"""
        return result
    else:
        return "❌ Η πόλη δεν βρέθηκε!"

# Gradio Interface
interface = gr.Interface(
    fn=get_weather,
    inputs=gr.Textbox(placeholder="Π.χ. Αθήνα", label="Πόλη"),
    outputs=gr.Markdown(),
    title="🌤️ Weather App",
    description="Μπες σε ατμόσφαιρα καιρού με Gradio & OpenWeatherMap API!",
    theme="soft"
)

if __name__ == "__main__":
    interface.launch()
