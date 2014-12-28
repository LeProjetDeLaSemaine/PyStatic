#-*- coding:utf-8 -*-
"""module PyStatic permettant d'utiliser du typage statique en Python"""
from types import *

def staticArgs(*t):
    """décrit un décorateur permettant de définir le type des arguments passés à une fonction"""
    """   *t:tuple contenant les types des variables (dans l'ordre)"""
    """   0 ignore l'argument actuel et passe au suivant"""
    def wrapper(fonction):
        def sousWrapper(*args,**kwargs):
            for el in range(len(args)):
                if(t[el]==0):
                    pass
                elif (type(args[el])!= t[el]):
                    raise TypeError("type of {0} is not {1}".format(args[el],t[el]))
            fonction(*args,**kwargs)
        return sousWrapper
    return wrapper
                    
    
def staticFunc(cls):
    """Décrit un décorateur qui permet de définir statiquement une fonction"""
    """    cls:type du renvoi"""
    def Wrapper(fonction): #notez l'originalité du nom
        def wrapper(*args,**kwargs): #quelle nom bien trouvé!!!
            if(type(fonction(*args,**kwargs)) is cls):
                fonction(*args,**kwargs)
            else:
                raise TypeError("type of {0} is not {1}".format(fonction(*args,**kwargs),cls))
        return wrapper
    return Wrapper

@staticArgs(type,str,0)
@staticFunc(bool)
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
        
 
        

