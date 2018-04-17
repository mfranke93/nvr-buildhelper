# neovim remote build helper

This tool is supposed to extend the utilities provided by [https://github.com/mhinz/neovim-remote](neovim-remote) regarding the population of the quickfix list.
Specifically, for an output with a given error format, the quickfix list is populated _without_ jumping to the first entry.
Additionally, signs are added at all places where an error or warning was loaded.

This tool is supposed to more tightly couple the build process of a project with neovim.
