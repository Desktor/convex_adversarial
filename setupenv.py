#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:20:58 2021

@author: felix
"""

import json
from subprocess import run
import argparse
    
def conda_list():
    proc = run(["conda", "list", "torchvision|pytorch"], 
                   text=True, capture_output=True)
    return proc.stdout

def conda_check():
    try:
        import torch
        import torchvision
    except ImportError:
        return False
    
    return torch.__version__=="1.6.0" and torchvision.__version__=="0.8.1"

def conda_installenv():
    print('installing environment')
    proc = run(["conda", "env", "create", "-f", "convex-adversarial.yml", '-y'], text=True, capture_output=True)
    return proc.stdout

if __name__ == "__main__":
    print('This program prints whether current or the given environment contains the necessary packages to run the code in convex-adversarial')
    t=conda_list()
    print(t)
    
    u=conda_check()
    
    if u == False:
        print('\n','wrong versions of the packages, do you want to setup environment?')
        while True:
            try:
                i=input('(y/n):')
                if i =="y" or i =="yes":
                    conda_installenv()
                    break
                if i =="n" or i == "no":
                    break
            except:
                continue