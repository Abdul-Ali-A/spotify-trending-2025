# app.py
from flask import Flask, render_template, request, jsonify
from spotify_api import get_popular_tracks

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    tracks = []
    genre = ""

    if request.method == 'POST':
        genre = request.form['genre'].strip().lower()
        tracks = get_popular_tracks(genre, limit=5)

    return render_template('index.html', tracks=tracks, genre=genre)

# API Endpoint
@app.route('/api/<genre>')
def api_tracks(genre):
    try:
        tracks = get_popular_tracks(genre.lower(), limit=5)
        return jsonify({
            "genre": genre.lower(),
            "count": len(tracks),
            "tracks": tracks
        })
    except Exception as e:
        return jsonify({"error": "Invalid genre or API error", "details": str(e)}), 400

if __name__ == '__main__':
    import os
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
