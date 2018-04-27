from flask import Flask, render_template, request
import rf_send

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("lighton"):
            rf_send.control_light("on")
        elif request.form.get("lightoff"):
            rf_send.control_light("off")

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
