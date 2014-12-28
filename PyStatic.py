#-*- coding:utf-8 -*-
"""module PyStatic permettant d'utiliser du typage statique en Python"""
from types import *

def static(cls):
    """Décrit un décorateur qui permet de définir statiquement une fonction"""
    """    cls:type du renvoi"""
    def wrapper(fonction):
        def sousWrapper(*args,**kwargs):
            if(type(fonction(*args,**kwargs)) is cls):
                fonction(*args,**kwargs)
            else:
                raise TypeError("type of {0} is not {1}".format(fonction(*args,**kwargs),cls))
        return sousWrapper
    return wrapper


@static(bool)
def let(cls,name,value):
    """Assigne statiquement une valeur à une variable"""
    """    cls: type de la variable"""
    """    name: nom de la variable"""
    """    value: valeur de la variable"""
    if(type(value) is cls):
        if(type(value) is FunctionType):
            globals()[name] = value
        else:
            globals()[name] = cls(value)
        return True
    else:
        raise TypeError("type of {0} is not {1}".format(value,cls))
        return False
        


    
        

