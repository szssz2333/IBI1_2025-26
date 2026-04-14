class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def calculate_daily_nutrition(food_list):
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0
    
    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat
    
    print(f"Total calories: {total_calories} kcal")
    print(f"Total protein: {total_protein} g")
    print(f"Total carbs: {total_carbs} g")
    print(f"Total fat: {total_fat} g")
    
    if total_calories > 2500:
        print("Warning: Calories exceed 2500 kcal!")
    if total_fat > 90:
        print("Warning: Fat exceeds 90 g!")

#example
apple = food_item("Apple", 60, 0.3, 15, 0.5)
banana = food_item("Banana", 105, 1.1, 27, 0.4)
chicken_breast = food_item("Chicken Breast", 165, 31, 0, 3.6)
rice = food_item("Rice", 206, 4.3, 45, 0.3)
broccoli = food_item("Broccoli", 55, 2.8, 11, 0.4)

daily_foods = [apple, banana, chicken_breast, rice, broccoli]
    

print("Daily Nutrition Summary:")
calculate_daily_nutrition(daily_foods)
    
    
print("\nTesting over-limit case:")
pizza = food_item("Pizza", 3000, 50, 100, 100)
over_limit_foods = [pizza]
calculate_daily_nutrition(over_limit_foods)
