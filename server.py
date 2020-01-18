from flask import Flask , request, send_file

app = Flask(__name__)

@app.route("/privacy")
def privacy():
    return send_file("build/index.html")

if __name__ == '__main__':
    app.run()
