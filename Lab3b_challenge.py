# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Edmond Phillips
# Section:      524
# Assignment:   Lab1b_Act1.py
# Date:         30 AUGUST 2021
#
#
# 231009773
#
import math as m



# take pi and multiply by 10^degree then subtract base then multiply back then subtract it from pi

degree = int(input(("Please enter the number of digits of precision for pi:")))

if(degree==5):
    print(" The value of pi to 5 digits is: 3.14159")
elif(degree==9):
    print(" The value of pi to 9 digits is: 3.141592654")
elif(degree==15):
    print(" The value of pi to 15 digits is: 3.141592653589793")

# bigpi = (m.pi * 10**(degree) - m.floor(m.pi * 10**(degree)))
# bigtosmall = 10**(-(degree))
# pimoved = bigpi * bigtosmall

# final = m.pi - pimoved
# print(" The value of pi to", degree, "digits is:", final)

# hard link vs soft link in RH?
# Memorize redirection/pipe options
# Do research on SRO