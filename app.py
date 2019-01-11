from flask import Flask, jsonify, request
from stok import stok
from reception import reception

app = Flask(__name__)

@app.route('/',methods=['Post'])
def database():
    non = request.json['non']
    kant = request.json['kant']
    typ = request.json['tip']
    reket = reception(kant,non,typ)
    lisP =[]
    for i in range(reket.kantitepwodwi):
        newst = stok(nonpwodwi = reket.nonpwodwi, typpwodwi = reket.typpwodwi)
        lisP.append(newst.__dict__)
    return jsonify(lisP)

#@app.route('/')
#def recep():
 #   res= reception(5,"diri","alimentaire")
  #  return jsonify({"kant": res.kantitepwodwi, "non": res.nonpwodwi, "typ": res.typwodwi})
if __name__ == '__main__':
    app.run(debug=True)

