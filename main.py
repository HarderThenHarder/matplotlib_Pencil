from Pencil import Pencil
import matplotlib.pyplot as plt


def main():
    Pencil.set_width_height(plt, 1, 1)
    # Pencil.stroke_line(plt, [0, 0], [10, 10], line_style='--', color='r', alpha=0.5)
    Pencil.fill_circle(plt, [0, 0], 1)
    Pencil.fill_rect(plt, [10, 10], 10, 10)
    plt.show()


if __name__ == '__main__':
    main()
