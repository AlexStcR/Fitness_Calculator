#https://www.nhs.uk/health-assessment-tools/calculate-your-body-mass-index/calculate-bmi-for-adults
#https://www.strongerbyscience.com/protein-science/
'''The BMI is calculated by dividing an adult's weight in kilograms by their height in metres squared.

For example, if you weigh 70kg (around 11 stone) and are 1.70m (around 5 foot 7 inches)
tall, you work out your BMI by:

squaring your height in metres: 1.70 x 1.70 = 2.89
dividing your weight in kilograms: 70 ÷ 2.89 = 24.22
Your result will be displayed to one decimal place, for example, 24.2.'''
#https://emojipedia.org/ (for the emojis)
'''Sedentary (little or no exercise): TDEE = BMR × 1.2
Lightly active (light exercise/sports 1-3 days/week): TDEE = BMR × 1.375
Moderately active (moderate exercise/sports 3-5 days/week): TDEE = BMR × 1.55
Very active (hard exercise/sports 6-7 days a week): TDEE = BMR × 1.725
Extra active (very hard exercise/sports & a physical job): TDEE = BMR × 1.9.
'''
#Functions
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def get_waist_to_height_ratio(waist_cm, height_cm):
    ratio = waist_cm / height_cm
    return ratio

def assess_fitness(bmi, waist_to_height, is_athletic):
    if is_athletic.lower() == 'y':
        if waist_to_height < 0.5:
            #returning 2 strings
            return ("💪 Muscular (Low Fat)", "✅ Healthy (High muscle mass)")
        else:
            return ("⚠️ Muscular but High Waist", "❗ Possible visceral fat (Check diet)")
    else:
        if bmi < 16:
            return ("🍗 Severely Underweight", "🆘 High risk of malnutrition")
        elif 16 <= bmi < 18.5:
            return( "😟 Underweight", "⚠️ Moderate risk of deficiencies")
        elif 18.5 <= bmi < 25:
            return ("✅ Normal", "👍 Healthy range")
        elif 25 <= bmi < 30:
            if waist_to_height < 0.5:
                return ("⚠️ Overweight (Low Waist Fat)", "🔍 May need body fat analysis")
            else:
                return ("⚠️ Overweight", "🆘 Increased health risks")
        else:
            if waist_to_height < 0.5:
                return ("🔴 High BMI but Low Waist", "❓ Could be muscle or fat (DEXA scan recommended)")
            else:
                return( "🚨 Obese", "💀 High health risk")

def calculate_calories(age, gender, height_cm, weight_kg, activity_level, goal):
    # Harris-Benedict Equation
    if gender.lower() == 'male':
        #For men: BMR = 66.5 + (13.75 × weight in kg) + (5.003 × height in cm) - (6.75 × age)
        bmr = 66.5 + (13.75* weight_kg) + (5.003* height_cm) - (6.75* age)
    else:
        #For women: BMR = 655.1 + (9.563 × weight in kg) + (1.850 × height in cm) - (4.676 × age)
        bmr = 655.1 + (9.563 * weight_kg) + (1.850 * height_cm) - (4.676* age)



    activity_multipliers = {'sedentary': 1.2,
                            'light': 1.375,
                            'moderate': 1.55,
                            'active': 1.725,
                            'very active': 1.9}

    tdee = bmr * activity_multipliers.get(activity_level.lower())
    #TDEE = BMR x Activity Multiplier

    if goal == 'weight loss':
        calories = tdee - 500  # deficit for weight loss
    elif goal == 'muscle gain':
        calories = tdee + 300   # surplus for muscle gain
    else:
        calories = tdee         # maintain

    return calories, tdee  # Ensure this line exists!

def calculate_macros(calories, goal, weight_kg):
    if goal == 'muscle gain':
        protein = 2.2 * weight_kg  # 2.2g/kg for muscle growth
        carbs = (calories * 0.45) / 4
        fats = (calories * 0.25) / 9
    elif goal == 'weight loss':
        protein = 2.2 * weight_kg  # High protein to preserve muscle
        carbs = (calories * 0.35) / 4
        fats = (calories * 0.30) / 9
    else:  # Maintenance
        protein = 1.8 * weight_kg
        carbs = (calories * 0.40) / 4
        fats = (calories * 0.25) / 9

    return protein, carbs, fats


# Main Program


def main():
    print("\n=== 🏋️‍♂️ ULTIMATE FITNESS CALCULATOR🏋️‍♂️ ===")
    print("📏 STEP 1: Body Composition Analysis")

    # Get age with validation
    while True:
        try:
            age = int(input("🎂Age: "))
            if age > 0:
                break
            print("Please enter a valid age (positive number).")
        except ValueError:
            print("Please enter a valid number for age.")

    # Get gender with validation
    while True:
        gender = input("🚻 Gender (Male/Female): ").strip().lower()
        if gender in ['male', 'female']:
            break
        print("Please enter either 'Male' or 'Female'.")

    # Get height with validation
    while True:
        try:
            height = float(input("📏 Height (cm): "))
            if height > 0:
                break
            print("Please enter a valid height (positive number).")
        except ValueError:
            print("Please enter a valid number for height.")

    # Get weight with validation
    while True:
        try:
            weight = float(input("⚖️ Weight (kg): "))
            if weight > 0:
                break
            print("Please enter a valid weight (positive number).")
        except ValueError:
            print("Please enter a valid number for weight.")

    # Get waist circumference with validation
    while True:
        try:
            waist = float(input("📐 Waist circumference (cm): "))
            if waist > 0:
                break
            print("Please enter a valid waist measurement (positive number).")
        except ValueError:
            print("Please enter a valid number for waist circumference.")

    # Get athletic status with validation
    while True:
        is_athletic = input("🏋️‍♂️ Do you engage in regular strength training? (Y/N): ").strip().lower()
        if is_athletic in ['y', 'n']:
            break
        print("Please enter either 'Y' or 'N'.")

    # Body Composition Results
    bmi = calculate_bmi(height, weight)
    waist_ratio = get_waist_to_height_ratio(waist, height)
    category, risk = assess_fitness(bmi, waist_ratio, is_athletic)

    print("\n===== 🧠 BODY COMPOSITION🧠 =====")
    print(f"📌 BMI: {bmi:.1f} → {category}")
    print(f"📐 Waist-to-Height Ratio: {waist_ratio:.2f} (Healthy <0.5)")
    print(f"⚠️ Health Note: {risk}")

    # Nutrition Calculator
    print("\n🔥 STEP 2: Basic Nutrition Planning")
    print("  [1] Sedentary (little or no exercise)")
    print("  [2] Lightly Active (light exercise/sports 1-3 days/week)")
    print("  [3] Moderately Active (moderate exercise/sports 3-5 days/week)")
    print("  [4] Very Active (hard exercise/sports 6-7 days a week)")
    print("  [5] Extra Active (very hard exercise/sports & a physical job)")

    # Get activity level with validation
    while True:
        try:
            activity_choice = int(input("Select activity level (1-5): "))
            if 1 <= activity_choice <= 5:
                if activity_choice == 1:
                    activity='sedentary'
                elif activity_choice == 2:
                    activity='light'
                elif activity_choice == 3:
                    activity='moderate'
                elif activity_choice == 4:
                    activity='active'
                elif activity_choice == 5:
                    activity='extra active'

                break
            print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number between 1 and 5.")

    # Get goal with validation
    while True:
        goal = input("\n🎯 Goal (muscle gain/weight loss/maintain): ").lower().strip()
        if goal in ['muscle gain', 'weight loss', 'maintain']:
            break
        print("Please enter one of: 'muscle gain', 'weight loss', or 'maintain'")

    calories, tdee = calculate_calories(age, gender, height, weight, activity, goal)
    protein, carbs, fats = calculate_macros(calories, goal, weight)

    print("\n===== 🍽️ NUTRITION PLAN =====")
    print(f"⚡ Estimated Total Daily Energy Expenditure (TDEE): {tdee:.0f} kcal")
    print(f"🎯 Daily Calorie Goal: {calories:.0f} kcal")
    print("\n📊 Macronutrients:")
    print(f"  🥩 Protein: {protein:.1f} grams ({protein * 4 / calories:.0%})")
    print(f"  🍞 Carbohydrates: {carbs:.1f} grams ({carbs * 4 / calories:.0%})")
    print(f"  🥑Good Fats: {fats:.1f} grams ({fats * 9 / calories:.0%})")

    # Goal-Specific Tips
    print("\n💡 EXPERT TIPS:")
    if "Underweight" in category:
        print("  - Focus on calorie-dense foods such as nuts, seeds, avocados, and olive oil.")
        print("  - Consider eating more frequently throughout the day.")
        print("  - Engage in regular strength training (around 3 times per week) to build muscle mass.")
        print("  - It's advisable to consult with a healthcare professional or a registered dietitian for personalized guidance.")
    elif "Overweight" in category or "Obese" in category:
        print("  - Prioritize whole, unprocessed foods and focus on portion control.")
        print("  - Aim for a balanced exercise routine including both cardiovascular exercises and strength training.")
        print("  - Pay attention to your waist-to-height ratio as an indicator of abdominal fat.")
        print("  - Consulting with a healthcare professional or a registered dietitian can provide tailored strategies for healthy weight management.")
    elif "Muscular" in category:
        print("  - Ensure adequate protein intake (around 1.6-2.2 grams per kilogram of body weight) to support muscle maintenance and growth.")
        print("  - Adjust your calorie intake based on your training intensity and performance goals.")
        print("  - Listen to your body and ensure sufficient rest and recovery.")
        print("  - Consider consulting with a sports nutritionist for optimized fueling strategies.")
    elif "Normal" in category:
        print("  - Maintain a balanced diet with plenty of fruits, vegetables, and whole grains.")
        print("  - Continue with regular physical activity to support overall health and well-being.")
        print("  - Monitor your BMI and waist-to-height ratio periodically to stay within healthy ranges.")

if __name__ == "__main__":
    main()
