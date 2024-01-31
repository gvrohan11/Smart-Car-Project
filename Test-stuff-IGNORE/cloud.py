from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/process_request')
def process_request():
    # Simulate processing the request
    success = True  # Set this based on your actual processing logic

    if success:
        result = "success"
    else:
        result = "failure"

    response_data = {'result': result}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)