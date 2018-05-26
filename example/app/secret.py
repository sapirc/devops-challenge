from flask import Flask
import sys, os

import subprocess

app = Flask(__name__)

@app.route("/secret")
def secret():
    x = os.popen("/root/.local/bin/aws dynamodb get-item --table-name devops-challenge --key \"code_name\"={\"S\"=\"thedoctor\"} | jq '.Item.secret_code.S'").read()
#    x = os.popen(["aws dynamodb get-item --table-name devops-challenge --key \"code_name\"={\"S\"=\"thedoctor\"} | jq '.Item.secret_code.S'"]).read()

    return x

if __name__ == '__main__':
    app.run(debug=True)

