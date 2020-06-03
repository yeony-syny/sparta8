from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET'])
def bom():
   title_receive = request.args.get('title_receive')
   print (title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})



@app.route('/test', methods=['post'])
def bom2():
   title_receive = request.form['title_receive']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 post!'})



if __name__ == '__main__':  
   app.run('127.0.0.1',port=5000,debug=True)