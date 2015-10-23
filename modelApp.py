from flask import Flask, render_template, make_response
from randomModel import drawPic
import StringIO

app = Flask(__name__)


@app.route('/')
def homepage():
    title = "Model App"
    paragraph = ["This is a full functional application, seriously.", "Are you serious?"]
    return render_template("index.html", title=title, paragraph=paragraph)


@app.route('/about')
def aboutpage():

    title = "About this page"

    paragraph = ["Right", "Copy Left"]

    pageType = 'about'

    return render_template("index.html")#, title=title, paragraph=paragraph, pageType=pageType)


@app.route('/images')
def plot():
    return render_template("images.html", title="abc")


@app.route('/pic')
def pic():

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    fig = drawPic()
    canvas = FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    return response


if __name__ == '__main__':
    app.run()
