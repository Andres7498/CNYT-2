 import math

def sumacom(x,y):
    q=float(x[0])+float(y[0])
    e=float(x[1])+float(y[1])
    return(q,e)
def rescom(x,y):
    q=float(x[0])-float(y[0])
    e=float(x[1])-float(y[1])
    return(q,e)
def multicom(x,y):
    q=(float(x[0])*float(y[0])+(float(x[1])*float(y[1])*-1))
    e=(float(x[0])*float(y[1]))+((float(x[1])*float(y[0])))
    return(q,e)
def modcom(x):
    q=((float(x[0])**2)+(float(x[1])**2))**0.5
    return(q)
def divcom(x,y):
    a1=float(x[0])
    a2=float(x[1])
    b1=float(y[0])
    b2=float(x[0])
    q=(((a1*a2)+(b1*b2))/(a2**2)+(b2**2))
    e=(((a2*b1)-(a1*b2))/(a2**2)+(b2**2))
    return(q,e)
def concom(x):
    q=float(x[0]),(float(x[1])*-1)
    return(q)
def cartcom(x):
    q=((float(x[0])**2)+(float(x[1])**2))**0.5
    ang1=math.atan(float(x[1])/float(x[0]))
    x=q*math.cos(ang1)
    y=q*math.sin(ang1)
    return(x,y)
def polarcart(x):
    a=round(x[0]*math.cos(x[1]),5)
    b=round(x[0]*math.sin(x[1]),5)
    return(a,b)
def fasecom(x):
    arri=x[1]
    abaj=x[0]
    d=(math.atan2(arri,abaj))
    return round(d,2)
def adicivectocom(x,y):
    lista=[]
    if len(x)== len(y):
        for i in range(len(x)):
            tup=x[i]
            tup2=y[i]
            z=sumacom(tup,tup2)
            lista.append(z)
        return lista
    else:
        return "No son de la misma dimension"
def invervectocom(x):
    lista=[]
    for i in range(len(x)):
        a=x[i]
        d=float(a[0])*-1
        f=float(a[1])*-1
        z=(d,f)
        lista.append(z)
    return lista
def multivectocom(x,a):
    lista=[]
    for i in range(len(x)):
        tup=x[i]
        z=multicom(tup,a)
        lista.append(z)
    return lista
def adicimatcom(x,y):
    
    final2=[]
    for i in range(len(x)):
        final=[]
        for j in range(len(x[0])):
            final.append(sumacom(x[i][j],y[i][j]))
        final2.append(final)
    return final2
def invermatcom(x):
    final=[]
    for i in range(len(x)):
        fila=[]
        for j in range(len(x[0])):
            a=((((x[i][j])[0])*-1))
            b=((((x[i][j])[1])*-1))
            c=(a,b)
            fila.append(c)
        final.append(fila)
    return(final)
def escamatcom(x,y):
    final=[]
    for i in range(len(x)):
        fila=[]
        for j in range(len(x[0])):
            a=((((x[i][j])[0])*y))
            b=((((x[i][j])[1])*y))
            c=(a,b)
            fila.append(c)
        final.append(fila)
    return(final)
def transmatvec(x):
    final=[]
    for i in range(len(x[0])):
        fila=[]
        for j in range(len(x)):
            a=(((x[j][i])[0]))
            b=(((x[j][i])[1]))
            c=(a,b)
            fila.append(c)
        final.append(fila)
    return(final)
def conjumatveccom(x):
    final=[]
    for i in range(len(x)):
        fila=[]
        for j in range(len(x[0])):
            a=(x[j][i])
            c=concom(a)
            fila.append(c)
        final.append(fila)
    return(final)
def adjunmatveccom(x):
    final=[]
    for i in range(len(x[0])):
        fila=[]
        for j in range(len(x)):
            a=(((x[j][i])[0]))
            b=(((x[j][i])[1]))
            c=(a,b)
            d=concom(c)
            fila.append(d)
        final.append(fila)
    return(final)
def producmatcom(x,y):
    try:
        res = [[[0,0] for j in range(len(y[0]))] for i in range(len(x))]
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    res[i][j] = sumacom(res[i][j], multicom(x[i][k], y[k][j]))
        return res
    except:
        return 'Malas dimensiones de matrices'
##def accimatveccom(x,y):
##    res = [[0,0] for j in range(len(y))]
##    print(res)
##    print (y)
##    for i in range(len(x)):
##        for j in range(len(y)):
##            for k in range(len(y)):
##                res[i] = sumacom(res[i], multicom(y[i][k], x[k]))
##
##    return res
##def prodintvec(x,y):
##    compa=adjunmatveccom(x)
##    res=(0,0)
##    for i in range(len(x)):
##        for j in range(len(x)-2):
##            res=sumacom(multicom(compa[i][j],y[i][j]),res)
##    return res

def matcomuni(x):
    res = []
    for i in range(len(x)):
        fila = []
        for k in range(len(x)):
            if i == k:
                fila = fila + [[1,0]]
            else:
                fila = fila + [[0,0]]
        res = res + [fila]
    if producmatcom(x,adjunmatveccom(x))  == res:
        return True
    else:
        return False
def mathermi(x):
    if x==adjunmatveccom(x):
        return True
    else:
        return False






##def tensorcom(x,y):   
##    final=[]
##    for i in range(len(x[0])):
##        for j in range(len(x)):
##            fina2=[]
##            for k in range(len(y[0])):
##                for l in range(len(y)):
##                    q=float((x[i][k])[0])*float((y[j][l])[0])
##                    e=(float((x[i][k])[0])*float((y[j][l])[1]))+((float((x[i][k])[1])*float((y[j][l])[0])))
##                    i=(float((x[i][k])[1])*float((y[j][l])[1])*-1)
##                    q=q+i
##                    fina2.append(q)
##            final.append(fina2)
##    print(final)
###SISTEMA CUANTICO DE PARTICULA EN UNA LINEA ###

    
def prob_parti(x,y):
    total=0
    for i in range(len(x)):
        total=total+modcom(x[i])
    y=modcom(x[y])
    return (total,y)
