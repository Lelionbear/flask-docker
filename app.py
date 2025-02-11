from flask import Flask, render_template

app = Flask(__name__)
file_name = 'count.txt'


def get_count():
    global file
    try:
        file = open(file_name, 'r')
        count = int(file.read())
    except Exception as inst:
        print(inst)
        count = 0
    finally:
        file.close()

    return count


def update_count():
    global file
    count = get_count()
    count += 1

    try:
        file = open(file_name, 'w')
        file.write(str(count))
    except Exception as inst:
        print(inst)
    finally:
        file.close()
    return count


@app.route('/')
def index():
    return render_template("index.html", count=update_count())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
