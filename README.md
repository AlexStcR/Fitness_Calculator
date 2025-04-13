# Fitness Calculator: TDEE, Protein & BMI Calculator 🏋️‍♂️

A Python-based calculator that estimates your **Total Daily Energy Expenditure (TDEE)**, optimal **protein intake**, and **Body Mass Index (BMI)** based on your goals (muscle gain, weight loss, or maintenance).

## 🔧 Features
- **TDEE Calculation** using Harris-Benedict Equation (BMR + activity level)
- **Protein Recommendation** based on fitness goals
- **BMI Calculation** with standard weight categories
- **Goal-Based Calorie Prescription** (surplus/deficit/maintenance)
- **Error Handling** for invalid inputs

## 🚀 How to Use

### Prerequisites
- Python 3.x installed

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Fitness_Calculator.git
   ```
   
2.Navigate to the project directory:
   ```bash
   cd Fitness_Calculator
   ```

## Running the Calculator
Execute the Python script:
```bash
python Fitness_Calculator.py
```

## Step-by-Step Usage Guide
Enter Personal Details:

- Gender (male/female)

- Age (years)

- Height (cm)

- Weight (kg)

## Select Activity Level:

- Sedentary (little or no exercise)

- Lightly active (light exercise 1-3 days/week)

- Moderately active (moderate exercise 3-5 days/week)

- Very active (hard exercise 6-7 days/week)

- Extra active (very hard exercise & physical job)

## Choose Your Goal:

- Muscle gain

- Weight loss

- Maintenance

- View Your Results:

- BMI and weight category

- BMR (Basal Metabolic Rate)

- TDEE (Total Daily Energy Expenditure)

- Recommended daily calorie intake

- Recommended protein intake

## 🔬 Research Deep Dive
### Estimating Your Engine: Total Daily Energy Expenditure (TDEE)
- Uses Harris-Benedict Equation (gender-specific)

- Factors in Activity Level Multipliers  to estimate TDEE

## Fueling Your Goals: Protein Levels
- Muscle Gain/Weight Loss: ~2.2g protein/kg body weight

- Maintenance: ~1.8g protein/kg body weight

## Understanding Body Composition: BMI
- Calculated as weight (kg) / (height (m))^2

- Standard BMI ranges included for weight classification

## Calorie Prescription
- Muscle Gain: TDEE + ~300 calories

- Weight Loss: TDEE - ~500 calories

- Maintenance: TDEE

## 🛡️ Error Handling
The calculator includes robust error handling:

- Non-numeric entries caught with ValueError

- Ensures positive values for age, height, and weight

- Validates gender and activity level selections

## 📊 Example Output
```python
=== 🏋️‍♂️ ULTIMATE FITNESS CALCULATOR🏋️‍♂️ ===
📏 STEP 1: Body Composition Analysis
🎂Age:  30
🚻 Gender (Male/Female):  female
📏 Height (cm):  160
⚖️ Weight (kg):  50
📐 Waist circumference (cm):  14
🏋️‍♂️ Do you engage in regular strength training? (Y/N):  y

===== 🧠 BODY COMPOSITION🧠 =====
📌 BMI: 19.5 → 💪 Muscular (Low Fat)
📐 Waist-to-Height Ratio: 0.09 (Healthy <0.5)
⚠️ Health Note: ✅ Healthy (High muscle mass)

🔥 STEP 2: Basic Nutrition Planning
  [1] Sedentary (little or no exercise)
  [2] Lightly Active (light exercise/sports 1-3 days/week)
  [3] Moderately Active (moderate exercise/sports 3-5 days/week)
  [4] Very Active (hard exercise/sports 6-7 days a week)
  [5] Extra Active (very hard exercise/sports & a physical job)
Select activity level (1-5):  4

🎯 Goal (muscle gain/weight loss/maintain):  weight loss

===== 🍽️ NUTRITION PLAN =====
⚡ Estimated Total Daily Energy Expenditure (TDEE): 2223 kcal
🎯 Daily Calorie Goal: 1723 kcal

📊 Macronutrients:
  🥩 Protein: 110.0 grams (26%)
  🍞 Carbohydrates: 150.8 grams (35%)
  🥑Good Fats: 57.4 grams (30%)

💡 EXPERT TIPS:
  - Ensure adequate protein intake (around 1.6-2.2 grams per kilogram of body weight) to support muscle maintenance and growth.
  - Adjust your calorie intake based on your training intensity and performance goals.
  - Listen to your body and ensure sufficient rest and recovery.
  - Consider consulting with a sports nutritionist for optimized fueling strategies.
```
