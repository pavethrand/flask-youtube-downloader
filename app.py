from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask(__name__)

@app.route('/download', methods=["GET","POST"])
def result():
        #try:
            youtube_url = request.form["u-text"]
            download_path = YouTube(youtube_url).streams[0].download()
            fname = download_path.split("//")[-1]
            return send_file(fname, as_attachment=True)
        #except:
            #return "Video download failed!"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
