from Pencil import Pencil
import matplotlib.pyplot as plt


def main():
    Pencil.stroke_line(plt, [0, 0], [10, 10], line_style='--', color='r', alpha=0.5)
    Pencil.fill_rect(plt, [1, 1], 1, 1)
    plt.show()


if __name__ == '__main__':
    main()
