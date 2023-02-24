import numpy as np
import matplotlib.pyplot as plt

from scipy import signal
A = np.array([[=1, 0, 0.1] ,
[0, =1 , 0] ,
[0, 0, =1]])
B = np.array([[1], [1] , [1] ])
C = np.array([[1, 0, 0] ])
D = np.array([[0]])

sistema = signal.StateSpace(A, B, C, D)

t, h = signal.impulse(sistema) # Construir h(t)
# Gr ́afica de h(t)
plt . plot(t, h)
plt . xlabel(r ’$t$’, fontsize =14)
plt . ylabel(r ’$h(t)$’, fontsize =14)
plt . grid()
plt .show()

t, s = signal.step(sistema) # Construye s(t)
# Gr ́afica de s(t)
plt . plot(t, s)
plt . xlabel(r ’$t$’, fontsize =14)
plt . ylabel(r ’$s(t)$’, fontsize =14)
plt . grid()
plt .show()

w, mag, phase = sistema.bode() # Construye los diagramas de Bode
# Gr ́aficas de los diagramas de Bode
# Bode de Magnitud
plt . figure ( figsize =(16, 4))
plt .subplot(1,2,1)
plt .semilogx(w, mag) # Diagrama de Bode de magnitud
plt . xlabel(r ’$\omega$’,fontsize=16)
plt . ylabel(r ’$20\log|H(\omega)|$’,fontsize=16)
plt . grid(True, which=”both”)
# Bode de Fase
plt .subplot(1,2,2)
plt .semilogx(w, phase) # Diagrama de Bode de fase
plt . xlabel(r ’$\omega$’,fontsize=16)
plt . ylabel(r ’$\angle H(\omega)$’,fontsize=16)
plt . grid(True, which=”both”)
plt .show()
