import optparse

from flask import Flask, jsonify, request
from stok import stok
from reception import reception
def flaskrun(app, default_host="127.0.0.1",
                  default_port="5000"):
    """
    Takes a flask.Flask instance and runs it. Parses
    command-line flags to configure the app.
    """

    # Set up the command-line options
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host",
                      help="Hostname of the Flask app " + \
                           "[default %s]" % default_host,
                      default=default_host)
    parser.add_option("-P", "--port",
                      help="Port for the Flask app " + \
                           "[default %s]" % default_port,
                      default=default_port)
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug",
                      help=optparse.SUPPRESS_HELP)
    options, _ = parser.parse_args()
    app.run(
        debug=options.debug,
        host=options.host,
        port=int(options.port)
    )


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
    flaskrun(app)

