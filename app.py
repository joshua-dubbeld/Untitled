from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}.".format(name)


@app.route('/f')
@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius=""):
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * 9 / 5) + 32
    except ValueError:
        return "Invalid temperature"
    return "{} celsius is equal to {} fahrenheit.".format(str(celsius), str(fahrenheit))


if __name__ == '__main__':
    app.run()
