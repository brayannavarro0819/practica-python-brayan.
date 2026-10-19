
# Alumno: Brayan Daniel De Jesús Muñoz Navarro
# Matrícula: 2630463
# Grupo: 1-3
# ============================================================

# EXECUTIVE SUMMARY
# The int type stores whole numbers, while float stores numbers with decimals.
# A Boolean is a logical value: True or False.
# Comparisons such as >=, <, and == produce Boolean values.
# Input validation checks that data has the correct type and a reasonable range.
# Validation prevents invalid calculations, including division by zero.
# This file contains six problems using calculations, conditions, and Boolean values.
# Each problem documents its description, inputs, outputs, validations, and test cases.

# GOOD PROGRAMMING PRACTICES
# 1. Use int for whole-number quantities and float for decimal quantities.
# 2. Store intermediate results in descriptive variables.
# 3. Validate input before performing calculations.
# 4. Use descriptive variable names and clear output messages.
# 5. Interpret each Boolean explicitly: True means the stated condition is met;
#    False means it is not met.

# ============================================================
# Problem 1: Temperature converter and range flag
# Description:
# Convert Celsius to Fahrenheit and Kelvin. Also indicate whether
# the Celsius temperature is at least 30 degrees.
#
# Inputs: temp_c (float, degrees Celsius).
# Outputs: Fahrenheit, Kelvin, and High temperature (True/False).
# Validations: Input must be numeric; Kelvin cannot be below zero.
# Test cases:
# 1) Normal: 25 -> Fahrenheit 77.0, Kelvin 298.15, High temperature False.
# 2) Border: -273.15 -> Fahrenheit -459.67, Kelvin 0.0, False.
# 3) Error: "abc" -> Error: invalid input.
# ============================================================

def problem_1():
    try:
        temp_c = float(input("Enter temperature in Celsius: "))
        temp_k = temp_c + 273.15

        if temp_k < 0.0:
            print("Error: invalid input")
            return

        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("High temperature:", str(is_high_temperature).lower())
    except ValueError:
        print("Error: invalid input")


# ============================================================
# Problem 2: Work hours and overtime payment
# Description:
# Calculate weekly pay. The first 40 hours are paid at the normal rate;
# additional hours are paid at 150% of the normal hourly rate.
#
# Inputs: hours_worked (float), hourly_rate (float).
# Outputs: Regular pay, overtime pay, total pay, and Has overtime.
# Validations: hours_worked >= 0 and hourly_rate > 0.
# Test cases:
# 1) Normal: 45 hours at 20 -> regular 800, overtime 150, total 950.
# 2) Border: 40 hours at 20 -> regular 800, overtime 0, total 800.
# 3) Error: -2 hours at 20 -> Error: invalid input.
# ============================================================

def problem_2():
    try:
        hours_worked = float(input("Enter hours worked this week: "))
        hourly_rate = float(input("Enter hourly rate: "))

        if hours_worked < 0 or hourly_rate <= 0:
            print("Error: invalid input")
            return

        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(hours_worked - 40.0, 0.0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40

        print("Regular pay:", round(regular_pay, 2))
        print("Overtime pay:", round(overtime_pay, 2))
        print("Total pay:", round(total_pay, 2))
        print("Has overtime:", str(has_overtime).lower())
    except ValueError:
        print("Error: invalid input")


# ============================================================
# Problem 3: Discount eligibility with booleans
# Description:
# A customer receives a 10% discount if they are a student, are a senior,
# or have a purchase total of at least 1000.
#
# Inputs: purchase_total (float), is_student_text (YES/NO),
#         is_senior_text (YES/NO).
# Outputs: Discount eligible and Final total.
# Validations: purchase_total >= 0; answers must be YES or NO.
# Test cases:
# 1) Normal: 500, YES, NO -> eligible True, final total 450.
# 2) Border: 1000, NO, NO -> eligible True, final total 900.
# 3) Error: 100, MAYBE, NO -> Error: invalid input.
# ============================================================

def problem_3():
    try:
        purchase_total = float(input("Enter purchase total: "))
        is_student_text = input("Is the customer a student? (YES/NO): ").strip().upper()
        is_senior_text = input("Is the customer a senior? (YES/NO): ").strip().upper()

        if purchase_total < 0 or is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
            print("Error: invalid input")
            return

        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"
        discount_eligible = is_student or is_senior or purchase_total >= 1000.0

        if discount_eligible:
            final_total = purchase_total * 0.90
        else:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", round(final_total, 2))
    except ValueError:
        print("Error: invalid input")


# ============================================================
# Problem 4: Basic statistics of three integers
# Description:
# Read three integers and calculate their sum, average, maximum,
# minimum, and whether all three numbers are even.
#
# Inputs: n1, n2, n3 (integers).
# Outputs: Sum, Average, Max, Min, and All even.
# Validations: All three inputs must be valid integers; negatives are allowed.
# Test cases:
# 1) Normal: 2, 4, 6 -> sum 12, average 4.0, max 6, min 2, True.
# 2) Border: 0, -2, 2 -> sum 0, average 0.0, max 2, min -2, True.
# 3) Error: 2, "hello", 6 -> Error: invalid input.
# ============================================================

def problem_4():
    try:
        n1 = int(input("Enter the first integer: "))
        n2 = int(input("Enter the second integer: "))
        n3 = int(input("Enter the third integer: "))

        sum_value = n1 + n2 + n3
        average_value = sum_value / 3
        max_value = max(n1, n2, n3)
        min_value = min(n1, n2, n3)
        all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

        print("Sum:", sum_value)
        print("Average:", round(average_value, 2))
        print("Max:", max_value)
        print("Min:", min_value)
        print("All even:", str(all_even).lower())
    except ValueError:
        print("Error: invalid input")


# ============================================================
# Problem 5: Loan eligibility (income and debt ratio)
# Description:
# Decide whether a person qualifies for a loan based on monthly income,
# monthly debt, and credit score.
#
# Inputs: monthly_income (float), monthly_debt (float), credit_score (int).
# Outputs: Debt ratio and Eligible.
# Validations: income > 0, debt >= 0, and credit score >= 0.
# Test cases:
# 1) Normal: income 10000, debt 2000, score 700 -> ratio 0.2, True.
# 2) Border: income 8000, debt 3200, score 650 -> ratio 0.4, True.
# 3) Error: income 0, debt 100, score 700 -> Error: invalid input.
# ============================================================

def problem_5():
    try:
        monthly_income = float(input("Enter monthly income: "))
        monthly_debt = float(input("Enter monthly debt payments: "))
        credit_score = int(input("Enter credit score: "))

        if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
            print("Error: invalid input")
            return

        debt_ratio = monthly_debt / monthly_income
        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print("Debt ratio:", round(debt_ratio, 2))
        print("Eligible:", str(eligible).lower())
    except ValueError:
        print("Error: invalid input")


# ============================================================
# Problem 6: Body Mass Index (BMI) and category flag
# Description:
# Calculate BMI from weight and height, then identify the BMI category.
# These categories are simple screening ranges, not a medical diagnosis.
#
# Inputs: weight_kg (float), height_m (float).
# Outputs: BMI, Underweight, Normal, and Overweight.
# Validations: weight_kg > 0 and height_m > 0.
# Test cases:
# 1) Normal: 70 kg, 1.75 m -> BMI 22.86, Normal True.
# 2) Border: 50 kg, 1.70 m -> BMI 17.3, Underweight True.
# 3) Error: 70 kg, 0 m -> Error: invalid input.
# ============================================================

def problem_6():
    try:
        weight_kg = float(input("Enter weight in kilograms: "))
        height_m = float(input("Enter height in meters: "))

        if weight_kg <= 0 or height_m <= 0:
            print("Error: invalid input")
            return

        bmi = weight_kg / (height_m * height_m)
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", round(bmi, 2))
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())
    except ValueError:
        print("Error: invalid input")


# ============================================================
# PROGRAM MENU
# Select which problem to run.
# ============================================================

def main():
    print("Python Programming Assignment")
    print("Choose a problem from 1 to 6.")
    print("Enter 0 to exit.")

    while True:
        try:
            choice = int(input("Problem number (0-6): "))
        except ValueError:
            print("Error: invalid input")
            continue

        if choice == 0:
            print("Goodbye!")
            break
        elif choice == 1:
            problem_1()
        elif choice == 2:
            problem_2()
        elif choice == 3:
            problem_3()
        elif choice == 4:
            problem_4()
        elif choice == 5:
            problem_5()
        elif choice == 6:
            problem_6()
        else:
            print("Error: invalid input")


if __name__ == "__main__":
    main()


# ============================================================
# CONCLUSIONES
# Los números enteros se usan para cantidades completas y los flotantes
# permiten trabajar con valores decimales en cálculos de la vida real.
# Las comparaciones generan valores booleanos (True o False) que ayudan
# al programa a tomar decisiones mediante instrucciones como if.
# Validar los datos permite comprobar que las entradas sean correctas
# y evita errores, como dividir entre cero.
# Los operadores and, or y not permiten combinar condiciones para evaluar
# diferentes situaciones y tomar decisiones de manera adecuada.
# Estos conocimientos se pueden aplicar en cálculos de nómina, descuentos,
# préstamos y mediciones.
# ============================================================

# REFERENCES
# 1. Python Software Foundation. Built-in Types:
#    https://docs.python.org/3/library/stdtypes.html
# 2. Python Software Foundation. Built-in Functions:
#    https://docs.python.org/3/library/functions.html
# 3. Python Software Foundation. Errors and Exceptions:
#    https://docs.python.org/3/tutorial/errors.html
# 4. Python Software Foundation. More Control Flow Tools:
#    https://docs.python.org/3/tutorial/controlflow.html
# 5. Python Software Foundation. An Informal Introduction to Python:
#    https://docs.python.org/3/tutorial/introduction.html
# 6. Python Software Foundation. Numeric Types — int, float:
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
#
# GITHUB REPOSITORY
# Paste the public URL of your GitHub repository here after uploading this file.
# Example format: https://github.com/your-username/your-repository
