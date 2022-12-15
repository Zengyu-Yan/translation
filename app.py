from flask import Flask, jsonify
#import pandas as pd

# Create the Flask app
app = Flask(__name__)

# Load the dataframe with the translation pairs
df = pd.read_csv("cleaned_dataset.csv")

@app.route('/translations')
def get_translations():
    # Get the first 10 rows from the dataframe
    translations = df.head(10)

    # Convert the dataframe to a dictionary
    translations_dict = translations.to_dict()

    # Return the dictionary as a JSON response
    return jsonify(translations_dict)

if __name__ == '__main__':
    app.run()
