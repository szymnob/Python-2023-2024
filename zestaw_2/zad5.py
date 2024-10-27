import numpy as np
import matplotlib as plt

def draw(x1, x2, polynomial):
    x_val = np.linspace(x1, x2, 100)
    y_val = [eval(polynomial) for x in x_val]

    plt.plot(x_val, y_val)
    plt.title("Wykres wielomianu")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    wielomian = input("Podaj wielomian: ")
    x1 = input("Podaj poczatek przedzialu: ")
    x2 = input("Podaj koniec przedzialu: ")