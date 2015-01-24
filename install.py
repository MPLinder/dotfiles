from glob import glob
from os import environ, getcwd, symlink, makedirs
from os.path import exists, expanduser, join, normpath
from platform import system
from sys import stderr


home = expanduser(environ['HOME'])

def install_sym(src, target):
    if exists(target):
        print >>stderr, "skipping %s, already exists" % target
    else:
        print "installing %s to %s" % (src, target)
        symlink(src, target)

for f in glob('*'):
    if any((f.startswith(x) for x in ('README', 'install'))):
        continue
    target = normpath(join(home, '.%s'%f))
    src = normpath(join(getcwd(), f))
    install_sym(src, target)
