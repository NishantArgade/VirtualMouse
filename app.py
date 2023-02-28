from flask import Flask, render_template
import Virtual_Mouse


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/start/')
def my_link():
    print('I got clicked!')
    Virtual_Mouse.vm_mouse(0)
    return 'Click.'


@app.route('/stop/')
def stop():
    print('I got clicked!')
    Virtual_Mouse.vm_mouse(1)
    return 'Click.'


if __name__ == "__main__":
    app.run(debug=True)
