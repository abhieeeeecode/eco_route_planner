from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/route", methods=["POST"])
def get_route():
    data = request.json
    start = data["start"]
    end = data["end"]

    # OSRM with ALTERNATIVES ENABLED
    url = (
        f"https://router.project-osrm.org/route/v1/driving/"
        f"{start['lng']},{start['lat']};{end['lng']},{end['lat']}"
        f"?overview=full&geometries=geojson&alternatives=true"
    )

    try:
        r = requests.get(url)
        r.raise_for_status()
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
