# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:44:23 2022
@author: Kahé Yami
"""

import random
from re import A

bacteria = 0
planta = 0
agua = 0

variable1 = random.randint(1,4)

if variable1 == 3 or variable1 ==4:
    variable1 = "b"
    bacteria +=1
else:
    if variable1 == 1:
        variable1 = "p"
        planta += +1
    else:
        if variable1 == 2:
            variable1 = "a"
            agua += +1
            
variable2 = random.randint(1,4)

if variable2 == 3 or variable2 ==4:
    variable2 = "b"
    bacteria +=1
else:
    if variable2 == 1:
        variable2 = "p"
        planta += +1
    else:
        if variable2 == 2:
            variable2 = "a"
            agua += +1

variable3 = random.randint(1,4)

if variable3 == 3 or variable3 ==4:
    variable3 = "b"
    bacteria +=1
else:
    if variable3 == 1:
        variable3 = "p"
        planta += +1
    else:
        if variable3 == 2:
            variable3 = "a"
            agua += +1

variable4 = random.randint(1,4)

if variable4 == 3 or variable4 ==4:
    variable4 = "b"
    bacteria +=1
else:
    if variable4 == 1:
        variable4 = "p"
        planta += +1
    else:
        if variable4 == 2:
            variable4 = "a"
            agua += +1            

variable5 = random.randint(1,4)

if variable5 == 3 or variable5 ==4:
    variable5 = "b"
    bacteria +=1
else:
    if variable5 == 1:
        variable5 = "p"
        planta += +1
    else:
        if variable5 == 2:
            variable5 = "a"
            agua += +1


variable6 = random.randint(1,4)

if variable6 == 3 or variable6 ==4:
    variable6 = "b"
    bacteria +=1
else:
    if variable6 == 1:
        variable6 = "p"
        planta += +1
    else:
        if variable6 == 2:
            variable6 = "a"  
            agua += +1   

variable7 = random.randint(1,4)

if variable7 == 3 or variable7 ==4:
    variable7 = "b"
    bacteria +=1
else:
    if variable7 == 1:
        variable7 = "p"
        planta += +1
    else:
        if variable7 == 2:
            variable7 = "a"
            agua += +1

variable8 = random.randint(1,4)

if variable8 == 3 or variable8 ==4:
    variable8 = "b"
    bacteria +=1
else:
    if variable8 == 1:
        variable8 = "p"
        planta += +1
    else:
        if variable8 == 2:
            variable8 = "a"
            agua += +1

variable9 = random.randint(1,4)

if variable9 == 3 or variable9 ==4:
    variable9 = "b"
    bacteria +=1
else:
    if variable9 == 1:
        variable9 = "p"
        planta += +1
    else:
        if variable9 == 2:
            variable9 = "a"
            agua += +1
            
variable10 = random.randint(1,4)

if variable10 == 3 or variable10 ==4:
    variable10 = "b"
    bacteria +=1
else:
    if variable10 == 1:
        variable10 = "p"
        planta += +1
    else:
        if variable10 == 2:
            variable10 = "a"
            agua += +1            

variable11 = random.randint(1,4)

if variable11 == 3 or variable11 ==4:
    variable11 = "b"
    bacteria +=1
else:
    if variable11 == 1:
        variable11 = "p"
        planta += +1
    else:
        if variable11 == 2:
            variable11 = "a"
            agua += +1

variable12 = random.randint(1,4)

if variable12 == 3 or variable12 ==4:
    variable12 = "b"
    bacteria +=1
else:
    if variable12 == 1:
        variable12 = "p"
        planta += +1
    else:
        if variable12 == 2:
            variable12 = "a"
            agua += +1

variable13 = random.randint(1,4)

if variable13 == 3 or variable13 ==4:
    variable13 = "b"
    bacteria +=1
else:
    if variable13 == 1:
        variable13 = "p"
        planta += +1
    else:
        if variable13 == 2:
            variable13 = "a"
            agua += +1

variable14 = random.randint(1,4)

if variable14 == 3 or variable14 ==4:
    variable14 = "b"
    bacteria +=1
else:
    if variable14 == 1:
        variable14 = "p"
        planta += +1
    else:
        if variable14 == 2:
            variable14 = "a"
            agua += +1

variable15 = random.randint(1,4)

if variable15 == 3 or variable15 ==4:
    variable15 = "b"
    bacteria +=1
else:
    if variable15 == 1:
        variable15 = "p"
        planta += +1
    else:
        if variable15 == 2:
            variable15 = "a"
            agua += +1

variable16 = random.randint(1,4)

if variable16 == 3 or variable16 ==4:
    variable16 = "b"
    bacteria +=1
else:
    if variable16 == 1:
        variable16 = "p"
        planta += +1
    else:
        if variable16 == 2:
            variable16 = "a"
            agua += +1


print("------------------")
print("|", variable1,   "|", variable2,   "|", variable3,   "|", variable4,   "|")
print("------------------")
print("|", variable5,   "|", variable6,   "|", variable7,   "|", variable8,   "|")
print("------------------")
print("|", variable9,   "|", variable10,   "|", variable11,   "|", variable12,   "|")
print("------------------")
print("|", variable13,   "|", variable14,   "|", variable15,   "|", variable16,   "|")
print("------------------")


print("existen", bacteria, "elementos de bacteria, existen", planta, "elementos de planta, existen", agua, "elementos de agua" )

total = (bacteria + planta + agua)

porcentajeB = (bacteria * 100) / total
porcentajeP = (planta * 100) / total
porcentajeA = (agua * 100) / total
print ("el porcentaje de ocurrencia de las bacterias es ", porcentajeB,"%, el porcentaje de ocurrencia de las plantas es ", porcentajeP, "% y el porcentaje de ocurrencia del agua es de ", porcentajeA, "%")
if bacteria == planta:
    print("la ocurrencia de las bacterias y las plantas han empatado")
else:
    if planta == agua:
        print("la ocurrencia de las plantas y el agua han empatado")
    else:
        if bacteria == agua:
            print("la ocurrencia de las bacterias y el agua han empatado")
        else:
            if bacteria > planta > agua:
                print("las bacterias tienen mayor ocurrencia, mientras que el agua tiene la menor ocurrencia")
            else:
                if planta > bacteria > agua:
                    print("las plantas tienen mayor ocurrencia mientras que el agua tiene la menor ocurrencia")
                else:
                    if bacteria > agua > planta:
                        print("las bacterias tienen mayor ocurrencia mientras que las plantas tienen la menor ocurrencia")
                    else:
                        if planta > agua > bacteria:
                            print("las plantas tienen mayor ocurrencia mientras que las bacterias tiene la menor ocurrencia")
                        else:
                            if agua > planta > bacteria:
                                print("el agua tienen mayor ocurrencia mientras que las bacterias tiene la menor ocurrencia")
                            else:
                                if agua > bacteria > planta:
                                    print("el agua tienen mayor ocurrencia mientras que las plantas tiene la menor ocurrencia")


    


