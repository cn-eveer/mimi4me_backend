from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    # index.htmlはtemplatesディレクトリに置く
    return "HELLO FLASK"

if __name__ == '__main__':
    # Flaskはポート番号5000で起動
    app.run(port=5000, debug=True)