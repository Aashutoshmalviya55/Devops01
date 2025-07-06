from flask import Flask
a=Flask(__name__)
def lw():
    return "hwllo "
a.run(host="0.0.0.0")