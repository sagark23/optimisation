from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

def solve_farming_problem():
    # Define crops and their parameters
    profit = {
        "potato": 1.2,
        "carrot": 1.7
    }
    crop_seed_limits = {
        "potato": 3000,
        "carrot": 4000
    }
    fertilizer_available = 5000

    # Variables
    potato = LpVariable("potato", 0)
    carrot = LpVariable("carrot", 0)

    # Problem
    prob = LpProblem("Farmers_Optimization", LpMaximize)

    # Objective
    prob += profit["potato"] * potato + profit["carrot"] * carrot, "Total_Profit"

    # Constraints
    prob += potato <= crop_seed_limits["potato"], "Potato_Seeds_Limit"
    prob += carrot <= crop_seed_limits["carrot"], "Carrot_Seeds_Limit"
    prob += potato + carrot <= fertilizer_available, "Fertilizer_Limit"

    # Solve using default solver
    prob.solve()

    # Results
    print("\nOptimization Results:")
    print(f"Status: {LpStatus[prob.status]}")
    print("\nOptimal Planting Plan:")
    print(f"Potato seeds to plant: {value(potato):.2f} kgs")
    print(f"Carrot seeds to plant: {value(carrot):.2f} kgs")
    print(f"Maximum profit: £{value(prob.objective):.2f}")


if __name__ == "__main__":
    solve_farming_problem()
