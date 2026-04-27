#Now we will learn about control flow in Python which includes if statements, loops
#Control flow refers to the order in which individual statements, instructions, or function calls are executed or evaluated in a programming language. In Python, control flow is managed using various constructs such as if statements, loops, and functions.
#1. If Statements:
#If statements are used to execute a block of code only if a specified condition is true.
#Syntax:
# if condition:
#     # block of code to be executed if the condition is true
#Example:
x = 10
if x > 5:
    print("x is greater than 5")
#Output: x is greater than 5
#In this example, the condition x > 5 is true, so the block of code inside the if statement is executed, and "x is greater than 5" is printed.
#else statements can be used to execute a block of code if the condition is false.
#Syntax:
# if condition:
#     # block of code to be executed if the condition is true
# else:
#     # block of code to be executed if the condition is false
#Example:
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
#Output: x is not greater than 5
#In this example, the condition x > 5 is false, so the block of code
#inside the else statement is executed, and "x is not greater than 5" is printed.
#else if statements can be used to check multiple conditions.
#Syntax:
# if condition1:
#     # block of code to be executed if condition1 is true
# elif condition2:
#     # block of code to be executed if condition2 is true
# else:
#     # block of code to be executed if both condition1 and condition2 are false
#Example:
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but not greater than 10")
else:
    print("x is not greater than 5")
#Output: x is greater than 5 but not greater than 10
#In this example, the condition x > 10 is false, but the condition x > 5 is true, so the block of code inside the elif statement is executed, and "x is greater than 5 but not greater than 10" is printed. 
#Nested if statements can be used to check multiple conditions within another condition.
#Syntax:
# if condition1:
#     if condition2:
#         # block of code to be executed if both condition1 and condition2 are true
#     else:
#         # block of code to be executed if condition1 is true but condition2 is false
# else:
#     # block of code to be executed if condition1 is false
#Example:
x = 8
if x > 5:
    if x < 10:
        print("x is greater than 5 and less than 10")
    else:
        print("x is greater than or equal to 10")
else:
    print("x is not greater than 5")
#Output: x is greater than 5 and less than 10
#In this example, the condition x > 5 is true, so we check the next condition x < 10, which is also true. Therefore, the block of code inside the nested if statement is executed, and "x is greater than 5 and less than 10" is printed.   
#The use of logical operators (and, or, not) can help to combine multiple conditions in if statements.
#Example:
x = 6
y = 3
if x > 5 and y < 5:
    print("x is greater than 5 and y is less than 5")
#Output: x is greater than 5 and y is less than 5
#In this example, both conditions x > 5 and y < 5 are true,
#so the block of code inside the if statement is executed, and "x is greater than 5 and y is less than 5" is printed.
#The use of or operator allows us to check if at least one of the conditions is true.
#Example:
x = 4
y = 6
if x > 5 or y < 5:
    print("Either x is greater than 5 or y is less than 5")
#Output: Either x is greater than 5 or y is less than 5
#In this example, the condition x > 5 is false, but the condition y < 5 is true. Since we are using the or operator, the block of code inside the if statement is executed, and "Either x is greater than 5 or y is less than 5" is printed.
#The not operator can be used to negate a condition.
#Example:
x = 4
if not x > 5:
    print("x is not greater than 5")
#Output: x is not greater than 5
#In this example, the condition x > 5 is false, but since we are using the not operator, the condition not x > 5 is true. Therefore, the block of code inside the if statement is executed, and "x is not greater than 5" is printed.           
#The use of not operator can also be combined with other logical operators to create more complex conditions.
#Example:
x = 4
y = 6
if not (x > 5 and y < 5):
    print("Either x is not greater than 5 or y is not less than 5")
#Output: Either x is not greater than 5 or y is not less than 5
#In this example, the condition x > 5 and y < 5 is false, but since we are using the not operator, the condition not (x > 5 and y < 5) is true. Therefore, the block of code inside the if statement is executed, and "Either x is not greater than 5 or y is not less than 5" is printed.
#The combined use of if statements and logical operators allows us to create complex conditions and control the flow of our program based on multiple criteria.
#Advanced examples with the use of if statements and logical operators:
#Example 1:
x = 7
y = 3
z = 5
if (x > 5 and y < 5) or z == 5:
    print("Either x is greater than 5 and y is less than 5, or z is equal to 5")
#Output: Either x is greater than 5 and y is less than 5, or z is equal to 5
#z is equal to 5
#In this example, the condition (x > 5 and y < 5) is true, and the condition z == 5 is also true. Since we are using the or operator, the block of code inside the if statement is executed, and "Either x is greater than 5 and y is less than 5, or z is equal to 5" is printed.
#Example 2:
x = 4
y = 6
z = 5
if not (x > 5 or y < 5) and z == 5:
    print("Neither x is greater than 5 nor y is less than 5, and z is equal to 5")
#Output: Neither x is greater than 5 nor y is less than 5, and z is equal to 5
#z is equal to 5
#In this example, the condition x > 5 or y < 5 is false, but since we are using the not operator, the condition not (x > 5 or y < 5) is true. Additionally, the condition z == 5 is also true. Since we are using the and operator, the block of code inside the if statement is executed, and "Neither x is greater than 5 nor y is less than 5, and z is equal to 5" is printed.
#Example 3: In this example, we will use if statements and logical operators to determine if a number is positive, negative, or zero.
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
#In this example, we take input from the user and check if the number is greater than
#0, less than 0, or equal to 0 using if statements and logical operators. Based on the condition that is true, we print the appropriate message indicating whether the number is positive, negative, or zero.
#Example 4: In this example, we will use if statements and logical operators to determine if a person is eligible to vote based on their age and citizenship status.
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (yes/no): ")
if age >= 18 and citizenship.lower() == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#In this example, we take input from the user for their age and citizenship status. We then check if the age is greater than or equal to 18 and if the citizenship status is "yes" using if statements and logical operators. If both conditions are true, we print a message indicating that the person is eligible to vote. Otherwise, we print a message indicating that they are not eligible to vote.            
#Example 5: In this example, we will use if statements and logical operators to determine if a student has passed or failed based on their score.
score = int(input("Enter your score: "))
if score >= 60:
    print("You have passed.")
else:
    print("You have failed.")
#In this example, we take input from the user for their score. We then check if the score is greater than or equal to 60 using an if statement. If the condition is true, we print a message indicating that the student has passed. Otherwise, we print a message indicating that they have failed.
#Example 6: In this example, we will use if statements and logical operators to determine if a person is eligible for a discount based on their age and membership status.
age = int(input("Enter your age: "))
membership = input("Are you a member? (yes/no): ")
if (age >= 65 or age <= 12) and membership.lower() == "yes":
    print("You are eligible for a discount.")  
else:  
    print("You are not eligible for a discount.")
#In this example, we take input from the user for their age and membership status. We then check if the age is greater than or equal to 65 or less than or equal to 12, and if the membership status is "yes" using if statements and logical operators. If both conditions are true, we print a message indicating that the person is eligible for a discount. Otherwise, we print a message indicating that they are not eligible for a discount.
#Example 7:
#In this example, we will use if, elif, else statements and logical operators like the and, or, not to determine the grade of a student based on their score and attendance.
score = int(input("Enter your score: "))
attendance = int(input("Enter your attendance percentage: "))
if score >= 90 and attendance >= 90:
    print("You have received an A grade.")
elif score >= 80 and attendance >= 80:
    print("You have received a B grade.")
elif score >= 70 and attendance >= 70:
    print("You have received a C grade.")
elif score >= 60 and attendance >= 60:
    print("You have received a D grade.")
else:
    print("You have received an F grade.")
#In this example, we take input from the user for their score and attendance percentage. We then use a series of if, elif, and else statements along with logical operators to determine the grade of the student based on their score and attendance. The conditions check if the score and attendance meet certain thresholds for each grade, and the appropriate message is printed based on the conditions that are true.
#Example 8:
#In this example, we will advance and use all the statements that we have learned in this chapter to determine if a person is eligible for a loan based on their age, income, credit score, and employment status.
#We will use if,elif, else statements and logical operators like the and, or, not to check multiple conditions for loan eligibility.
age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))
credit_score = int(input("Enter your credit score: "))
employment_status = input("Are you currently employed? (yes/no): ")
if age >= 18 and income >= 30000 and credit_score >= 700 and employment_status.lower() == "yes":
    print("You are eligible for a loan.")
elif age >= 18 and income >= 30000 and credit_score >= 700:
    print("You are eligible for a loan, but you need to be employed.")
elif age >= 18 and income >= 30000:
    print("You are eligible for a loan, but you need to have a good credit score.")
elif age >= 18:
    print("You are eligible for a loan, but you need to have a good income.")
else:
    print("You are not eligible for a loan.")
#In this example, we take input from the user for their age, income, credit score, and employment status. We then use a series of if, elif, and else statements along with logical operators to determine if the person is eligible for a loan based on the provided criteria. The conditions check if the age, income, credit score, and employment status meet certain thresholds for loan eligibility, and the appropriate message is printed based on the conditions that are true.
#Example 9:
#In this example, we will use if statements and logical operators to determine if a person is eligible for a scholarship based on their GPA, extracurricular activities, and financial need.
gpa = float(input("Enter your GPA: "))
extracurricular_activities = input("Do you participate in extracurricular activities? (yes/no): ")
financial_need = input("Do you have financial need? (yes/no): ")
if gpa >= 3.5 and extracurricular_activities.lower() == "yes" and financial_need.lower() == "yes":
    print("You are eligible for a scholarship.")
elif gpa >= 3.5 and extracurricular_activities.lower() == "yes":
    print("You are eligible for a scholarship, but you need to have financial need.")
elif gpa >= 3.5 and financial_need.lower() == "yes":
    print("You are eligible for a scholarship, but you need to participate in extracurricular activities.")
elif extracurricular_activities.lower() == "yes" and financial_need.lower() == "yes":
    print("You are eligible for a scholarship, but you need to have a good GPA.")
else:
    print("You are not eligible for a scholarship.")
#In this example, we take input from the user for their GPA, extracurricular activities, and financial need. We then use a series of if, elif, and else statements along with logical operators to determine if the person is eligible for a scholarship based on the provided criteria. The conditions check if the GPA, extracurricular activities, and financial need meet certain thresholds for scholarship eligibility, and the appropriate message is printed based on the conditions that are true.
#Example 10:
#In this example, we will use if statements and logical operators to determine if a person is eligible for a job based on their qualifications, experience, and interview performance.
qualifications = input("Do you have the required qualifications? (yes/no): ")
experience = int(input("Enter your years of experience: "))
interview_performance = input("Did you perform well in the interview? (yes/no): ")
if qualifications.lower() == "yes" and experience >= 5 and interview_performance.lower() == "yes":
    print("You are eligible for the job.")
elif qualifications.lower() == "yes" and experience >= 5:
    print("You are eligible for the job, but you need to perform well in the interview.")
elif qualifications.lower() == "yes" and interview_performance.lower() == "yes":
    print("You are eligible for the job, but you need to have enough experience.")
elif experience >= 5 and interview_performance.lower() == "yes":
    print("You are eligible for the job, but you need to have the required qualifications.")
else:
    print("You are not eligible for the job.")
#In this example, we take input from the user for their qualifications, years of experience, and interview performance. We then use a series of if, elif, and else statements along with logical operators to determine if the person is eligible for a job based on the provided criteria. The conditions check if the qualifications, experience, and interview performance meet certain thresholds for job eligibility, and the appropriate message is printed based on the conditions that are true.
#Example 11:
#In this example, we will use if statements and logical operators to determine if a person is eligible for a health insurance plan based on their age, pre-existing conditions, and lifestyle choices.
#We will use if, elif, else statements and logical operators like the and, or, not to check multiple conditions for health insurance eligibility.
#This example is more complex and involves multiple criteria for determining health insurance eligibility.
#This will include nested if statements, elif statements, else statements, and all logical operators like the and, or, not to create a comprehensive eligibility check for health insurance plans.
print("Health Insurance Eligibility Checker")

# 1. Inputs
age = int(input("Enter your age: "))
pre_existing = input("Pre-existing conditions (yes/no): ").lower()
lifestyle = input("Healthy lifestyle (yes/no): ").lower()
smoker = input("Smoker (yes/no): ").lower()
exercise = input("Exercise regularly (yes/no): ").lower()
income = int(input("Monthly income: "))
bmi = float(input("BMI: "))

print("\n1. Eligibility Check")

# 2. Eligibility Logic
if age < 18:
    print("Not eligible")
else:
    if age >= 18 and age < 30:
        if pre_existing == "no" and not (lifestyle == "no") and not (smoker == "yes"):
            if not (exercise == "no") and bmi < 25:
                print("Lowest premium")
            elif exercise == "no" or not (bmi < 25):
                print("Low premium")
        elif pre_existing == "no" and (not (lifestyle == "yes") or smoker == "yes"):
            print("Medium premium")
        elif not (pre_existing == "no") and lifestyle == "yes":
            print("Medium premium")
        else:
            print("High premium")

    elif age >= 30 and age < 50:
        if pre_existing == "no" and not (lifestyle == "no"):
            if not (smoker == "yes") and not (exercise == "no"):
                print("Moderate premium")
            else:
                print("Slightly high premium")
        elif not (pre_existing == "no"):
            if smoker == "yes" or not (bmi <= 30):
                print("High premium")
            else:
                print("Medium premium")
        else:
            print("High premium")

    else:
        if pre_existing == "no":
            if not (lifestyle == "no") and not (smoker == "yes"):
                print("High premium")
            else:
                print("Very high premium")
        elif not (pre_existing == "no"):
            if not (lifestyle == "yes" and smoker == "no"):
                print("Extremely high premium")
            else:
                print("Very high premium")

print("\n2. Financial Evaluation")

# 3. Income Check
if not (income >= 20000):
    print("Subsidy eligible")
elif not (income > 50000):
    print("Standard plan")
else:
    print("Premium plan")

print("\n3. Health Risk Analysis")

# 4. BMI Check
if not (bmi >= 18.5):
    print("Underweight risk")
elif not (bmi >= 25):
    print("Normal")
elif not (bmi >= 30):
    print("Overweight risk")
else:
    print("Obesity risk")

print("\nEnd")
#In this example, we take input from the user for their age, pre-existing conditions, lifestyle choices, smoking status, exercise habits, income, and BMI. We then use a series of if, elif, and else statements along with logical operators to determine the person's eligibility for a health insurance plan based on the provided criteria. The conditions check various factors such as age, pre-existing conditions, lifestyle choices, smoking status, exercise habits, income, and BMI to determine the appropriate health insurance plan and premium level for the individual.
#Example 12:
print("Job Hiring System")

age = int(input("Enter your age: "))
qualification = input("Qualification (graduate/postgraduate): ").lower()
experience = int(input("Years of experience: "))
skills = input("Do you have required skills? (yes/no): ").lower()
relocation = input("Willing to relocate? (yes/no): ").lower()
background_check = input("Background check clear? (yes/no): ").lower()

print("\n1. Hiring Decision")

if age < 18:
    print("Not eligible for job")
else:
    if age >= 18 and age < 30:
        if qualification == "graduate" and skills == "yes":
            if experience >= 2 and not (background_check == "no"):
                print("Selected for junior role")
            elif experience < 2 or relocation == "no":
                print("Selected for internship")
            else:
                print("On hold")
        elif not (skills == "yes"):
            print("Rejected due to lack of skills")
        else:
            print("On hold")

    elif age >= 30 and age < 50:
        if qualification == "postgraduate" and not (background_check == "no"):
            if experience >= 5 and skills == "yes":
                print("Selected for senior role")
            elif experience >= 3 or relocation == "yes":
                print("Selected for mid-level role")
            else:
                print("On hold")
        elif not (qualification == "postgraduate"):
            print("Rejected due to qualification")
        else:
            print("On hold")

    else:
        if not (background_check == "yes"):
            print("Rejected due to background check")
        else:
            if experience >= 10 and skills == "yes":
                print("Selected as consultant")
            elif not (experience >= 10) or relocation == "no":
                print("Selected for advisory role")
            else:
                print("On hold")

print("\n2. Experience Level")

if not (experience >= 2):
    print("Fresher")
elif not (experience >= 5):
    print("Intermediate")
elif not (experience >= 10):
    print("Experienced")
else:
    print("Expert")

print("\n3. Final Status")

if not (skills == "yes"):
    print("Skill improvement required")
elif not (background_check == "yes"):
    print("Verification pending")
else:
    print("Ready for onboarding")

print("\nEnd")
#In this example, we take input from the user for their age, qualification, years of experience, skills, willingness to relocate, and background check status. We then use a series of if, elif, and else statements along with logical operators to determine the person's eligibility for a job role based on the provided criteria. The conditions check various factors such as age, qualification, experience, skills, willingness to relocate, and background check status to determine the appropriate job role and hiring decision for the individual. The program also evaluates the experience level and final status of the candidate based on their skills and background check status.
#Example 13:
print("Smart Home Automation System")

time_of_day = input("Time of day (morning/afternoon/night): ").lower()
motion = input("Is motion detected? (yes/no): ").lower()
temperature = float(input("Enter room temperature: "))
light_level = input("Light level (low/medium/high): ").lower()
security_mode = input("Security mode (on/off): ").lower()
user_home = input("Is user at home? (yes/no): ").lower()

print("\n1. Lighting Control")

if motion == "yes" and not (light_level == "high"):
    if time_of_day == "night":
        print("Lights ON at full brightness")
    elif time_of_day == "evening" or light_level == "low":
        print("Lights ON at medium brightness")
    else:
        print("Lights ON at low brightness")
elif not (motion == "yes"):
    print("Lights OFF")
else:
    print("No change in lighting")

print("\n2. Temperature Control")

if temperature < 18:
    if not (user_home == "no"):
        print("Heating ON")
    else:
        print("Heating OFF (energy saving)")
elif temperature >= 18 and temperature <= 26:
    if not (motion == "no"):
        print("Maintain temperature")
    else:
        print("Eco mode active")
else:
    if user_home == "yes" and not (temperature < 30):
        print("Cooling ON at high level")
    elif not (user_home == "yes"):
        print("Cooling OFF (away mode)")
    else:
        print("Cooling ON at moderate level")

print("\n3. Security System")

if security_mode == "on":
    if not (user_home == "yes") and motion == "yes":
        print("Alert: Intrusion detected")
    elif motion == "no" or user_home == "yes":
        print("Security monitoring active")
    else:
        print("Standby mode")
else:
    if not (security_mode == "on"):
        print("Security system disabled")
    else:
        print("Unknown state")

print("\n4. Energy Optimization")

if not (motion == "yes") and not (user_home == "yes"):
    print("All systems in power saving mode")
elif motion == "yes" or user_home == "yes":
    print("Normal power usage")
else:
    print("Minimal activity detected")

print("\nEnd")
#In this example, we take input from the user for the time of day, motion detection, room temperature, light level, security mode, and whether the user is at home. We then use a series of if, elif, and else statements along with logical operators to control various aspects of a smart home automation system. The program manages lighting control based on motion and time of day, temperature control based on room temperature and user presence, security system monitoring based on security mode and motion detection, and energy optimization based on motion and user presence. The appropriate actions are printed based on the conditions that are true for each aspect of the smart home automation system.
#Example 14:
print("Personalized Fitness Plan Generator")

age = int(input("Enter your age: "))
fitness_goal = input("Fitness goal (weight_loss/muscle_gain/endurance): ").lower()
experience = input("Experience level (beginner/intermediate/advanced): ").lower()
medical_condition = input("Any medical condition? (yes/no): ").lower()
diet = input("Following a healthy diet? (yes/no): ").lower()
sleep = int(input("Hours of sleep per day: "))
time_available = int(input("Workout time available (minutes per day): "))

print("\n1. Plan Selection")

if age < 16:
    print("Light activity plan recommended")
else:
    if fitness_goal == "weight_loss":
        if not (medical_condition == "yes") and time_available >= 30:
            if experience == "beginner":
                print("Cardio + basic HIIT plan")
            elif experience == "intermediate" or sleep < 6:
                print("Moderate cardio + strength mix")
            else:
                print("Intense HIIT + strength training")
        elif medical_condition == "yes" or not (time_available >= 30):
            print("Low intensity fat loss plan")
        else:
            print("Custom plan required")

    elif fitness_goal == "muscle_gain":
        if diet == "yes" and not (medical_condition == "yes"):
            if experience == "beginner" and sleep >= 7:
                print("Basic strength training plan")
            elif experience == "intermediate" or not (sleep >= 7):
                print("Split training routine")
            else:
                print("Advanced hypertrophy program")
        elif not (diet == "yes"):
            print("Improve diet before starting muscle gain plan")
        else:
            print("Consult professional")

    else:
        if not (medical_condition == "yes"):
            if time_available >= 45 and sleep >= 7:
                print("Endurance training with cardio focus")
            elif time_available < 45 or not (sleep >= 7):
                print("Light endurance building plan")
            else:
                print("Balanced endurance program")
        else:
            print("Medical clearance required")

print("\n2. Recovery Evaluation")

if not (sleep >= 6):
    print("Poor recovery")
elif not (sleep >= 8):
    print("Average recovery")
else:
    print("Good recovery")

print("\n3. Consistency Level")

if not (time_available >= 20):
    print("Low consistency")
elif not (time_available >= 45):
    print("Moderate consistency")
else:
    print("High consistency")

print("\nEnd")
#In this example, we take input from the user for their age, fitness goal, experience level, medical condition, diet, sleep hours, and workout time available. We then use a series of if, elif, and else statements along with logical operators to generate a personalized fitness plan based on the provided criteria. The program selects an appropriate fitness plan based on the user's age, fitness goal, experience level, medical condition, diet, sleep hours, and workout time available. It also evaluates the user's recovery and consistency levels based on their sleep hours and workout time. The appropriate messages are printed based on the conditions that are true for each aspect of the personalized fitness plan generator.
#Example 15:
print("Startup Idea Evaluation System")

idea_uniqueness = int(input("Idea uniqueness (1-10): "))
market_demand = int(input("Market demand (1-10): "))
budget = int(input("Available budget: "))
team_size = int(input("Team size: "))
experience = input("Team experience (low/medium/high): ").lower()
competition = input("Competition level (low/medium/high): ").lower()
scalability = input("Is the idea scalable? (yes/no): ").lower()
risk_tolerance = input("Risk tolerance (low/medium/high): ").lower()

print("\n1. Feasibility Analysis")

if idea_uniqueness < 4 or not (market_demand >= 5):
    print("Low feasibility")
else:
    if idea_uniqueness >= 4 and idea_uniqueness < 7:
        if market_demand >= 5 and not (competition == "high"):
            if scalability == "yes" and not (budget < 50000):
                print("Moderate feasibility")
            elif scalability == "no" or budget < 50000:
                print("Limited feasibility")
            else:
                print("Conditional feasibility")
        elif competition == "high" and not (risk_tolerance == "high"):
            print("Risky idea")
        else:
            print("Needs improvement")

    elif idea_uniqueness >= 7:
        if market_demand >= 7 and scalability == "yes":
            if experience == "high" and team_size >= 3:
                print("High feasibility startup")
            elif experience == "medium" or team_size < 3:
                print("Promising but needs stronger team")
            else:
                print("Execution risk present")
        elif not (market_demand >= 7):
            print("Innovative but weak demand")
        else:
            print("Scalability concerns")

print("\n2. Financial Viability")

if not (budget >= 20000):
    print("Insufficient budget")
elif not (budget >= 100000):
    print("Moderate financial strength")
else:
    print("Strong financial backing")

print("\n3. Risk Assessment")

if risk_tolerance == "low":
    if competition == "high" or not (market_demand >= 7):
        print("High perceived risk")
    else:
        print("Manageable risk")
elif risk_tolerance == "medium":
    if competition == "high" and not (scalability == "yes"):
        print("Moderate to high risk")
    else:
        print("Balanced risk")
else:
    if scalability == "yes" and idea_uniqueness >= 7:
        print("High risk high reward")
    else:
        print("Aggressive but uncertain")

print("\n4. Team Strength")

if not (team_size >= 2):
    print("Weak team")
elif not (team_size >= 5):
    print("Average team")
else:
    print("Strong team")

print("\n5. Final Decision")

if idea_uniqueness >= 7 and market_demand >= 7 and scalability == "yes" and not (budget < 50000):
    print("Proceed with startup")
elif idea_uniqueness >= 5 and market_demand >= 5:
    print("Refine idea before launching")
else:
    print("Do not proceed")

print("\nEnd")
#In this example, we take input from the user for various factors related to a startup idea, such as idea uniqueness, market demand, budget, team size, experience, competition level, scalability, and risk tolerance. We then use a series of if, elif, and else statements along with logical operators to evaluate the feasibility, financial viability, risk assessment, team strength, and final decision for the startup idea based on the provided criteria. The program assesses different aspects of the startup idea and provides feedback on its potential success or areas that need improvement. The appropriate messages are printed based on the conditions that are true for each aspect of the startup idea evaluation system.
