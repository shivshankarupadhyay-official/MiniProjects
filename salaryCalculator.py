salary = int(input("ENTER THE BASIC SALARY: "))
hra = int(input("ENTER THE HRA PERCENTAGE:"))
da = int(input("ENTER THE DA PERCENTAGE : "))


tax = int(input("ENTER THE TAX PERCENTAGE: "))
HRA = (salary*hra)/100
DA = (salary*da)/100
gross_salary = salary+HRA+DA
Tax = (gross_salary*tax)/100
netSalary = gross_salary-Tax


print(f"THE HRA IS : {HRA}")
print(f"THE DA IS : {DA}")
print(f"THE GROSS SALARY IS : {gross_salary}")
print(f"THE NET SALARY IS : {gross_salary - Tax}")
