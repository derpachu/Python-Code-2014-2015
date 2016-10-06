A = input ("air temperature measurement: ")
B = input ("Wind speed measurement: ")

atm = float(A)
wsm = float(B)

WCT = 35.74+0.6215*atm-35.75*(wsm**0.16)+0.4275*atm*wsm**0.16

print ("Air temperature is ", atm)
print ("Wind speed is ", wsm)
print ("Wind chill temperature is ", WCT)
