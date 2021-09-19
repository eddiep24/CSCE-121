import math as m

# take pi and multiply by 10^degree then subtract base then multiply back then subtract it from pi

degree = int(input(("Please enter the number of digits of precision for pi:")))

bigpi = (m.pi * 10**(degree) - m.floor(m.pi * 10**(degree)))
bigtosmall = 10**(-(degree))
pimoved = bigpi * bigtosmall

final = m.pi - pimoved
print(" The value of pi to", degree, "digits is:", final)
