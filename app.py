from flask import Flask, make_response

from scrapfile import scrape_site
from config import URL

app = Flask(__name__)

@app.route('/')
def home():
    result = scrape_site(URL)
    resp = make_response(result)
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp
    
if __name__ == '__main__':
    app.run(debug=False)