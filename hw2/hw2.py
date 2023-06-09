"""
CMSC 14100, Summer 2023
Homework #2

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.

"""
def polynomial(a,b,c,x):
    """
    compute ax^2 + bx + c for given values

    Inputs:
        a (float): coefficient
        b (float): coefficient
        c (float): coefficient
        x (float): a number

    Returns: ax^2+bx+c
    """
    ### EXERCISE 1 -- YOUR CODE GOES HERE
    # Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result

def not_congruent_mod_n(a, b, n):
    """
    Check if a and b are not congruent mod n

    Inputs:
        a (int): a value
        b (int): another value
        n (int): the modulus to use

    Returns: False if a and b are congruent mod n, and True otherwise.
    """

    ### EXERCISE 2 -- YOUR CODE GOES HERE
    # Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def find_principal(amount, rate, time):
    """
    Given the amount returned at the end of a time period for
    a bond, the interest rate, and the time in years,
    compute the principal, i.e., the face value for the bond
    (using simple interest).

    Inputs:
        amount (float): the payoff amount for the loan
        rate (float): the interest rate of the bond
        time (float): the number of years the bond was held

    Return (float): the face value of the bond
    """
    # Do not remove the three lines with assert. They help verify
    # that amount, principal, and time all have sensible values
    assert amount > 0
    assert rate > 0
    assert time > 0

    ### EXERCISE 3 -- YOUR CODE GOES HERE
    # You may define local variables here for use in
    # the result expression.

    # Replace "None" with an appropriate expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result

#######
# Constants used in Exercises 4-7
#######

URBAN_POPULATION_THRESHOLD = 80000
URBAN_DENSITY_THRESHOLD = 1200

RURAL_POPULATION_THRESHOLD = 3500
RURAL_DENSITY_THRESHOLD = 400

def non_urban_county(population, area):
    """
    Does a county not qualify as urban?

    Inputs:
        population (int): the number of people who live in an area
        area (float): the area of the county in square miles

    Returns (boolean): Returns False, if the county qualfies as urban,
        True otherwise.
    """
    # Do not remove the next two lines.  These assertions help verify
    # that the population and area values are sensible.
    assert population >= 0
    assert area > 0

    ### EXERCISE 4 -- YOUR CODE GOES HERE
    # Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def suburban_county(population, area):
    """
    Does a county qualify as suburban?

    Inputs:
        population (int): the number of people who live in an area
        area (float): the area of the county in square miles

    Limitations: your solution for this task must use
    relational operations and conditional statements.
    You may not use logical operators (and, or, not).

    Returns (boolean): Returns False if the county qualfies as suburban,
        True otherwise.

    """
    # Do not remove the next two lines.  These assertions help verify
    # that the population and area values are sensible.
    assert population >= 0
    assert area > 0

    result = None

    ### EXERCISE 5 -- YOUR CODE GOES HERE
    # Add code to set result to the correct value here.

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def alt_suburban_county(population, area):
    """
    Does a county qualify as suburban?

    Inputs:
        population (int): the number of people who live in an area
        area (float): the area of the county in square miles

    Limitations: your solution for this task must use only
    relational operations and logical operators (and, or, not).  You
    may not use conditional expressions or conditional statements for
    this exercise.

    Returns (boolean): Returns False if the county qualfies as suburban,
        True otherwise.

    """
    # Do not remove the next two lines.  These assertions help verify
    # that the population and area values are sensible.
    assert population >= 0
    assert area > 0

    ### EXERCISE 6 -- YOUR CODE GOES HERE
    # Replace "None" with an appropriate expression.

    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def categorize_county(population, area):
    """
    Categorize an area as rural, urban, or suburban based on its population
    and population density.

    Inputs:
        population (int): the number of people who live in an area
        area (float): the area of the county in square miles

    Returns (string): "rural", "urban", or "suburban"
    """
    # Do not remove the next two lines.  These assertions help verify
    # that the population and area values are sensible.
    assert population >= 0
    assert area > 0

    result = None

    ### EXERCISE 7 -- YOUR CODE GOES HERE
    # Add code to set result to "rural", "urban", or "other"
    # as appropriate

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def port_fee(length, weight):
    """
    Determine the port fee paid by for a container based on its weight
    and length.  All containers that weigh more than 20000kg must pay
    a port fee of $800.  The fee for containers below this limit is
    determined by their length: 50 ft containers pay $500, 20 ft
    containers pay $120, and 10ft containers pay $60.

    Inputs:
        length (int): container length in feet; must be 10, 20, or 50
        weight (int): the weight of the container in kilograms

    Returns (int): fee in dollars according to rules above
    """
    # Do not remove the next two lines.  They help verify that
    # weight and length have values appropriate for the function.
    assert weight > 0
    assert length in [10, 20, 50]

    ### EXERCISE 8 -- YOUR CODE GOES HERE
    # Add code to set fee to an appropriate value here.

    fee = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return fee
