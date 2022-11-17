from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.hrta48t.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/first_mini", methods=["POST"])
def first_mini_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.first_mini.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini", methods=["GET"])
def first_mini_get():
    homework_list = list(db.first_mini.find({}, {'_id': False}))
    return jsonify({'first_mini':homework_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)