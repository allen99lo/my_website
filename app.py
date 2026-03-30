from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>我的第一個 Python 網頁在網路上跑起來了！</h1>"

if __name__ == '__main__':
    app.run()