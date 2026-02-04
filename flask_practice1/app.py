from flask import Flask, render_template

app = Flask(__name__)

# 사용자 데이터
users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"},
    {"username": "designer", "name": "Jordan"},
    {"username": "musician", "name": "Taylor"},
    {"username": "actor", "name": "Morgan"},

]

# 루트 URL
@app.route('/')
def index():
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
