import datetime, sys, os, shutil
from string import ascii_lowercase
import re

base = os.path.split(os.path.abspath(__file__))[0]
blogs_base = os.path.join(base, 'docs/blogs')
draft_base = os.path.join(base, 'docs/draft')

try:
	draft_md = f'{sys.argv[1]}.md'
	draftname = os.path.join(draft_base, sys.argv[1])
	with open(os.path.join(draftname, draft_md)) as f:
		body = f.read()

	files = os.listdir(draftname)
	files.remove(draft_md)
except:
	print('failed to find draft')
	exit()

try:
	match = re.search(r'# (.+)\n', body)
	title = match.groups()[0]
except:
	print('failed to find title')
	exit()


now = datetime.datetime.now()

name = now.strftime('%Y%m%d')
for c in ascii_lowercase:
	_name = name + c
	if not os.path.exists(os.path.join(blogs_base, _name)):
		name = _name
		break
else:
	print('failed to create files')
	exit()


publishname = os.path.join(blogs_base, name)
os.makedirs(publishname)
with open(os.path.join(publishname, f'{name}.md'), 'w', encoding='utf-8') as f:
	f.write('\n'.join([
		'---',
		f'date: {now.strftime("%Y-%m-%d")}',
		'is_blog: true',
		'tags: []',
		'---',
		'',
		'',
		body
	]))


for _f in files:
	src = os.path.join(draftname, _f)
	dst = os.path.join(publishname, _f)
	shutil.move(src, dst)

shutil.rmtree(draftname)

print(f'published {sys.argv[1]} as {name}')
