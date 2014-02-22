from pyparsing import (operatorPrecedence, opAssoc, CaselessLiteral,
                       quotedString, removeQuotes)


def _not_expression(tokens):
    return {'not': tokens[0][-1]}


def _and_expression(tokens):
    return {'and': tokens[0][0::2]}


def _or_expression(tokens):
    return {'or': tokens[0][0::2]}


def _query_expression():
    operand = quotedString.setParseAction(removeQuotes)
    return operatorPrecedence(operand, [
        (CaselessLiteral('not'), 1, opAssoc.RIGHT, _not_expression),
        (CaselessLiteral('and'), 2, opAssoc.LEFT, _and_expression),
        (CaselessLiteral('or'), 2, opAssoc.LEFT, _or_expression)
    ])


def parse_query(value):
    grammar = _query_expression()
    return grammar.parseString(value)[0]
