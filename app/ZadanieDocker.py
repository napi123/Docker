from flask import Flask, render_template
from flask import Flask, request, escape, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import urllib

app = Flask(__name__)

@app.route('/Test')
def show_test():
    return "Test"

@app.route('/')
def graph():
    a = request.args.get('a', 12, type=int)
    b = request.args.get('b', 5, type=int)
    c = request.args.get('c', 0, type=int)
    xmin = request.args.get('xmin', -50, type=int)
    xmax = request.args.get('xmax', 50, type=int)
    ymin = request.args.get('ymin', -50, type=int)
    ymax = request.args.get('ymax', 50, type=int)
    
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    x = range(int(xmin), int(xmax))
    y = [a*i*i + b*i + c for i in x]

    axis.plot(x, y)
    axis.set_xlim(xmin, xmax)
    axis.set_ylim(ymin, ymax)

    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

#if __name__ == '__main__':
#    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5000)