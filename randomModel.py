import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft2, ifft2
from autocorrelation import autocorrelation_func


def drawPic():
    m = 200
    n = 200
    a = 20
    b = 20
    r = 1
    vp0 = 1500
    variance = 0.08
    dx = 3
    C = np.zeros((m, n))

    au = autocorrelation_func(a, b)

    for i in xrange(m):
        for j in xrange(n):
            C[i, j] = au.gaussian((i-(m-1)/2.)*dx, (j-(n-1)/2.)*dx)
    S = fft2(C)  # power spectral density
    z = np.random.randn(m, n)
    Z = fft2(z)

    G = np.sqrt(dx * S)

    GZ = G * Z
    gz = ifft2(GZ)

    A = np.real(gz)

    K = np.real(A)
    f = plt.figure()
    plt.imshow(K)
    return f
