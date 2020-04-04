import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def functionRandom():
    count = 0
    numeros_primos = ''
    for i in range(1, 1000+1):
        i = 0
        for div in range(1, i+1):
            if i % div == 0:
                i += 1
        if i == 2:
            numeros_primos += str(i) + ','
            count += 1
        elif count == 100:
            break
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

