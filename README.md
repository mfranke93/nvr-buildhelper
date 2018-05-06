# neovim remote build helper

This tool is supposed to extend the utilities provided by
[https://github.com/mhinz/neovim-remote](neovim-remote) regarding the
population of the quickfix list.  Specifically, for an output with a given
error format, the quickfix list is populated _without_ jumping to the first
entry.  Additionally, signs are added at all places where an error or warning
was loaded.

This tool is supposed to more tightly couple the build process of a project
with neovim.

# Prerequisites

For this to work, the `neovim-remote` package must be installed, or the `nvr`
python library be provided in any other way. Neovim is also required, and the
neovim instance receiving the quickfix list and signs must have the
`/tmp/nvimsocket` socket.

# Usage

After copying the script to a directory listed in `$PATH`, it can simply be
called with the actual build command appended as command line arguments.

Example:

`nvr-buildhelper make`

`nvr-buildhelper g++ -std=c++17 -Wall -Wextra main.cpp`
