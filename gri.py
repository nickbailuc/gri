#!/usr/bin/env python3

##  Author = "Nick Bailuc"
##  Copyright = "Copyright (C) 2018 Nick Bailuc, <nick.bailuc@gmail.com>"
##  License = "GNU General Public License, version 3 or later"
##  version = "1.01-python3"
##
##
##  "Generator of Recurring Integers" (or "GRI")
##  is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 3 of the License, or
##  (at your option) any later version.
##
##  GRI is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.


import math

def gri(x, λ1, λ2):
    '''int->flo
    "Generator of Recurring Integers" or "GRI" generates numbers
    with recurring elements, based on specified integers and limits.
    See also: agri , igri
    
    x = Periodic integer
    λ1 = Initiating place-value
    λ2 = Terminating place-value
    λ1 < λ2
    '''
    
    k = math.floor(math.log10(abs(x)))+1
    sum = 0
    for i in range(λ1, λ2):
        sum = sum + 10**(k*i)
    return sum*x

def agri(x):
    '''int->flo
    Automated version of the GRI program. Does not require place-value
    entries, but the output is only accurate to 2^16 decimal places!

    "Generator of Recurring Integers" or "GRI" generates numbers
    with recurring elements, based on specified integers and limits.
    See also: gri , igri
    
    x = Periodic integer
    '''
    
    k = math.floor(math.log10(abs(x)))+1
    sum = 0
    for i in range(-65536, 0):
        sum = sum + 10**(k*i)
    return sum*x

def igri():
    '''int->flo
    Interactive version of the GRI program. Run without arguments!

    "Generator of Recurring Integers" or "GRI" generates numbers
    with recurring elements, based on specified integers and limits.
    See also: gri , agri
    '''
    
    x = int(input("Periodic integer = "))
    λ1 = int(input("Initiating place-value = "))
    λ2 = int(input("Terminating place-value = "))
    k = math.floor(math.log10(abs(x)))+1
    sum = 0
    for i in range(λ1, λ2):
        sum = sum + 10**(k*i)
    return sum*x
