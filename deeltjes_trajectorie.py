"""
Name:

Date:

Porgram description:
"""

def deeltje_trajectorie(t, zwaartekracht, beginsnelheid):
   positie = -0.5 * zwaartekracht * t**2 + beginsnelheid * t
   return positie