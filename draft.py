import datetime, sys, os, traceback
import util

draft_base = os.path.join(util.path(), 'docs/draft')

try:
	name = util.suf(draft_base, '')
except:
	traceback.print_exc()
	exit()

dirname = os.path.join(draft_base, name)
os.makedirs(dirname)
with open(os.path.join(dirname, f'{name}.md'), 'w', encoding='utf-8') as f:
	title = sys.argv[1] if len(sys.argv)>1 else 'title'
	f.write(f'# {title}\n')

print(f'created {dirname}')
