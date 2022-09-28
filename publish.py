import datetime, sys, os, shutil, traceback
import util

blogs_base = os.path.join(util.path(), 'docs/blogs')

try:
	draft_md = f'{sys.argv[1]}.md'
	draft_dir = os.path.join(util.path(), 'docs/draft', sys.argv[1])
	with open(os.path.join(draft_dir, draft_md), encoding='utf-8') as f:
		body = f.read()
except:
	print('failed to find draft')
	traceback.print_exc()
	exit()


now = datetime.datetime.now()

try:
	name = util.suf(blogs_base, now.strftime('%Y%m%d'))
except :
	traceback.print_exc()
	exit()


publish_dir = os.path.join(blogs_base, name)
os.makedirs(publish_dir)
with open(os.path.join(publish_dir, f'{name}.md'), 'w', encoding='utf-8') as f:
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


files = os.listdir(draft_dir)
files.remove(draft_md)
for f in files:
	src = os.path.join(draft_dir, f)
	dst = os.path.join(publish_dir, f)
	shutil.move(src, dst)

shutil.rmtree(draft_dir)

print(f'published {draft_dir} as {publish_dir}')
