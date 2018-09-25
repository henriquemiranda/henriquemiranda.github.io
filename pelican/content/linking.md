Title: Linking
Date: 2018-07-20 12:11
Category: Computers
Status: Draft

Linking anything
---------------------------------------

Compiling and linking a code is not always easy.
I will some tools that can help you to debug your compilation problem.

First of what


How do you find what path the linker is searching libraries for?

    :::bash
    gcc -v -Wl,

When creating you compilation command you should pay special attention to the order in which the `-L` tags are passed
specially in folders with many libraries.


Where can I specify paths for the libraries?
LIBRARY_PATH
LD_LIBARY_PATH
DYLD_LIBRARY_PATH

