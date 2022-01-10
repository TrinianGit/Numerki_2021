import numpy as np
import matplotlib.pyplot as plt

def solve(A_, B_, C_, y):

    A = np.array(A_)
    B = np.array(B_)
    C = np.array(C_)
    D = np.array(y)

    for i in range(D.size - 1):
        w = A[i] / B[i]
        B[i+1] = B[i+1] - w*C[i]
        D[i+1] = D[i+1] - w*D[i]

    u = np.zeros(D.size)

    for i in range((u.size - 1), -1, -1):
        if i == (u.size - 1):
            u[i] = D[i] / B[i]
        else:
            u[i] = (D[i] - C[i] * u[i+1]) / B[i]

    return u

def SplajnKubiczny(x_x):
    print (x_x)
    fx = np.zeros_like(x_x)
    for j in range(0, x_x.size - 1):
        i = (x_x[j] - x[0])/(x[1]-x[0])
        i = int(i)
        
        Ax = (x[i+1] - x_x[j])/(x[i+1] - x[i])
        Bx = (x_x[j] - x[i])/(x[i+1] - x[i])
        Cx = (1/6)*(Ax**3-Ax)*(x[i+1] - x[i])**2
        Dx = (1/6)*(Bx**3-Bx)*(x[i+1] - x[i])**2
        fx[j] = Ax*y[i] + Bx*y[i+1] + Cx*eps[i] + Dx*eps[i+1]

    j = x_x.size-1
    i = (x_x[j] - x[0])/(x[1]-x[0])
    i = int(i) - 1
        
    Ax = (x[i+1] - x_x[j])/(x[i+1] - x[i])
    Bx = (x_x[j] - x[i])/(x[i+1] - x[i])
    Cx = (1/6)*(Ax**3-Ax)*(x[i+1] - x[i])**2
    Dx = (1/6)*(Bx**3-Bx)*(x[i+1] - x[i])**2

    fx[j] = Ax*y[i] + Bx*y[i+1] + Cx*eps[i] + Dx*eps[i+1]

    return fx


if (__name__ == "__main__"):
    x = np.array([i/8 for i in range(-7, 9, 2)])
    y = np.array([1/(1+5*x[i]**2) for i in range(8)])

    A = np.array([1. for i in range(5)])
    B = np.array([4. for i in range(6)])
    C = np.array([1. for i in range(5)])

    D = np.array([y[i] - 2*y[i+1] + y[i+2] for i in range(0, 6)])

    eps = solve( A, B, C, (6/(x[1]-x[0])**2)*D)
    eps = np.insert(eps, (0, 6), 0.)

    plot_x = np.linspace(x[0],x[7])
    plot_fx = SplajnKubiczny(plot_x)

    plt.plot(plot_x, plot_fx)
    print (plot_fx)
    for i in range (8):
        plt.plot(x[i], y[i],'o')
        
    plt.show()