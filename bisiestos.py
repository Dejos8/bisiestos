#coding: utf­8
print 'Escriba un año:'
anio=int(input())
if (anio%4==0 and anio%100!=0)or anio%400==0:
    print"El año", str(anio), "es bisiesto"
else:
    print "El año ",str(anio)," no es bisiesto"
