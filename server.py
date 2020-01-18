from flask import Flask , request, send_file

app = Flask(__name__)

@app.route("/privacy")
def privacy():
    return send_file("build/index.html")

@app.route("/privacy_static/<path:filename>")
def privacy_static(filename):
    if filename.startswith("/"):
        return send_file("privacy_static" + filename)
    else:
        return send_file("privacy_static/" + filename)

if __name__ == '__main__':
    app.run()
