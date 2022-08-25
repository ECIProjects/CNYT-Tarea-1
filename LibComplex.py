import math
def suma(a,b):
    """retorna la suma entre dos numeros complejos"""
    return (a[0]+b[0]),(a[1]+b[1])
def producto(a,b):
    """retorna el producto entre dos numeros complejos"""
    if a[0]==b[0] and a[1]==(b[1]*-1):
        return (a[0]**2)+(a[1]**2)
    return ((a[0]*b[0])-(a[1]*b[1])),((a[0]*b[1])+(a[1]*b[0]))
def resta(a,b):
    """retorna la resta entre dos numeros complejos"""
    return (a[0]-b[0]),(a[1]-b[1])
def conjug(a):
    """retorna el conjugado de un numero complejo"""
    return a[0],(a[1]*(-1))
def division(a,b):
    """retorna la division de dos numero complejo"""
    x=producto(a,conjug(b))
    return ((x[0])/producto(b,conjug(b))),((x[1])/producto(b,conjug(b)))
def modulo(a):
    """retorna el modulo de un numero complejo"""
    return math.hypot(a[0],a[1])
def fase(a):
    """retorna la fase de un numero complejo en radianes"""
    return math.atan(a[1]/a[0])
def carpol(a):
    """convierte un numero complejo desde su representación cartesiana a la polar"""
    return modulo(a),fase(a)
def polcar(a):
    """convierte un numero complejo desde la representación polar a la cartesiana"""
    return a[0]*math.cos(a[1]),a[0]*math.sin(a[1])
