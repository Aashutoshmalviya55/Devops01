from flask import Flask
a=Flask(__name__)
@a.route('/sms1')
def lw():
    return "Hellow , this is first project of my Devoops jouney using git,github,jenkins,docker,python fully automated."
a.run(host="0.0.0.0")
