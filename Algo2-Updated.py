import matplotlib.pyplot as plt
from fractions import Fraction
Tn = []
numberElement = 5000


def plot_graph(label, func, n_ranges, bound, is_bounds):
    print('\nValues of y axis\n', Tn)
    plt.plot(n_ranges, func, label="function")
    if is_bounds:
        plt.plot(n_ranges, bound, label=label)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Plot for Time Complexity')
    plt.grid(True)
    plt.legend()
    plt.show()


def gn(i1, coefficient, power):
    return coefficient * i1 ** power


def function(n1, t1i):
    t1i = t1i * ((n1 + 3) / n1) ** n1 * ((n1 - 1) / (n1 + 2)) ** (n1 - 1)
    Tn.append(t1i)
    return t1i


n_range = range(2, numberElement)
ti = 4
Tn.append(ti)
for n in n_range:
    ti = function(n, ti)
n_range = range(1, numberElement)
plot_graph("", Tn, n_range, "", False)


# upper_bound graphs
c2_values = [1, 10, 15, 21]
c2_powers = [1, 1 / 8, 1 / 16, 1 / float('inf')]
for i in range(len(c2_values)):
    c2g = [gn(n, c2_values[i], c2_powers[i]) for n in n_range]
    string = 'Upper Bound::g(n)=' + str(c2_values[i]) + '*(n^' + str(Fraction(c2_powers[i])) + ')'
    plot_graph(string, Tn, n_range, c2g, True)


# lower_bound graphs
c1_values = [1, 8, 12, 1]
c1_powers = [1 / 8, 1 / 8, 1 / 16, 1 / float('inf')]
for i in range(len(c1_values)):
    c1g = [gn(n, c1_values[i], c1_powers[i]) for n in n_range]
    string = 'Lower Bound::g(n)=' + str(c1_values[i]) + '*(n^' + str(Fraction(c1_powers[i])) + ')'
    plot_graph(string, Tn, n_range, c1g, True)


# Calculation of slope of Tn
slope = []
for n in range(2, len(Tn)):
    slope.append(Tn[n] - Tn[n - 1])
print('Slope of this graph is\n', slope)
