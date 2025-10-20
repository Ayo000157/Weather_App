from flask import Flask,  render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form['city']
        api_key ="477b7d4e328287f9d2721ec6232ca4bd"  #  OpenWeather key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data["cod"] == "404":
            error = "City not found, try again later"
        else:
            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
                     }

    return render_template('index.html', weather_data=weather_data , error=error)
if __name__ == '__main__':
    app.run(debug=True)