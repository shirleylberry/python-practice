from nose.tools import *
from ex48 import lexicon



# test to make sure the correct direction is returned
def test_directions():
	assert_equal(lexicon.scan('north'), [('direction', 'north')])
	result = lexicon.scan("north south east")
	assert_equal(result, [('direction', 'north'),
						  ('direction', 'south'),
						  ('direction', 'east'),])

def test_verbs():
	assert_equal(lexicon.scan('go'), [('verb', 'go')])
	result = lexicon.scan("go kill eat")
	assert_equal(result, [('verb', 'go'),
						  ('verb', 'kill'),
						  ('verb', 'eat'),])

def test_fillers():
	assert_equal(lexicon.scan('the'), [('filler', 'the')])
	result = lexicon.scan("the in of and")
	assert_equal(result, [('filler', 'the'),
						  ('filler', 'in'),
						  ('filler', 'of'),
						  ('filler', 'and'),])

def test_nouns():
	assert_equal(lexicon.scan('bear'), [('noun', 'bear')])
	result = lexicon.scan("bear princess door cabinet")
	assert_equal(result, [('noun', 'bear'),
						  ('noun', 'princess'),
						  ('noun', 'door'),
						  ('noun', 'cabinet'),])

def test_numbers():
	assert_equal(lexicon.scan('1234'), [('number', 1234)])
	result = lexicon.scan("3 90210")
	assert_equal(result, [('number', 3),
						  ('number', 90210),])


def test_errors():
	assert_equal(lexicon.scan('ASDFASDFASDASD'), [('error', 'ASDFASDFASDASD')])
	result = lexicon.scan("bear BLABLA of")
	assert_equal(result, [('noun', 'bear'),
						  ('error', 'BLABLA'),
						  ('filler', 'of'),])
