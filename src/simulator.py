#!/usr/bin/python

"""
This program was developed for KSP2Mars
to simulate vessels' ascent and staging
performance on both Earth and Mars.
"""

from decimal import *

def atmo_earth(h):
    p = -1
    rho = -1
    a0 = -1

    if h < 11000:
        T = 15.04 - 0.00649 * h + 273.1
        P = 101.29 * exp((T/288.08),5.256)
    elif h < 25000:
        T = -56.46 + 273.1
        P = 22.65 * exp(1.73 - 0.000157 * h)
    else:
        T = -131.21 + 0.00299 * h + 273.1
        P = 2.488 * exp( T / 216.6, -11.388 )
    rho = P / (0.2869 * T)

    gamma = 1.4
    R = 287

    a0 = sqrt(gamma * R * T)

    return [ P, rho, a0 ]

def atmo_mars(h):
    if h < 7000:
        T = -31 - .000998*h + 273.1
        P = .699*exp(-.00009*h)
    else:
        T = -23.4 - .00222*h + 273.1
        P = .699*exp(-.00009*h)

    rho = (P)/(.1921*(T))
    gamma = 1.4
    R = 287

    a0 = sqrt(gamma * R * T);
    
    return [ P, rho, a0 ]

def planet_parameters( Planet ):

    if 'Earth' == Planet:
        R_planet = 6371000
        Omega_planet = (2*pi)/(23.9345*60*60)
        AtmoAlt_planet = 130000
        GM_planet = 3.986004418E+14
    elif 'Mars' == Planet:
        R_planet = 3389500
        Omega_planet = (2*pi)/(24.6229*60*60)
        AtmoAlt_planet = 130000
        GM_planet = 4.2828E13
    else:
        R_planet = 0
        Omega_planet = 0
        AtmoAlt_planet = 0
        GM_planet =  0
        Planet = 'Error'  

    return [ R_planet, Omega_planet, AtmoAlt_planet, GM_planet, Planet ]
