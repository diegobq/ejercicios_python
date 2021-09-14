# Ejercicio 6.1: Propagar por vecinos
# def propagar_al_vecino(l):
#     modif = False
#     n = len(l)
#     for i,e in enumerate(l):
#         if e==1 and i<n-1 and l[i+1]==0:
#             l[i+1] = 1
#             modif = True
#         if e==1 and i>0 and l[i-1]==0:
#             l[i-1] = 1
#             modif = True
#     return modif

# def propagar(l):
#     m = l.copy()
#     veces=0
#     while propagar_al_vecino(l):
#         veces += 1

#     print(f"Repetí {veces} veces la función propagar_al_vecino.")
#     print(f"Con input {m}")    
#     print(f"Y obtuve  {l}")
#     return m

# propagar([0,0,0,0,1])
# propagar([0,0,0,0,0,1])
# propagar([1,0,0,0,0])

# Ejercicio 6.2: Propagar por como el auto fantástico
# def propagar_a_derecha(l):
#     n = len(l)
#     for i,e in enumerate(l):
#         if e==1 and i<n-1:
#             if l[i+1]==0:
#                 l[i+1] = 1
#     return l

# def propagar_a_izquierda(l):
#     return propagar_a_derecha(l[::-1])[::-1]

# def propagar(l):
#     copy = l.copy()
#     ld=propagar_a_derecha(copy)
#     lp=propagar_a_izquierda(ld)
#     return lp

# l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
# # l = [0,0,0,0,0,0,1]
# # l = [1,0,0,0,0,0,0]
# print("Estado original:  ",l)
# print("Propagando...")
# lp=propagar(l)
# print("Estado original:  ",l)
# print("Estado propagado: ",lp)

# Ejercicio 6.3: Propagar con cadenas
def trad2s(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('x')
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps='x'.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)

#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
