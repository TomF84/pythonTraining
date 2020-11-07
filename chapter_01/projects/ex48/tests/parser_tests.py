from nose.tools import *
from ex48 import parser


def test_peek():
    assert_equal(parser.peek([('direction', 'north')]), 'direction')
    result = parser.peek([('direction', 'north'),('noun', 'bear')])
    assert_equal(result, 'direction')
    assert_equal(parser.peek([]), None)
    
def test_match():
    assert_equal(parser.match([('direction', 'north')], 'direction'), ('direction', 'north'))
    assert_equal(parser.match([('direction', 'north')], 'verb'), None)
    assert_equal(parser.match([], ''), None)
    
def test_skip():
    assert_equal(parser.skip([('direction', 'north')], 'direction'), None)
    result = parser.skip([('stop', 'the'),('stop', 'in'),('direction', 'north'),('direction', 'north')], 'stop')
    assert_equal(result, None)
    
def test_parse_verb():
    assert_equal(parser.parse_verb([('verb', 'move')]), ('verb', 'move'))
    assert_equal(parser.parse_verb([('stop', 'to'),('verb', 'move')]), ('verb', 'move'))
    assert_raises(parser.ParserError, parser.parse_verb, [('noun', 'bear')]) 

def test_parse_object():
    assert_equal(parser.parse_object([('noun', 'hip')]), ('noun', 'hip'))
    assert_equal(parser.parse_object([('stop', 'to'),('noun', 'arm')]), ('noun', 'arm'))
    assert_raises(parser.ParserError, parser.parse_object, [('verb', 'bear')])
    
def test_parse_subject():
    assert_equal(parser.parse_subject([('noun', 'hip')]), ('noun', 'hip'))
    assert_equal(parser.parse_subject([('stop', 'to'),('verb', 'kill')]), ('noun', 'player'))
    assert_raises(parser.ParserError, parser.parse_subject, [('stop', 'to'),('direction','north')]) 
    
def test_parse_sentence():
    testSentence = parser.parse_sentence([('noun', 'bear'),('verb', 'eats'),('noun', 'honey')])
    assert_equal([testSentence.subject, testSentence.verb, testSentence.object],  ['bear', 'eats', 'honey'])
    testSentence = parser.parse_sentence([('stop', 'to'),('verb', 'kill'),('stop', 'a'),('noun', 'mockingbird')])    
    assert_equal([testSentence.subject, testSentence.verb, testSentence.object], ['player', 'kill', 'mockingbird'])
    assert_raises(parser.ParserError, parser.parse_sentence, [('noun', 'hip')])
    assert_raises(parser.ParserError, parser.parse_sentence, [('verb', 'cheer')])  
                          
