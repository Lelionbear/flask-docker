from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    global file
    try:
        file = open('count.txt', 'r')
        count = int(file.read())
    except Exception as inst:
        print(inst)
        count = 0
    finally:
        file.close()

    count += 1

    try:
        file = open('count.txt', 'w')
        file.write(str(count))
    except Exception as inst:
        print(inst)
    finally:
        file.close()

    return render_template("index.html", count=count)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
