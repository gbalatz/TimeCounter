"""
A script that generates the monthly payment, based on fees.

@author Georgios Balatzis (balatzig)
@author Karoline Stumpf (stumpfk)

Copyright 2017
"""

### Los Variablos ###
stunden = float(input("Gebe Stunden ein : "))
minutos = float(input("Gebe los minutos ein : "))
stundenlohn = 12

"""
Defined Method logic of the script
@params stunden : Integer, Worked hours
@params minutos : Integer , worked minutes
@params stundenlohn : Integer , fee pay per hour
@return Lohn :  Actual payment
"""

def Gehalt(Std, Min, Std_Lohn):

	# In place variables
	Min=(10.0/6.0)*Min*(1.0/100.0)
	Std += Min
	Lohn=Std_Lohn*(Std)

	if Lohn>=2000.0:
		return round((Lohn*(1.0-0.158))*(1.0-0.0935),2)
	elif Lohn>=950.0:
# Solidarittszuschlag und Lohnsteuer bei ungefaehr 15,7 %
		return round((Lohn*(1.0-0.024))*(1.0-0.0935),2)
	else:
		return round(Lohn*(1.0-0.0935),2)

#Main Script Output
print ("\n" "Mein Gehalt diesen Monat betraegt %s Euro."%((Gehalt(stunden,minutos,stundenlohn))))
