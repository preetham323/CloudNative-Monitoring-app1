import psutil
from flask import Flask, render_template

app = flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent
    mem_metic = psutil.virtual_memory().percent
    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory detected, please saclue up"

    return render_template("index.html", cpu_metric=cpu_metric, mem_metic=mem_metic, Message=Message)

if __name__ == '__main__':
    app.run(debug=True, host=0.0.0.0)    