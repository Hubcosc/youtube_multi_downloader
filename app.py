from flask import Flask, request, jsonify, send_from_directory
import os
import threading
from pytube import YouTube # Add this line to import the YouTube class

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'message': 'No URL provided'}), 400

    def download():
        try:
            youtube = YouTube(url)
            video = youtube.streams.get_highest_resolution()
            video.download()
            print(f"Downloaded video: {url}")
        except Exception as e:
            print(f"Failed to download video: {url}\nError: {e}")

    # Start the download in a new thread to avoid blocking the server
    thread = threading.Thread(target=download)
    thread.start()

    return jsonify({'message': 'Download started'}), 200

if __name__ == '__main__':
    app.run(debug=True)