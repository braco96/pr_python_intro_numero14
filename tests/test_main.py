import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_contar_llamadas():
    @mod.contar_llamadas
    def suma(a,b): return a+b
    assert suma(1,2) == 3
    assert suma(2,2) == 4
    assert suma.contador["n"] == 2
