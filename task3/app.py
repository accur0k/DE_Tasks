from flask import Flask, request, Response
import math

app = Flask(__name__)

def plain(text):
    return text, 200, {'Content-Type': 'text/plain'}

@app.route("/achabarovcuru_gmail_com")
def lcm():
    x = request.args.get('x')
    y = request.args.get('y')
    
    if x is None or y is None:
        return plain("NaN")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return plain("NaN")
    if x < 0 or y < 0:
        return plain("NaN")

    res = str(math.lcm(x,y)) 
    return plain(res)

if __name__ == '__main__':
    app.run()