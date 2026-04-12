class FoodItem:
    
    def __init__(self, name, calories, protein, carbs, fat):
        
        self.name = name
        self.calories = float(calories)
        self.protein = float(protein)
        self.carbs = float(carbs)
        self.fat = float(fat)

def calculate_daily_nutrition(food_list):
    total_nutrition = {
        'total_calories': 0.0,
        'total_protein': 0.0,
        'total_carbs': 0.0,
        'total_fat': 0.0}
    for food in food_list:
        if not isinstance(food, FoodItem):
            raise TypeError("Error: All items in food_list must be instances of FoodItem!")
        total_nutrition['total_calories'] += food.calories
        total_nutrition['total_protein'] += food.protein
        total_nutrition['total_carbs'] += food.carbs
        total_nutrition['total_fat'] += food.fat

    # print the total nutrition summary
    print(f"total calories:{total_nutrition['total_calories']:.1f} kal")
    print(f"total protein:{total_nutrition['total_protein']:.1f} gram")
    print(f"total carbs:{total_nutrition['total_carbs']:.1f} gram")
    print(f"total fat:{total_nutrition['total_fat']:.1f} gram")
   
    # detect and warn about excessive intake 
    if total_nutrition['total_calories'] > 2500:
        print(f"⚠️ warning: ({total_nutrition['total_calories']:.1f}>2500)!")
    if total_nutrition['total_fat'] > 90:
        print(f"⚠️ warning:fat intake excessive ({total_nutrition['total_fat']:.1f}>90)!")

    return total_nutrition

if __name__ == '__main__':
    print("Test the Nutrition Tracker's Function")

    # example1:simple valid food list with typical items, testing normal nutrition calculation
    print("【Example 1: Normal Nutrition Intake】")
    apple = FoodItem("apple", 60, 0.3, 15, 0.5) 
    egg = FoodItem("egg", 155, 13, 0.5, 10)
    rice = FoodItem("rice", 130, 2.6, 28, 0.3)
    normal_food_list = [apple, egg, rice]
    try:
        calculate_daily_nutrition(normal_food_list)
    except (TypeError, ValueError) as e:
        print(e)
    # example2:food list with excessive calories and fat, testing warning system 
    print("【Example 2: Excessive Nutrition Intake】")
    burger = FoodItem("burger", 560, 25, 40, 30)
    fries = FoodItem("fries", 320, 3, 40, 18)
    steak = FoodItem("steak(200g)", 500, 40, 0, 35)
    cake = FoodItem("cake", 400, 4, 60, 18)
    excess_food_list = [burger, fries, steak, cake, apple, egg, rice]
    try:
        calculate_daily_nutrition(excess_food_list)
    except (TypeError, ValueError) as e:
        print(e)
    # example3:invalid food list containing a non-FoodItem object, testing error handling
    print("【Example 3: Invalid Food List】")
    invalid_food_list = [apple, "not a food item", rice]
    try:
        calculate_daily_nutrition(invalid_food_list)
    except (TypeError, ValueError) as e:
        print(e)    