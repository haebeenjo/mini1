from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://sayapinn:$100doller@cluster0.qv0cojm.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/teamintro", methods=["POST"])
def teamintro_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.intro.insert_one(doc)

    return jsonify({'msg':'방명록을 남겼습니다.'})

@app.route("/teamintro", methods=["GET"])
def teamintro_get():
    comment_list = list(db.intro.find({}, {'_id': False}))
    return jsonify({'comments':comment_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)