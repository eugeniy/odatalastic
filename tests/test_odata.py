# -*- coding: utf-8 -*-
from nose.tools import assert_equal
from odatalastic.odata import parse_query


def test_quoted_string():
    assert_equal(parse_query('"a"'), 'a')
    assert_equal(parse_query("'a'"), 'a')


def test_unicode_string():
    assert_equal(parse_query('"панда"'), 'панда')


def test_not():
    assert_equal(parse_query('not "b"'), {'not': 'b'})


def test_multiple_not():
    assert_equal(parse_query('not not "b"'), {'not': {'not': 'b'}})


def test_and():
    assert_equal(parse_query('"a" and "b"'), {'and': ['a', 'b']})


def test_multiple_and():
    assert_equal(parse_query('"a" and "b" and "c"'),
                 {'and': ['a', 'b', 'c']})


def test_or():
    assert_equal(parse_query('"a" or "b"'),
                 {'or': ['a', 'b']})


def test_multiple_or():
    assert_equal(parse_query('"a" or "b" or "c"'),
                 {'or': ['a', 'b', 'c']})


def test_operator_associativity():
    assert_equal(parse_query('("a" and "b") or "c"'),
                 {'or': [{'and': ['a', 'b']}, 'c']})
    assert_equal(parse_query('"a" and ("b" or "c")'),
                 {'and': ['a', {'or': ['b', 'c']}]})
    assert_equal(parse_query('not ("a" and "b")'),
                 {'not': {'and': ['a', 'b']}})
