from flask import Flask, jsonify, request
import stok
import reception

app = Flask(__name__)

@app.route('/',methods=['Post'])
def database():
    non = request.json['non']
    kant = request.json['kant']
    typ = request.json['tip']
    sent = stok(kant,non,typ)
    lisP =[]
    for i in range(kant):
        newst = stok(nonpwodwi = non, typpwodwi = typ)
        lisP.append(newst)
    return jsonify(lisP)







#@app.route('/')
#def recep():
 #   res= reception(5,"diri","alimentaire")
  #  return jsonify({"kant": res.kantitepwodwi, "non": res.nonpwodwi, "typ": res.typwodwi})
if __name__ == '__main__':
    app.run(debug=True)

