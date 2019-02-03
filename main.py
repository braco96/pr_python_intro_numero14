# -*- coding: utf-8 -*-
import re
def contar_llamadas(fn):
    contador = {"n":0}
    def env(*a, **k):
        contador["n"] += 1
        return fn(*a, **k)
    env.contador = contador
    return env

