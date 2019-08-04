from flask import Flask, render_template

from api import api_bp

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.register_blueprint(api_bp)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
