from flask import Flask, jsonify, request
import pandas as pd

# Create the Flask app
app = Flask(__name__)

# Load the dataframe with the translation pairs
df = pd.read_csv("dataset/cleaned_dataset.csv")

@app.route("/api/v1/status", methods=['GET'])
def status():
    # Return appropriate status code
    return jsonify({'status': 'OK'}), 200

@app.route('/api/v1/sentences', methods=['GET'])
def get_translations():
    # Get the first 10 rows from the dataframe
    translations = df.head(10)

    # Convert the dataframe to a list of pairs
    translations_list = list(zip(df.English,df.German))

    # Take 10 sentences counting from the given index, if no i ndex specified, return the first 10 sentences
    index = request.args.get('index', default=0, type=int)

    # Return the dictionary as a JSON response
    return jsonify(translations_list[index:index+10]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
