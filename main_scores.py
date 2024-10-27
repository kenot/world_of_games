from flask import Flask
import os

app = Flask(__name__)

from utils import SCORES_FILE_NAME, BAD_RETURN_CODE


@app.route('/')
def score_server():
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                score = file.read().strip()
        else:
            score = '0'
        html_content = f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is <div id="score">{score}</div></h1>
            </body>
        </html>
        """
        return html_content
    except Exception as e:
        error_content = f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">Error: {str(e)}</div></h1>
            </body>
        </html>
        """
        return error_content, BAD_RETURN_CODE


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
