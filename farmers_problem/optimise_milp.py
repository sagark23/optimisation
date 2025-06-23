from pulp import *

def solve_extended_farming_problem():
    # Crop data
    crops = ["potato", "carrot", "lettuce", "tomato"]

    profit = {
        "potato": 1.4, "carrot": 1.6, "lettuce": 1.5, "tomato": 1.9
    }
    setup_cost = {
        "potato": 400, "carrot": 800, "lettuce": 600, "tomato": 700
    }
    fertilizer_use = {
        "potato": 1, "carrot": 1, "lettuce": 0.5, "tomato": 1.2
    }
    labour_use = {
        "potato": 0.5, "carrot": 0.8, "lettuce": 1.2, "tomato": 1.5
    }
    land_use = {
        "potato": 1.0, "carrot": 1.2, "lettuce": 0.8, "tomato": 1.5
    }
    equipment_required = {
        "potato": 0, "carrot": 0, "lettuce": 1, "tomato": 1
    }
    crop_seed_limits = {
        "potato": 3000, "carrot": 4000, "lettuce": 2000, "tomato": 1500
    }

    # New resource limits
    fertilizer_available = 6000
    labour_available = 5000
    land_available = 5500
    equipment_available = 2

    # Variables
    crop_amount = LpVariable.dicts("crop_amount", crops, 0)
    is_crop_planted = LpVariable.dicts("is_crop_planted", crops, cat=LpBinary)

    # Problem
    prob = LpProblem("Extended_Farming_Knapsack", LpMaximize)

    # Objective
    prob += (
        lpSum([
            profit[crop] * crop_amount[crop] - setup_cost[crop] * is_crop_planted[crop]
            for crop in crops
        ])
    ), "Total_Net_Profit"

    # Constraints
    prob += lpSum([fertilizer_use[crop] * crop_amount[crop] for crop in crops]) <= fertilizer_available, "Fertilizer_Limit"
    prob += lpSum([labour_use[crop] * crop_amount[crop] for crop in crops]) <= labour_available, "Labour_Limit"
    prob += lpSum([land_use[crop] * crop_amount[crop] for crop in crops]) <= land_available, "Land_Limit"
    prob += lpSum([equipment_required[crop] * is_crop_planted[crop] for crop in crops]) <= equipment_available, "Equipment_Limit"

    for crop in crops:
        prob += crop_amount[crop] <= crop_seed_limits[crop] * is_crop_planted[crop], f"SeedLimit_{crop}"

    # Solve
    prob.solve()

    # Results
    print("\n📊 Extended MILP Results:")
    print(f"Status: {LpStatus[prob.status]}")
    print(f"Net Profit: £{value(prob.objective):.2f}")
    for crop in crops:
        if value(is_crop_planted[crop]) > 0.5:
            print(f"- Plant {value(crop_amount[crop]):.2f} kg of {crop} ✅")
        else:
            print(f"- Do not plant {crop} ❌")

if __name__ == "__main__":
    solve_extended_farming_problem()

