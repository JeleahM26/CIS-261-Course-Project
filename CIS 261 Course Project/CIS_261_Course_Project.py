#Jeleah Mclean 
#CIS 261 

def getDatesWorked():
    fromDate = input("Please enter start date in the following formatMM/DD/YYYY: ")
    endDate = input("Please enter end date in the following format MM/DD/YYYY: ")
    return fromDate, endDate


def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getHoursworked ():
    hours =float(input("Enter Hours: "))
    return hours

def getHourlyRate() :
    hourlyRate = float(input("Enter Hourly Rate: "))
    return hourlyRate

def getTaxRate():
    taxrate = float(input("Enter tax Rate"))
    taxrate = taxrate / 100
    return taxrate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

    
def PrintTotals(totalEmployees, totalHours, totalGrossPay, totalTax,
totalNetPay):
    print(f"\nTotal Number Of Employees: {totalEmployees}")
    print(f"Total Hours: {totalHours:,.2f}")
    print(f"Total Gross Pay: {totalGrossPay:,.2f}")
    print(f"Total Tax: {totalTax:,.2f}")
    print(f"Total Net Pay: {totalNetPay:,.2f}")
    
def printTotals(empTotals):
    print(f'Total Number Of Employees: {empTotals["totEmp"]}')
    print(f'Total Hours Of Employees: {empTotals["totHours"]}')
    print(f'Total Gross Pay Of Employees: {empTotals["totGross"]}')
    print(f'Total Tax Of Employees: {empTotals["totTax"]}')
    print(f'Total Net Pay Of Employees: {empTotals["totNet"]}')
    
if __name__ == "__main__":
    while True:
        empName = getEmpName()
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursworked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()


                      

    
    


    