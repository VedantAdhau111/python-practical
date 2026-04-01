# Vendor Purchase Report

vendor_name = input("Enter vendor name: ")
year = int(input("Enter year of association: "))
contact = input("Enter contact number: ")
email = input("Enter email ID: ")

annual_total = 0

print("\nEnter monthly purchase amounts:")
for i in range(1, 13):
    amount = float(input(f"Month {i}: "))
    annual_total += amount

print("\n--- Vendor Annual Report ---")
print("Vendor Name:", vendor_name)
print("Year of Association:", year)
print("Contact:", contact)
print("Email:", email)
print("Total Annual Purchase:", annual_total)

# Employee Salary Program

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
department = input("Enter department: ")
basic_salary = float(input("Enter basic salary: "))

da = 0.92 * basic_salary
hra = 0.58 * basic_salary
ta = 0.30 * basic_salary
lic = 500
gross_salary = basic_salary + da + hra + ta
net_salary = gross_salary - lic

print("\n--- Employee Salary Details ---")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)
print("Basic Salary:", basic_salary)
print("DA:", da)
print("HRA:", hra)
print("TA:", ta)
print("LIC Deduction:", lic)
print("Net Salary:", net_salary)
