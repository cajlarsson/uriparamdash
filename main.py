#!/usr/bin/env python


from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True


def sorted_params(dparams):
    return sorted(dparams.items())

@app.route("/")
def hello():
    params = sorted_params(request.args)
    if len(params) == 0:
        return render_template("main.html")
    return render_template("table.html", params=params)


if __name__ == "__main__":
    app.run()
