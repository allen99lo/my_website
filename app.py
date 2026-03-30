from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head><title>我的班表網頁</title></head>
        <body>
            <h1>我的個人網站</h1>
            <p>歡迎查看我的班表：</p>
            
            <a href="/static/schedule.xlsx" download>
                <button style="padding: 10px; cursor: pointer;">下載最新班表 (Excel)</button>
            </a>
            
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)