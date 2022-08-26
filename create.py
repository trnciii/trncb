import datetime, sys, os
from string import ascii_lowercase

path_blogs = os.path.join(
	os.path.split(os.path.abspath(__file__))[0],
	'docs/blogs'
)

now = datetime.datetime.now()

name = now.strftime('%Y%m%d')
for c in ascii_lowercase:
	_name = name + c
	if not os.path.exists(os.path.join(path_blogs, _name)):
		name = _name
		break
else:
	print('failed to create files')
	exit()


dirname = os.path.join(path_blogs, name)

os.makedirs(dirname)
with open(os.path.join(dirname, f'{name}.md'), 'w', encoding='utf-8') as f:
	if len(sys.argv)>1:
		title = sys.argv[1]
	else:
		title = 'title'

	string = '\n'.join([
		'---',
		f'title: {title}',
		f'date: {now.strftime("%Y-%m-%d")}',
		'is_blog: true',
		'tags: []',
		'---',
		'',
		'',
		F'# {title}'
	])

	f.write(string)