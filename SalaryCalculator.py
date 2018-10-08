'''
Created on Oct 7, 2018

@author: ekinkade20
'''
hourRate=float(input("Please enter hourly rate: "))
hoursPerWeek = float(input("PLease enter number of hours per week: "))
weeklyPay=hourRate*hoursPerWeek
monthlyPay=weeklyPay*4
annualPay=monthlyPay*12

print("Salary:")
print("\t",format("weeklyPay:",'<12s'),format(weeklyPay,'10,.2f'))
print("\t",format("monthlyPay:",'<12s'),format(monthlyPay,'10,.2f'))
print("\t",format("annualPay:",'<12s'),format(annualPay,'10,.2f'))