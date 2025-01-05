#!/bin/bash

# Exit on any error
set -e

echo "Setting up Vim environment for Python, Bash, and C++ development on Fedora 41..."

# Step 1: Install Vim-Plug
echo "Installing Vim-Plug..."
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
echo "Vim-Plug installed."

# Step 2: Install Node.js (Required for CoC)
if ! command -v node &> /dev/null; then
    echo "Node.js not found. Installing Node.js..."
    curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -
    sudo dnf install -y nodejs
else
    echo "Node.js is already installed."
fi

# Step 3: Install npm (Node.js package manager) if not already installed
if ! command -v npm &> /dev/null; then
    echo "npm not found. Installing npm..."
    sudo dnf install -y npm
else
    echo "npm is already installed."
fi

# Step 4: Install Python language server (Pyright)
echo "Installing Pyright for Python..."
sudo npm install -g pyright -y

# Step 5: Install Bash language server
echo "Installing Bash language server..."
sudo npm install -g bash-language-server -y

# Step 6: Install Clang tools for C++
echo "Installing Clang tools for C++..."
sudo dnf install -y clang clang-tools-extra

# Step 7: Install Formatters
echo "Installing Python formatters (Black and Isort)..."
pip install --user black isort

# Step 8: Install Go (if not installed already)
if ! command -v go &> /dev/null; then
    echo "Go not found. Installing Go..."
    sudo dnf install -y golang
else
    echo "Go is already installed."
fi

# Step 9: Install shfmt (Shell script formatter)
if ! command -v shfmt &> /dev/null; then
    echo "Installing shfmt..."
    go install mvdan.cc/sh/v3/cmd/shfmt@latest
else
    echo "shfmt is already installed."
fi

# Step 10: Install ShellCheck (if not installed already)
if ! command -v shellcheck &> /dev/null; then
    echo "Installing ShellCheck..."
    sudo dnf install -y ShellCheck
else
    echo "ShellCheck is already installed."
fi

# Step 11: Create ~/.vimrc file
echo "Creating ~/.vimrc..."
cat > ~/.vimrc <<EOL
call plug#begin('~/.vim/plugged')

" Plugins
Plug 'dense-analysis/ale'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tpope/vim-sensible'

call plug#end()

set nocompatible
set encoding=utf-8
set number
set relativenumber
set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set smartindent
set updatetime=300
set shortmess+=c

filetype plugin indent on
syntax on

let mapleader = "\\"

inoremap <silent><expr> <Tab> pumvisible() ? "\\<C-n>" : "\\<Tab>"
inoremap <silent><expr> <S-Tab> pumvisible() ? "\\<C-p>" : "\\<S-Tab>"

nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gr <Plug>(coc-references)
nmap <silent> <leader>rn <Plug>(coc-rename)
nmap <silent> <leader>f <Plug>(coc-format)

autocmd CursorHold * silent call CocActionAsync('diagnostic')

let g:ale_fix_on_save = 1
let g:ale_linters = {
\\   'python': ['flake8', 'pylint'],
\\   'sh': ['shellcheck'],
\\   'cpp': ['clangd']
\\}
let g:ale_fixers = {
\\   'python': ['black', 'isort'],
\\   'sh': ['shfmt'],
\\   'cpp': ['clang-format']
\\}

autocmd FileType python nnoremap <silent> <C-r> :w<CR>:!python3 %<CR>
autocmd FileType sh nnoremap <silent> <C-r> :w<CR>:!chmod +x % && bash %<CR>
autocmd FileType cpp nnoremap <silent> <C-r> :w<CR>:!g++ -std=c++17 -o %:r % && ./%:r<CR>

let g:coc_global_extensions = ['coc-pyright', 'coc-sh', 'coc-clangd']

autocmd BufWritePre *.py,*.sh,*.cpp,*.c :ALEFix
autocmd BufLeave * silent! :w
EOL
echo "~/.vimrc created."

# Step 12: Install Vim plugins
echo "Installing Vim plugins..."
vim +PlugInstall +qall

echo "Vim environment setup complete! You can now use Vim for Python, Bash, and C++ development."
