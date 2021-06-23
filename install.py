from glob import glob
import os
from platform import system
from sys import stderr


home = os.path.expanduser(os.environ['HOME'])

# Oh My Zosh
os.system('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
# Oh My Zosh will insert it's own zshrc. Remove it so that I can add the one I want
os.system('rm ~/.zshrc')

# Oh My Tmux
os.system('git clone https://github.com/gpakosz/.tmux ~/.tmux')
os.system('ln -s -f ~/.tmux/.tmux.conf ~/.tmux.conf')

def install_sym(src, target):
    if os.path.exists(target):
        print >>stderr, "skipping %s, already exists" % target
    else:
        print "installing %s to %s" % (src, target)
        os.symlink(src, target)

# Install symlinks
for f in glob('*'):
    if any((f.startswith(x) for x in ('README', 'install', 'Brewfile'))):
        continue
    target = os.path.normpath(os.path.join(home, '.%s'%f))
    src = os.path.normpath(os.path.join(os.getcwd(), f))
    install_sym(src, target)

# Homebrew
os.system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"; brew bundle')
