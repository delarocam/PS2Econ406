"""This file is for building functions to track elasticity,
   and quanity demanded"""
import math

# a.) compute elasticity function


def compute_elasticity(price1: float, price2: float, quantity1: float,
                       quantity2: float) -> float:
    """this function computes the elasticity given price and quantities"""
    elasticity = math.log(quantity1 / quantity2) / math.log(price1 / price2)
    print(elasticity)
    return elasticity

# test, uncomment to run function
# compute_elasticity(10, 12, 10, 8)

# b.) elasticity classifier function


def check_elasticity(elasticity: float) -> str:
    """this funciton classifies elasticites as either elastic
    inelastic or unit elastic"""
    if elasticity > 1:
        category = "elastic"
    elif elasticity == 1:
        category = "unit elastic"
    else:
        category = "inelastic"
    print(category)
    return category

# test, uncomment to run function
# check_elasticity(1.2)
# check_elasticity(0.5)
# check_elasticity(1)
# c.) demand function(solved as q2 = q1 * (p2/p1)^e


def compute_demand(sales: float, initprice: float, newprice: float,
                   elasticity: float) -> float:
    """this function computes new quantity demanded"""
    newdemand = sales * (initprice / newprice) ** elasticity
    print(newdemand)
    return newdemand

# test, uncomment to run function
# compute_demand(10, 10, 12, 1.2)
# d.) combining elasticity and Demand into main function using input function


def main():
    """This function is a universal function that will either compute
    Elasticity or Demand depending on user inputs"""
    choice = input("Would you like to Calculate Elasticity or Demand?")
    if choice == "Elasticity":
        oldprice = float(input("Old price?"))
        newprice = float(input("New price?"))
        oldquant = float(input("Old quantity?"))
        newquant = float(input("New quantity?"))
        elasticity = compute_elasticity(oldprice, newprice, oldquant, newquant)
        classification = check_elasticity(elasticity)
        output = print("e: " + str(elasticity) + "category: " +
                       str(classification))
    elif choice == "Demand":
        sales = float(input("Sales?"))
        initprice = float(input("Initial price?"))
        newelasticity = float(input("Elasticity?"))
        newrange = input("Additional price points?" +
                         "(input list of numbers separated by a white space" +
                         " between each one)")
        newrange = newrange.split()
        demand_dict = {initprice: sales}
        for i in newrange:
            i = float(i)
            demand_dict[i] = compute_demand(sales, initprice,
                                            i, newelasticity)
        output = demand_dict
    else:
        output = "not valid input"
        print(output)
    return output

# test, uncomment to run function
# main()
