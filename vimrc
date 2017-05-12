" vundle
set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" Add all your plugins here (note older versions of Vundle used Bundle instead
" of Plugin)
Plugin 'gmarik/Vundle.vim'
" Code folding
Plugin 'tmhedberg/SimpylFold'
" python sytax checker
Plugin 'vim-scripts/indentpython.vim'
" auto-completion
Plugin 'Valloric/YouCompleteMe'
" python sytax checker
Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
" Filesystem
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
" Searching
Plugin 'kien/ctrlp.vim'
" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" vundle end

" split hotkeys
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Code folding based on indentation:
autocmd FileType python set foldmethod=indent
" use space to open folds
nnoremap <space> za
let g:SimpylFold_docstring_preview=1

" ------------Start Python PEP 8 stuff----------------
" Number of spaces that a pre-existing tab is equal to.
au BufRead,BufNewFile *py,*pyw,*.c,*.h set tabstop=4

" Spaces for indents
au BufRead,BufNewFile *.py,*pyw set shiftwidth=4
au BufRead,BufNewFile *.py,*.pyw set expandtab
au BufRead,BufNewFile *.py set softtabstop=4

" Wrap text after a certain number of characters
au BufRead,BufNewFile *.py,*.pyw, set textwidth=100

" Use UNIX (\n) line endings.
au BufNewFile *.py,*.pyw,*.c,*.h set fileformat=unix

" Use the below highlight group when displaying bad whitespace is desired.
highlight BadWhitespace ctermbg=red guibg=red

" Display tabs at the beginning of a line in Python mode as bad.
au BufRead,BufNewFile *.py,*.pyw match BadWhitespace /^\t\+/
" Make trailing whitespace be flagged as bad.
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

" Set the default file encoding to UTF-8:
set encoding=utf-8
" ----------Stop python PEP 8 stuff--------------

" auto-completion
let g:ycm_autoclose_preview_window_after_completion=1

" custom keys
let mapleader=" "
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

" python with virtualenv support
py << EOF
import os.path
import sys
import vim
if 'VIRTUA_ENV' in os.environ:
  project_base_dir = os.environ['VIRTUAL_ENV']
  sys.path.insert(0, project_base_dir)
  activate_this = os.path.join(project_base_dir,'bin/activate_this.py')
  execfile(activate_this, dict(__file__=activate_this))
EOF

" For full syntax highlighting:
let python_highlight_all=1
syntax on

" Colors
" colorscheme molokai
" colorscheme github
" set t_Co=256

" Trun on numbering
set nu

" ignore files in NERDTree
let NERDTreeIgnore=['\.pyc$', '\~$']

" NERDTree hotkeys
map <F3> :NERDTreeMirror<CR>
map <F3> :NERDTreeToggle<CR>

" copy and paste mode
set pastetoggle=<F9>
