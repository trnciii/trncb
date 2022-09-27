import datetime, sys, os
from string import ascii_lowercase

draft_base = os.path.join(
	os.path.split(os.path.abspath(__file__))[0],
	'docs/draft'
)

now = datetime.datetime.now()

name = ''
for c in ascii_lowercase:
	_name = name + c
	if not os.path.exists(os.path.join(draft_base, _name)):
		name = _name
		break
else:
	print('failed to create files')
	exit()


dirname = os.path.join(draft_base, name)

os.makedirs(dirname)
with open(os.path.join(dirname, f'{name}.md'), 'w', encoding='utf-8') as f:
	if len(sys.argv)>1:
		title = sys.argv[1]
	else:
		title = 'title'

	string = '\n'.join([
		f'# {title}\n'
	])

	f.write(string)