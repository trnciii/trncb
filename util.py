from string import ascii_lowercase
import os

def suf(base, name):
	for c in ascii_lowercase:
		_name = name + c
		if not os.path.exists(os.path.join(base, _name)):
			return _name

	raise RuntimeError('failed to create publish name')

def path():
	return os.path.split(os.path.abspath(__file__))[0]
