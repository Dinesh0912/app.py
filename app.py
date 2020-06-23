from flask import Flask,request,render_template
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("calc.html")
    if request.method == 'POST':
        a = request.form.get("num1")
        b = request.form.get("num2")
        o = request.form.get("op")
        if o == "add":
            c = int(a)+int(b)
        elif o == "sub":
            c = int(a)-int(b)
        elif o == "mul":
            c = int(a)*int(b)
        elif o == "div":
            c = int(a)/int(b)
        return render_template("calc.html",output=str(c))


if __name__ == '__main__':
    app.run()
