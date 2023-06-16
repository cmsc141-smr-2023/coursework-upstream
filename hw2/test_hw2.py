"""
CMSC 14100
Summer 2023

Test code for Homework #2
"""

import os
import sys

import pytest
import test_helpers as helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

import hw2

MODULE = "hw2"

def check_result(actual, expected, recreate_msg):
    """
    Do the work of checking the result when the
    correctness test is equality.
    """
    # We expect a result is not None
    helpers.check_not_none(actual, recreate_msg)
    # We expect a result of the right type
    helpers.check_type(actual, expected, recreate_msg)
    # We expect a result that is the same as expected
    helpers.check_equals(actual, expected, recreate_msg)

@pytest.mark.parametrize("a, b, c, x, expected", 
                         [(0,0,0,0,0),
                          (1,0,0,0,0),
                          (0,1,0,0,0),
                          (0,0,1,0,1),
                          (0,0,0,1,0),
                          (1,1,1,1,3),
                          (1,1,1,2,7),
                          (1,1,1,10,111),
                          (-1,0,0,1,-1),
                          (1,0,0,-1,1),
                          (1,2,3,4,27),
                          (-1,2,3,4,-5)])
def test_polynomial(a, b, c, x, expected):
    """
    Do a single test for Exercise 1: polynomial
    """                     
    recreate_msg = helpers.gen_recreate_msg(MODULE, "polynomial",
                                            a, b, c, x)
    actual = hw2.polynomial(a, b, c, x)
    check_result(actual, expected, recreate_msg)

@pytest.mark.parametrize("a, b, n, expected",
                         [(2, 4, 2, False),
                          (2, 7, 5, False),
                          (1, 10, 4, True),
                          (8, -8, 5, True),
                          (-8, 7, 5, False)])
def test_not_congruent_mod_n(a, b, n, expected):
    """
    Do a single test for Exercise 2: not_congruent_mod_n.
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "not_congruent_mod_n",
                                            a, b, n)
    actual = hw2.not_congruent_mod_n(a, b, n)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("amount, rate, time, expected",
                         [(1000.00, 11.0, 1.0, 900.9009009),
                          (1250.00, 8.0, 2.0, 1077.586207),
                          (2000.00, 3.0, 20.0, 1250.0),
                          (10000.00,7.5, 2.0, 8695.652174)])
def test_find_principal(amount, rate, time, expected):
    """
    Do a single test for Exercise 3: find_principal
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "find_principal",
                                            amount, rate, time)
    actual = hw2.find_principal(amount, rate, time)
    helpers.check_not_none(actual, recreate_msg)
    helpers.check_type(actual, expected, recreate_msg)
    helpers.check_float_equals(actual, expected, recreate_msg)


##### County classification test cases #####

county_classes = \
    [(8500000, 302.6, "urban"),  # NYC: Urban
     (2700000, 231.7, "urban"),  # Chicago: Urban

     ## Population at urban threshold
     # Population density just above urban threshold
     (80000, 65.5, "urban"),
     # Population density at urban threshold
     (80000, 66.65, "urban"),
     # Population density just below urban threshold
     (80000, 67.0, "suburban"),

     ## Population below urban threshold
     # Population density above urban threshold
     (79999, 60.0, "suburban"),
     # population density just below urban threshold
     (79999, 70.0, "suburban"),

     ## Population meets rural threshold
     # Population density at rural threshold
     (3500, 8.8, "rural"),
     # Population density above rural threshold
     (3500, 8.0, "suburban"),
     # Population density below threshold
     (3500, 9.0, "rural"),

     ## Population meets rural threshold
     # Population density at rural threshold
     (1000, 2.5, "rural"),
     # Population density above rural threshold
     (1000, 2.0, "suburban"),
     # Population density below threshold
     (1000, 500.0, "rural"),

     ## Population neither rural nor urban
     # Population density at rural threshold
     (5000, 12.5, "suburban"),
     # Population density below rural threshold
     (5000, 40.0, "suburban"),
     # Population density urban threshold
     (5000, 4.15, "suburban"),
     # Population density above urban threshold
     (5000, 4.0, "suburban")]
@pytest.mark.parametrize("population, area, label", county_classes)
def test_non_urban_county(population, area, label):
    """
    Do a single test for Exercise 4: non_urban_county
    """
    expected = label.lower() != "urban" #not in ["rural",  "suburban"]
    recreate_msg = helpers.gen_recreate_msg(MODULE, "non_urban_county",
                                            population, area)
    actual = hw2.non_urban_county(population, area)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("population, area, label", county_classes)
def test_suburban_county(population, area, label):
    """
    Do a single test for Exercise 5: suburban_county
    """
    expected = label.lower() == "suburban"
    recreate_msg = helpers.gen_recreate_msg(MODULE, "suburban_county",
                                            population, area)
    actual = hw2.suburban_county(population, area)
    check_result(actual, expected, recreate_msg)


# Use a test name that does not have "non_suburban_county" as a substring
# to simplify grader.py.
@pytest.mark.parametrize("population, area, label", county_classes)
def test_alt_sub_county(population, area, label):
    """
    Do a single test for Exercise 6: alt_suburban_county
    """
    expected = label.lower() == "suburban"
    recreate_msg = helpers.gen_recreate_msg(MODULE, "alt_suburban_county",
                                            population, area)
    actual = hw2.alt_suburban_county(population, area)
    check_result(actual, expected, recreate_msg)

@pytest.mark.parametrize("population, area, expected", county_classes)
def test_categorize_county(population, area, expected):
    """
    Do a single test for Exercise 7: categorize_county
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "categorize_county",
                                            population, area)
    actual = hw2.categorize_county(population, area)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("length, weight, expected",
                         [(10, 43000, 800),   # above weight threshold
                          (20, 33000, 800),
                          (50, 23000, 800),

                          (10, 20000, 60),    # just below weight threshold
                          (20, 20000, 120),   # just below weight threshold
                          (50, 20000, 500),   # just below weight threshold

                          (10, 2500, 60),     # well below weight threshold
                          (20, 2500, 120),
                          (50, 2500, 500)])
def test_port_fee(length, weight, expected):
    """
    Do a single test for Exercise 8: port_fee
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "port_fee",
                                            length, weight)
    actual = hw2.port_fee(length, weight)
    check_result(actual, expected, recreate_msg)
