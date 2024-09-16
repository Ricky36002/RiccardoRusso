from flask import Flask, render_template, request
api = Flask("__name__")
utenti = [['mario', 'pinoilpanino', 'M', '0'], ['giuseppe', 'sigarolargo', 'M', '0'], ['anita', 'paperinoblu', 'F', '0']]

@api.route('/', methods=['GET'])
def es1 ():
    return render_template('es1.html')

@api.route('/regok', methods=['GET'])
def regok ():
    return render_template('reg_ok.html')

@api.route('/regko', methods=['GET'])
def regko ():
    return render_template('reg_ko.html')

@api.route('/registrati', methods=['GET'])
def registrati ():
    email = request.args.get("posta")
    codicefiscale= request.args.get("codfisc")
    password = request.args.get("pass")
    return render_template('reg_ko.html')

api.run(host="0.0.0.0", port=8085)
