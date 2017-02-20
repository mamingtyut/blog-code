# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "hi"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)
