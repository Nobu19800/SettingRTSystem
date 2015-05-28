#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys
import imp


def getFunc(filename, filepath):
    try:
            sys.path.append(filepath[0])
            (file, pathname, description) = imp.find_module(filename, filepath)
            
            mod = imp.load_module(filename, file, pathname, description)
            func = getattr(mod,filename+"Init",None)

            return func
    except:
            return None

print getFunc("MultipleOrderedEC",["./"])
