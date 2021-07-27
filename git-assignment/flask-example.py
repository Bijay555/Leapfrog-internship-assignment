from flask import Flask , request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
	return "Hello, How are you doing?"

@app.route("/data", methods=['POST'])
def data_forms():
	person_name = request.form.get('person_name')
	return "His name is {}".format(person_name)


if __name__ == '__main__':
	app.run(debug=True)
