import math
import pylab
from matplotlib.widgets import Button, Slider

def addPlot(graph_axes, a, n):
    d = 2 * math.pi / n
    fi = 0
    x_mass = []
    y_mass = []
    x_mass.append(0)
    y_mass.append(0)
    while fi < 2 * math.pi:
        fi = fi + d
        r = a * math.sin(2 * fi)
        x = r * math.cos(fi)
        y = r * math.sin(fi)
        x_mass.append(x)
        y_mass.append(y)
    x_mass.append(0)
    y_mass.append(0)
    graph_axes.plot(x_mass, y_mass)
    pylab.show()

def coord_sys():
    graph_axes.set_xlabel(' Ось X    ', fontsize=15, color='green')
    graph_axes.set_ylabel(' Ось Y    ', fontsize=15, color='green')
    graph_axes.set_title('r = a * sin(2 * fi)')
    graph_axes.axhline(0, color='green')
    graph_axes.axvline(0, color='green')

def onButtonAddClicked(event):
    global slider_phi
    global graph_axes
    graph_axes.clear()
    coord_sys()
    graph_axes.grid()
    pylab.draw()
    addPlot(graph_axes, slider_phi.val, slider_n.val)

if __name__ == '__main__':
    fig, graph_axes = pylab.subplots()
    graph_axes.grid()
    coord_sys()
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

    axes_button_add = pylab.axes([0.7, 0.01, 0.25, 0.075])
    button_add = Button(axes_button_add, 'Построить')
    button_add.on_clicked(onButtonAddClicked)

    axes_slider_phi = pylab.axes([0.05, 0.25, 0.85, 0.04])
    slider_phi = Slider(axes_slider_phi,
                          label='a',
                          valmin=1,
                          valmax=10,
                          valinit=2,
                          valfmt='%1.2f')

    axes_slider_n = pylab.axes([0.05, 0.17, 0.85, 0.04])
    slider_n = Slider(axes_slider_n,
                      label='n',
                      valmin=10,
                      valmax=100,
                      valinit=50,
                      valfmt='%1.2f')

    pylab.show()