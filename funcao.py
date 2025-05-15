
f1 = lambda x: x**2
mensagem = "Limite inferior tem que ser menor que o limite superior!"
def modulo(x):
    if x>=0:
        return x
    else:
        return -x

def trapezio_simples(f,c,d):

    if c>d:
        print(mensagem)
        return None
    else:
        return (d-c)*(f(c) + f(d))/2

def trapezio_recursivos(f,c,d,n):
    if c>d:
        print(mensagem)
        return None

    if n==0: #Caso base
        return trapezio_simples(f,c,d)

    else: # Dividir a metade
        metade = (c+d)/2
        return trapezio_recursivos(f,c,metade,n-1) + trapezio_recursivos(f,metade,d,n-1)


def trapezio_iterativos(f,c,d,n):
    if c > d:
        print(mensagem)
        return None

    h = (d+c)/n # Tamanho de todas as divisoes
    area_total = 0
    for i in range(n):
        lim_i = c+(h*i)
        lim_s = lim_i + h
        area_total += trapezio_simples(f,lim_i,lim_s)
    return area_total

def forca_bruta(f, c, d, max_iter=100000):
    counter = 2
    while counter < max_iter:
        t = trapezio_iterativos(f, c, d,counter)
        t_anterior = trapezio_iterativos(f, c, d,counter - 1)
        if t == t_anterior:
            return f"{trapezio_iterativos(f,c,d,counter)} quando n={counter}"  # Encontrou o valor onde Tn == Tn-1
        counter += 1
    return None # Não encontrou nada

def simpson_simples(f,c,d):
    if c>d:
        print(mensagem)
        return None
    metade =(c+d)/2
    return ((d-c)/2)*(f(c)+4*f(metade)+f(d))/3

def simpson_recursivos(f,c,d,n):
    if c>d:
        print(mensagem)
        return None
    if n==0: return simpson_simples(f,c,d) #Caso base
    else:
        metade = (c+d)/2
        return simpson_recursivos(f,c,metade,n-1) + simpson_recursivos(f,metade,d,n-1)

def greedy(f,c,d,epsilon):
    for n in range(2,30):
        t_1 = trapezio_iterativos(f,c,d,n)
        t_2 = trapezio_iterativos(f,c,d,n-1)
        s_1 = simpson_recursivos(f,c,d,n)
        if modulo(t_1-t_2)<epsilon and modulo(t_1-s_1)<epsilon:
            return t_1
    return None

greedy(f1,0,2,0.000001)


