

#+ dodawanie
#- odejmowanie
#* mnożenie
#/ dzielenie
#
#() - jak w matematyce kierują kolejnością działania
#
#** potęgowanie
#// dzielenie w "dół"
#% - modulo (reszta z dzielenia)



cenaNettoJavaPLN = 1000
cenaNettoAjaxPLN = 2000

Vat = 23
obliczonyVAT = (1 + Vat / 100)
cenabruttoJavaPLN = cenaNettoJavaPLN * (1 + Vat / 100)
cenaBruttoAjaxPLN = cenaNettoAjaxPLN * (1 + Vat / 100)
print(cenabruttoJavaPLN)
print(cenaBruttoAjaxPLN)