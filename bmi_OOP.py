#https://www.geeksforgeeks.org/python-oops-concepts/
#https://pythonguides.com/object-oriented-programming/

class Person:
    #Profile information, collecting all information necessary to run the calculations

    def __init__(self, age, gender, height_cm, weight_kg, waist_cm, is_athletic):
        #
        '''Initializes a Person object.

        Args:
            age (int): The age of the person in years.
            gender (str): The gender of the person ('male' or 'female').
            height_cm (float): The height of the person in centimeters.
            weight_kg (float): The weight of the person in kilograms
            '''
        self.age=age
        self.gender=gender.lower()
        self.height_cm=height_cm
        self.weight_kg=weight_kg
        self.waist_cm=waist_cm
        self.is_athletic=is_athletic

    def calculate_bmi(self):
        height_m = self.height_cm / 100
        return self.weight_kg / (height_m ** 2)

    def get_waist_to_height_ratio(self):
        """Calculates the waist-to-height ratio."""
        return self.waist_cm / self.height_cm

    def assess_fitness(self):
        bmi= self.calculate_bmi()
        waist_to_height = self.get_waist_to_height_ratio()

        if self.is_athletic == 'y':
            if waist_to_height < 0.5:

                return ("💪 Muscular (Low Fat)", "✅ Healthy (High muscle mass)")
            else:
                return ("⚠️ Muscular but High Waist", "❗ Possible visceral fat (Check diet)")
        else:
            if bmi < 16:
                return ("🍗 Severely Underweight", "🆘 High risk of malnutrition")
            elif 16 <= bmi < 18.5:
                return ("😟 Underweight", "⚠️ Moderate risk of deficiencies")
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
                    return ("🚨 Obese", "💀 High health risk")
class NutritionPlan:

    activity_multipliers = {'sedentary': 1.2,
                              'light': 1.375,
                              'moderate': 1.55,
                              'active': 1.725,
                              'very active': 1.9,
                              'extra active': 1.9} # Added 'extra active'

    def __init__(self, person, activity_level, goal):
        self.person = person
        self.activity_level = activity_level.lower()
        self.goal = goal.lower()

    def calculate_bmr(self):
        #For men: BMR = 66.5 + (13.75 × weight in kg) + (5.003 × height in cm) - (6.75 × age)
        #For women: BMR = 655.1 + (9.563 × weight in kg) + (1.850 × height in cm) - (4.676 × age)

        if self.person.gender == 'male':
            return 66.5 + (13.75 * self.person.weight_kg) + (5.003 * self.person.height_cm) - (6.75 * self.person.age)
        else:
            return 655.1 + (9.563 * self.person.weight_kg) + (1.850 * self.person.height_cm) - (4.676 * self.person.age)
    def calculate_calories(self):
        bmr = self.calculate_bmr()
        activity_multiplier = self.activity_multipliers.get(self.activity_level)
        tdee = bmr * activity_multiplier

        if activity_multiplier is None:
            raise ValueError("Invalid activity level provided.")
        if self.goal == 'weight loss':
            calories = tdee - 500
        elif self.goal == 'muscle gain':
            calories = tdee + 300
        else:
            calories = tdee

        return calories, tdee

    def calculate_macros(self):

        calories, _ = self.calculate_calories()
        weight_kg = self.person.weight_kg

        if self.goal == 'muscle gain':
            protein = 2.2 * weight_kg
            carbs = (calories * 0.45) / 4
            fats = (calories * 0.25) / 9
        elif self.goal == 'weight loss':
            protein = 2.2 * weight_kg
            carbs = (calories * 0.35) / 4
            fats = (calories * 0.30) / 9
        else:  # Maintenance
            protein = 1.8 * weight_kg
            carbs = (calories * 0.40) / 4
            fats = (calories * 0.25) / 9
        return protein, carbs, fats


class FitnessCalculatorApp:

    def get_valid_input(self, prompt, data_type, validation_func=None, error_message=None):

        while True:
            try:
                value = data_type(input(prompt))
                if validation_func is None or validation_func(value):
                    return value
                print(error_message if error_message else "Invalid input.")
            except ValueError:
                print(f"Please enter a valid {data_type.__name__}.")

    def get_valid_choice(self, prompt, choices):

        while True:
            choice = input(prompt).strip().lower()
            if choice in choices:
                return choice
            print(f"Please enter one of: {', '.join(choices)}")

    def get_valid_activity_level(self):

        print("  [1] Sedentary (little or no exercise)")
        print("  [2] Lightly Active (light exercise/sports 1-3 days/week)")
        print("  [3] Moderately Active (moderate exercise/sports 3-5 days/week)")
        print("  [4] Very Active (hard exercise/sports 6-7 days a week)")
        print("  [5] Extra Active (very hard exercise/sports & a physical job)")
        while True:
            try:
                activity_choice = int(input("Select activity level (1-5): "))
                if 1 <= activity_choice <= 5:
                    if activity_choice == 1:
                        return 'sedentary'
                    elif activity_choice == 2:
                        return 'light'
                    elif activity_choice == 3:
                        return 'moderate'
                    elif activity_choice == 4:
                        return 'active'
                    elif activity_choice == 5:
                        return 'extra active'
                print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number between 1 and 5.")

    def main(self):

        print("\n=== 🏋️‍♂️ ULTIMATE FITNESS CALCULATOR🏋️‍♂️ ===")
        print("📏 STEP 1: Body Composition Analysis")

        age = self.get_valid_input("🎂 Age: ", int, lambda x: x > 0, "Please enter a valid age (positive number).")
        gender = self.get_valid_choice("🚻 Gender (Male/Female): ", ['male', 'female'])
        height = self.get_valid_input("📏 Height (cm): ", float, lambda x: x > 0, "Please enter a valid height (positive number).")
        weight = self.get_valid_input("⚖️ Weight (kg): ", float, lambda x: x > 0, "Please enter a valid weight (positive number).")
        waist = self.get_valid_input("📐 Waist circumference (cm): ", float, lambda x: x > 0, "Please enter a valid waist measurement (positive number).")
        is_athletic = self.get_valid_choice("🏋️‍♂️ Do you engage in regular strength training? (Y/N): ", ['y', 'n'])

        person = Person(age, gender, height, weight, waist, is_athletic)
        bmi = person.calculate_bmi()
        waist_ratio = person.get_waist_to_height_ratio()
        category, risk = person.assess_fitness()

        print("\n===== 🧠 BODY COMPOSITION🧠 =====")
        print(f"📌 BMI: {bmi:.1f} → {category}")
        print(f"📐 Waist-to-Height Ratio: {waist_ratio:.2f} (Healthy <0.5)")
        print(f"⚠️ Health Note: {risk}")

        print("\n🔥 STEP 2: Basic Nutrition Planning")
        activity = self.get_valid_activity_level()
        goal = self.get_valid_choice("\n🎯 Goal (muscle gain/weight loss/maintain): ", ['muscle gain', 'weight loss', 'maintain'])

        nutrition_plan = NutritionPlan(person, activity, goal)
        try:
            calories, tdee = nutrition_plan.calculate_calories()
            protein, carbs, fats = nutrition_plan.calculate_macros()

            print("\n===== 🍽️ NUTRITION PLAN =====")
            print(f"⚡ Estimated Total Daily Energy Expenditure (TDEE): {tdee:.0f} kcal")
            print(f"🎯 Daily Calorie Goal: {calories:.0f} kcal")
            print("\n📊 Macronutrients:")
            print(f"  🥩 Protein: {protein:.1f} grams ({protein * 4 / calories:.0%})")
            print(f"  🍞 Carbohydrates: {carbs:.1f} grams ({carbs * 4 / calories:.0%})")
            print(f"  🥑 Good Fats: {fats:.1f} grams ({fats * 9 / calories:.0%})")

            print("\n💡 EXPERT TIPS:")
            if "Underweight" in category:
                print("  - Focus on calorie-dense foods such as nuts, seeds, avocados, and olive oil.")
                print("  - Consider eating more frequently throughout the day.")
                print("  - Engage in regular strength training (around 3 times per week) to build muscle mass.")
                print("  - It's advisable to consult with a healthcare professional or a registered dietitian for personalized guidance.")
            elif "Overweight" in category or "Obese" in category:
                print("  - Prioritize whole, unprocessed foods and focus on portion control.")
                print("  - Aim for a balanced exercise routine including both cardiovascular exercises and strength training.")
                print("  - Pay attention to your waist-to-height ratio as an indicator of abdominal fat.")
                print("  - Consulting with a healthcare professional or a registered dietitian can provide tailored strategies for healthy weight management.")
            elif "Muscular" in category:
                print("  - Ensure adequate protein intake (around 1.6-2.2 grams per kilogram of body weight) to support muscle maintenance and growth.")
                print("  - Adjust your calorie intake based on your training intensity and performance goals.")
                print("  - Listen to your body and ensure sufficient rest and recovery.")
                print("  - Consider consulting with a sports nutritionist for optimized fueling strategies.")
            elif "Normal" in category:
                print("  - Maintain a balanced diet with plenty of fruits, vegetables, and whole grains.")
                print("  - Continue with regular physical activity to support overall health and well-being.")
                print("  - Monitor your BMI and waist-to-height ratio periodically to stay within healthy ranges.")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = FitnessCalculatorApp()
    app.main()







