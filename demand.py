"""This file is for building functions to track elasticity , and demand"""
import math

# a.) compute elasticity function


def compute_elasticity(price1: float, price2: float, quantity1: float,
                       quantity2: float) -> float:
    """this function computes the elasticity given price and quantities"""
    elasticity = math.log(quantity1 / quantity2) / math.log(price1 / price2)
    return elasticity


# b.) elasticity classifier function


def check_elasticity(e: float) -> str:
    """this funciton classifies elasticites as either elastic
    inelastic or unit elastic"""
    if e > 1:
        category = "elastic"
    elif e == 1:
        category = "unit elastic"
    else:
        category = "inelastic"
    return category


# c.) demand function(solved as q2 = q1 * (p2/p1)^e


def compute_demand(sales: float, initprice: float, newprice: float,
                   e: float) -> float:
    """this function computes new quantity demanded"""
    newdemand = sales * (initprice / newprice) ** e
    return newdemand


# d.) combining elasticity and Demand into main function using input function

def main():
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
        newrange = list(input("Additional price points?(input list)"))
        demand_dict = {initprice: sales}
        for i in newrange:
            demand_dict[float(i)] = compute_demand(sales, initprice,
                                                   newelasticity, float(i))
        output = demand_dict
    else:
        output = "not valid input"
    return output


main()
