"""
CMSC 14100
Autumn 2022

Test code for Homework #3
"""

import os
import sys

import random
import pytest
import test_helpers as helpers


# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw3

MODULE = "hw3"

ls_tests = [
    ([],None),
    (['a'],'a'),
    (['a','a'],'a'),
    (['a','bb'],'bb'),
    (['aa','b'],'aa'),
    (['aa','bb','ccc'],'ccc'),
    (['aa','bbb','cc'],'bbb'),
    (['aaa','bb','cc'],'aaa'),
    (['aaa','bbb'],['aaa','bbb']),
    (['a','b','c'],['a','b','c']),
    (['aa','bb','c'],['aa','bb']),
    (['aa','b','cc'],['aa','cc']),
    (['a','bb','cc'],['bb','cc']),
    ([''],'')
]
@pytest.mark.parametrize("strings, expected", ls_tests)
def test_longest_string(strings, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "longest_string",
                                            strings)
    actual = hw3.longest_string(strings)
    if type(expected)==list:
        helpers.check_one_of(actual, expected, recreate_msg)
    else:
        helpers.check_result(actual, expected, recreate_msg)

exclaim_tests = [
    ([],[]),
    (['x'],['x!']),
    (['x','y'],['x!','y!']),
    (['','!'],['!','!!']),
    (['abc','xyz','m'],['abc!','xyz!','m!'])
]
@pytest.mark.parametrize("strings, expected",exclaim_tests)
def test_exclaim(strings, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "exclaim",
                                            strings)
    actual = hw3.exclaim(strings)
    helpers.check_result(actual, expected, recreate_msg)

cx_tests = [
    ('',0),
    ('x',1),
    ('X',1),
    ('y',0),
    ('xy',1),
    ('Xy',1),
    ('xY',1),
    ('xx',2),
    ('Xx',2),
    ('xX',2),
    ('XX',2),
    ('abcdef',0),
    ('axcdxf',2),
    ('XxXxYyYy',4),
    ('xxxxXXXX',8)
]
@pytest.mark.parametrize("string, expected",cx_tests)
def test_count_x(string, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "count_x",
                                            string)
    actual = hw3.count_x(string)
    helpers.check_result(actual, expected, recreate_msg)
    
    
cb_tests = [
    (0,[],0),
    (0,[1],0),
    (1,[0],1),
    (1,[1],0),
    (1,[2,3],0),
    (1,[2,0],1),
    (2,[1,0],2),
    (3,[1,2,0],3),
    (3,[9,9,9],0),
    (3,[3,3,3],0)
]
@pytest.mark.parametrize("threshold, numbers, expected",cb_tests)
def test_count_below(threshold, numbers, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "count_below",
                                            threshold, numbers)
    actual = hw3.count_below(threshold, numbers)
    helpers.check_result(actual, expected, recreate_msg)
    

sa_tests = [
    (10,[],0),
    (10,[2],0),
    (10,[10],0),
    (10,[11],11),
    (10,[1,11],11),
    (10,[12,1],12),
    (10,[12,11],23),
    (10,[3,4,5],0),
    (10,[3,44,5],44),
    (10,[44,3,5],44),
    (10,[44,3,44],88),
    (0,[1,2,3],6),
    (99,[1,2,3],0)
]
@pytest.mark.parametrize("threshold, numbers, expected",sa_tests)
def test_sum_above(threshold, numbers, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "sum_above",
                                            threshold, numbers)
    actual = hw3.sum_above(threshold, numbers)
    helpers.check_result(actual, expected, recreate_msg)

    
tri_tests = [
    (((0,0),(0,1),(1,1)),0.5),
    (((0,0),(0,-1),(-1,1)),0.5),
    (((0,0),(0,-1),(-1,-1)),0.5),
    (((0,0),(0,1),(1,-1)),0.5),
    (((0,0),(3,0),(3,4)),6),
    (((0,0),(-3,0),(-3,4)),6),
    (((0,0),(3,0),(3,-4)),6),
    (((0,0),(-3,0),(-3,-4)),6)    
]
@pytest.mark.parametrize("points, expected",tri_tests)
def test_triangle_area(points, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "triangle_area",
                                            points)
    actual = hw3.triangle_area(points)
    helpers.check_float_equals(actual, expected, recreate_msg)
    
far_tests = [
    ((1,1),[],None),
    ((1,1),[(0,0)],(0,0)),
    ((1,1),[(0,0),(0,1)],(0,0)),
    ((1,1),[(1,1.1),(0,1),(1,0)],[(0,1),(1,0)]),
    ((0,0),[(0,0.1),(0,0.2)],(0,0.2)),
    ((0,0),[(11,11),(2,2),(-3,-3)],(11,11)),
    ((-1,-2),[(-2,-3),(22,33),(-222,333)],(-222,333))
]
@pytest.mark.parametrize("point, points, expected",far_tests)
def test_farthest(point, points, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "farthest",
                                            point, points)
    actual = hw3.farthest(point, points)
    if type(expected)==list:
        helpers.check_one_of(actual, expected, recreate_msg)
    else:
        helpers.check_result(actual, expected, recreate_msg)


inside_tests = [
    (((0,0),10),[],[]),
    (((0,0),10),[(1,1)],[(1,1)]),
    (((0,0),10),[(1,1),(10,10)],[(1,1)]),
    (((0,0),10),[(1,1),(10,10),(-10,10),(10,-10),(-10,-10)],[(1,1)]),
    (((0,0),10),[(1,1),(10,10),(-1,-1)],[(1,1),(-1,-1)]),
    (((0,0),10),[(11,1),(10,10),(-1,-1)],[(-1,-1)]),
    (((0,0),0.1),[(11,1),(10,10),(-1,-1)],[]),    
]
@pytest.mark.parametrize("circle, points, expected",inside_tests)
def test_inside(circle, points, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "farthest",
                                            circle, points)
    actual = hw3.inside(circle, points)
    helpers.check_result(actual, expected, recreate_msg)


box_tests = [
    ([],None),
    ([(1,1)],((1,1),(1,1))),
    ([(1,1),(1,1)],((1,1),(1,1))),
    ([(0,1),(1,0)],((0,1),(1,0))),
    ([(1,0),(0,1)],((0,1),(1,0))),
    ([(1,0),(0.3,0.4),(0,1)],((0,1),(1,0))),
    ([(0,0),(1,1)],((0,1),(1,0))),
    ([(0,0),(0,0.5),(0,0.9),(1,1)],((0,1),(1,0))),
    ([(0,0),(0,0.5),(0,-1),(1,1)],((0,1),(1,-1))),
    ([(1,1),(2,2)],((1,2),(2,1))),
    ([(-6,0),(6,-1)],((-6,0),(6,-1))),
    ([(6,-1),(-6,0)],((-6,0),(6,-1))),
    ([(6,-1),(0,0),(-6,0)],((-6,0),(6,-1))),
    ([(0,0),(6,-1),(-6,0)],((-6,0),(6,-1))),
    ([(6,-1),(-6,0),(0,0)],((-6,0),(6,-1))),
    ([(6,-1),(-6,0),(0,0),(0,0),(0,0)],((-6,0),(6,-1)))
]
@pytest.mark.parametrize("points, expected",box_tests)
def test_bounding_box(points, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "bounding_box",
                                            points)
    actual = hw3.bounding_box(points)
    helpers.check_result(actual, expected, recreate_msg)
    
