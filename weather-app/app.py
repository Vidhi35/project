from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "5651a7b36ceef53d13b920f19ea3dcde"  # Replace with your OpenWeatherMap API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'].capitalize()
        }
        return render_template('result.html', weather=weather_data)
    else:
        error = data.get("message", "Something went wrong.")
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
