from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info', methods=["GET", "POST"])
def ip_info():
    return render_template('result_test.html')

@app.route('/aboutus', methods=["GET", "POST"])
def get_about_us():
    return render_template('about_us.html')




if __name__ == '__main__':
    app.run(debug=True)
