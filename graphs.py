#!/usr/bin/env python
# _*_ coding: utf8 _*_

import random
import string
import math
import numpy as np
import queue_1 as que



class Nodo:
    
    def __init__(self, idson, pos):
        self.idson = idson
        self.aristas_salientes = []
        self.pos= pos
        self.aristas_posibles = 0
        self.valorEquis = 0
        self.valorYe =0
        self.visited = False

    def agregar_arista_saliente(self, arista):
        self.aristas_salientes.append(arista)
    def toString(self, nodo):
        return f"Nodo(idson={nodo.idson}, pos={nodo.pos}), visited={nodo.visited}"


class Arista:
    def __init__(self, origen, destino, grado = 1):
        self.origen = origen
        self.destino = destino
        self.grado = grado
        self.distancia = 0
    def toString(self, arista):
        return f"origen={arista.origen}"+" "+f"destino={arista.destino}"

class Grafo:
    def __init__(self):
        self.nodos = []
        self.aristas = []

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)
        return self.nodos

    def agregarArista(self, origen, destino):
        arista = Arista(origen, destino)
        self.aristas.append(arista)
        origen.aristas_salientes.append(arista)

    def grado_nodo(self, nodo):
        return len(nodo.aristas_salientes)
    def generaId(self):
        idcitoBb= "".join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(10)
            )
        return idcitoBb
    def limpiaGrafo(self, grafo):
        for arista in grafo.aristas:
            arista.origen.visited = False
            arista.destino.visited = False
        return grafo
    def toString(self, grafo):
        return f"Grafo(nodos={grafo.nodos}, aristas={grafo.aristas})"
    


    def grafoMalla(self,m, n, dirigido=False):
        """
        Genera grafo de malla
        :param m: número de columnas (> 1)
        :param n: número de filas (> 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        t = 0; s = 0
        for x in range(m):
            print(m)
            l = list()
            for y in range(n):
                print(n)
                idcito = self.generaId
                print(idcito)
                pos = f"{t},{s}"
                s+=1
                nodo = Nodo(idcito, pos)
                print(nodo)
                l.append(nodo)
                self.nodos.append(nodo)
            nodos= self.agregar_nodo(self,l)
            t+=1;s=0
        i=0
        j=0
        for i in range(len(nodos)):
            for j in range(len(nodos[i])):
                if j<n-1: 
                    
                    if nodos[i][j].idson == nodos[i][j+1].idson:    
                        nodos[i][j+1].idson = self.generaId()
                    
                    arista = Arista(nodos[i][j],nodos[i][j+1])
                    nodos[i][j].aristas_salientes.append(nodos[i][j+1])
                    self.aristas.append(arista)
                    
                if i<m-1:
                    if (nodos[i][j].idson == nodos[i+1][j].idson):
                        nodos[i+1][j].idson = self.generaId()
                    arista = Arista(nodos[i][j], nodos[i+1][j])
                    nodos[i][j].aristas_salientes.append(nodos[i+1][j])
                    self.aristas.append(arista)
                if(i<m-1 and j<n-1):
                    
                    print(str(nodos[i][j].pos)+'--------'+ str(nodos[i][j+1].pos) +'\n|\n|\n|\n|\n'+str(nodos[i+1][j].pos))
                j+=1
            i+=1
        grafito = Grafo()
        grafito.nodos = self.nodos
        grafito.aristas = self.aristas
        return grafito
    
        
    def grafoErdosRenyi(self,n, m, dirigido=False):
        """
        Genera grafo aleatorio con el modelo Erdos-Renyi
        :param n: número de nodos (> 0)
        :param m: número de aristas (>= n-1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        t=0
        for x in range(n):
            for y in range(3):
                l = list()
                idcito = self.generaId()
                nodo = Nodo(idcito, str(t))
                nodos = self.agregar_nodo(nodo)
                t+=1

                if (x >0):
                    numerillo = random.randint(0,x)
                    if(numerillo != [x]):
                        p = 1 - (nodos[x].aristas_posibles/n)
                        if p> random.random():
                            if(nodos[numerillo].aristas_posibles < 4 and nodos[x].aristas_posibles < 4):
                                arista = Arista(nodos[x], nodos[numerillo])
                                self.agregarArista(nodos[x], nodos[numerillo])
                                nodos[numerillo].aristas_posibles +=1
                                nodos[x].aristas_posibles += 1

                if(len(self.aristas) < m-1):
                    break
        grafillo = Grafo()
        grafillo.nodos = self.nodos
        grafillo.aristas = self.aristas
        return grafillo
        
    def grafoGilbert(self,n, p, dirigido=False):
        """
        Genera grafo aleatorio con el modelo Gilbert
        :param n: número de nodos (> 0)
        :param p: probabilidad de crear una arista (0, 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        t=0
        for x in range(n):
            l = list()
            idcito = self.generaId()
            nodo = Nodo(idcito, str(t))
            nodos = self.agregar_nodo(nodo)
            t+=1
        i=0;j=0
        nodos2 = nodos
        for i in range(len(nodos)):
            for j in range(len(nodos2)):
                if(nodos[i].pos != nodos2[j].pos):
                    if(p > random.random()):
                        arista = Arista(nodos[i], nodos2[j])
                        self.agregarArista(nodos[i], nodos2[j])
            j+=1
        i+=1
        grafito = Grafo()
        grafito.nodos = self.nodos
        grafito.aristas = self.aristas
        return grafito

    def grafoGeografico(self,n, r, dirigido=False):
        """
        Genera grafo aleatorio con el modelo geográfico simple
        :param n: número de nodos (> 0)
        :param r: distancia máxima para crear un nodo (0, 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        #Esta función calcula la probabilidad mediante una función exponencial utilizando la distancia
        #la agrego porque si sólo me baso en la distancia, no va a existir un valor probabilístico real
        
        t=0
        for x in range(n):

            idcito = self.generaId()
            nodo = Nodo(idcito, str(t))
            numerilloUno= random.random(); numerilloDos = random.random()
            nodo.valorEquis = numerilloUno; nodo.valorYe = numerilloDos
            nodos = self.agregar_nodo(nodo)
            t+=1
        y=0
        for y in range(n):
            
            
            nodoRandom = nodos[random.randint(0,n-1)]
            index = nodos.index(nodoRandom)
            if(nodoRandom.idson != nodos[y].idson):
                euclidesDist = math.sqrt((nodoRandom.valorEquis - nodos[y].valorEquis)**2 + (nodoRandom.valorYe - nodos[y].valorYe)**2)

                if(euclidesDist < r):
                    self.agregarArista(nodos[y], nodos[index])
                    arista = Arista(nodos[y], nodos[index])
        y+=1
        
        grafito = Grafo()
        grafito.nodos = self.nodos
        grafito.aristas = self.aristas
        return grafito
    
    def grafoBarabasiAlbert(self,n, d, dirigido=False):
        """
        Genera grafo aleatorio con el modelo Barabasi-Albert
        :param n: número de nodos (> 0)
        :param d: grado máximo esperado por cada nodo (> 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        t=0; x=0
        for x in range(d):
            idcito = self.generaId()
            nodo = Nodo(idcito, str(t))
            nodos = self.agregar_nodo(nodo)
            t+=1
            if(x>0 and x< len(range(d))):
                self.agregarArista(nodos[x], nodos[x-1])
                nodos[x].aristas_posibles +=1
                nodos[x-1].aristas_posibles +=1
                if x == d-1:
                    
                    self.agregarArista(nodos[x], nodos[0])
                    nodos[x].aristas_posibles +=1
                    nodos[0].aristas_posibles +=1
            x+=1
        y=0;s=0;l=d
        for y in range(len(nodos), n):
            idcito = self.generaId()
            nodo = Nodo(idcito, str(l))
            nodos = self.agregar_nodo(nodo)
            l+=1
            
            numerillo =  random.randint(0, y-1)
            if(nodos[y].idson != nodos[numerillo]):
                self.agregarArista(nodos[y], nodos[numerillo])

            y+=1
        grafito = Grafo()
        grafito.nodos = self.nodos
        grafito.aristas = self.aristas
        return grafito

    def grafoDorogovtsevMendes(self,n, dirigido=False):
        """
        Genera grafo aleatorio con el modelo Barabasi-Albert
        :param n: número de nodos (≥ 3)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        d=3
        t=0; x=0
        for x in range(d):
            idcito = self.generaId()
            nodo = Nodo(idcito, str(t))
            nodos = self.agregar_nodo(nodo)
            t+=1
            if(x>0 and x< len(range(d))):
                self.agregarArista(nodos[x], nodos[x-1])
                nodos[x].aristas_posibles +=1
                nodos[x-1].aristas_posibles +=1
                if x == d-1:
                    
                    self.agregarArista(nodos[x], nodos[0])
                    
                    nodos[x].aristas_posibles +=1
                    nodos[0].aristas_posibles +=1
            x+=1
        y=0;l=d
        for y in range(len(nodos), n):
            idcito = self.generaId()
            nodo = Nodo(idcito, str(l))
            nodos = self.agregar_nodo(nodo)
            l+=1
            
            numerillo =  random.randint(0, y-1)
            if(nodos[y].idson != nodos[numerillo]):
                self.agregarArista(nodos[y], nodos[numerillo])

            y+=1

        grafito = Grafo()
        grafito.nodos = self.nodos
        grafito.aristas = self.aristas
        return grafito
    
    def generaGephi(self, grafo, nombre_archivo):
        dot = "graph G {\n"
        
        x=0
        for arista in grafo.aristas:
            dot += f'  {grafo.aristas[x].origen.pos} -- {grafo.aristas[x].destino.pos};\n'
            x+=1
        dot += "}"
        
        with open(nombre_archivo + '.gv', 'w') as archivo_dot:
            archivo_dot.write(dot)
    