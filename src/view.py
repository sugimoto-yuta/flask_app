# coding: utf-8

from flask import Flask, render_template

# Flaskをインスタンス化
app = Flask(__name__)

# -----View側の設定------
# ルートディレクトリにアクセスがあったときの挙動
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


