import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import Button

fig = plt.figure()
fig.subplots_adjust(bottom=0.3)
ax = fig.add_subplot(111, projection='3d')

v = [[0, 0, 1]]
for i in range(6):
    fi = 2 * np.pi * i / 6
    x = np.cos(fi)
    y = np.sin(fi)
    v.append([x, y, 0])

v = np.array(v)
ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

sides = [[v[0], v[1], v[6]], [v[0], v[1], v[2]], [v[0], v[2], v[3]], [v[0], v[3], v[4]], [v[0], v[4], v[5]],
         [v[0], v[5], v[6]], [v[1], v[2], v[3], v[4], v[5], v[6]]]

ax.add_collection3d(Poly3DCollection(sides, alpha=0.5, edgecolors='black'))


def button_callback_remove(event):
    ax.add_collection3d(Poly3DCollection(sides, alpha=1, edgecolors='black'))
    plt.draw()


button_ax_remove = fig.add_axes([0.5, 0.15, 0.31, 0.06])
button_remove = Button(button_ax_remove, "Убрать невидимые линии")
button_remove.on_clicked(button_callback_remove)


def button_callback_show(event):
    ax.add_collection3d(Poly3DCollection(sides, alpha=0.5, edgecolors='black'))
    plt.draw()


button_ax_show = fig.add_axes([0.5, 0.05, 0.31, 0.06])
button_show = Button(button_ax_show, "Каркасная отрисовка")
button_show.on_clicked(button_callback_show)


def button_callback_isometric(event):
    ax.view_init(35, 45)
    plt.draw()


button_ax_isometric = fig.add_axes([0.1, 0.05, 0.31, 0.06])
button_isometric = Button(button_ax_isometric, "Изометрическая")
button_isometric.on_clicked(button_callback_isometric)


def button_callback_ortographic_top(event):
    ax.view_init(90)
    plt.draw()


button_ax_ortographic_top = fig.add_axes([0.1, 0.15, 0.31, 0.06])
button_ortographic_top = Button(button_ax_ortographic_top, "Ортографическая верх")
button_ortographic_top.on_clicked(button_callback_ortographic_top)


def button_callback_ortographic_front(event):
    ax.view_init(0)
    plt.draw()


button_ax_ortographic_front = fig.add_axes([0.1, 0.25, 0.31, 0.06])
button_ortographic_front = Button(button_ax_ortographic_front, "Ортографическая перед")
button_ortographic_front.on_clicked(button_callback_ortographic_front)

plt.show()
