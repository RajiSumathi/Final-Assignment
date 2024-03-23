import pandas as pd
from urllib.parse import unquote, urlparse
from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)

LOG_FILE_PATH = "hn_logs.tsv"
DATE_FORMATS = [
    "%Y",
    "%Y-%m",
    "%Y-%m-%d",
    "%Y-%m-%d %H",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d %H:%M:%S"
]


def preprocess_logs(LOG_FILE_PATH):
    df = pd.read_csv(LOG_FILE_PATH, sep='\t', header=None)
    df[0] = pd.to_datetime(df[0])
    return df


def decode_url(url):
    url = url.strip('%22')
    decoded_url = urlparse(unquote(url)).netloc
    return decoded_url


def get_count(df, date_prefix, date_formats):
    for fmt in date_formats:
        try:
            parsed_datetime = datetime.strptime(date_prefix, fmt)
            return len(df[df[0].dt.strftime(fmt) == parsed_datetime.strftime(fmt)][1].unique())
        except ValueError:
            pass
    return 0


@app.route('/1/queries/count/<date_prefix>')
def get_logs_count(date_prefix):
    global LOG_FILE_PATH, DATE_FORMATS
    try:
        df = preprocess_logs(LOG_FILE_PATH)
        count = get_count(df, date_prefix, DATE_FORMATS)
        return jsonify({"count": count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)