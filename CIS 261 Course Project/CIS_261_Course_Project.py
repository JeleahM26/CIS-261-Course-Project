#Jeleah Mclean 
#CIS 261 
#Course Project Part 1-2

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

def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    for empList in empDetailList:
        fromDate = empList[0]
        endDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]


def printinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax,netPay):
    print(empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}",f"{gPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}",f"{netPay:,.2f}")
    
    totalEmployees += 1
    totalHours += hours
    totalGrossPay += gPay
    totalTax += incomeTax
    totalNetPay += netPay
    
    empTotals["totEmp"] = totalEmployees
    empTotals["totHours"] = totalHours
    empTotals["totGross"] = totalGrossPay
    empTotals["totTax"] = totalTax
    empTotals["totNet"] = totalNetPay



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
    empDetailList = []
    empTotals = {}
    while True:
        empName = getEmpName()
        if (empName.lower() == "end"):
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursworked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        empDetail = []
        empDetail.insert(0, fromDate)
        empDetail.insert(1, endDate)
        empDetail.insert(2, empName)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourlyRate)
        empDetail.insert(5, taxRate)
        empDetailList.append(empDetail)
    printInfo(empDetailList)
    printTotals(empTotals)


                      

    
    


    