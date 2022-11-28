#!/usr/bin/env python3

__author__ = "Jonas Stein"
__maintainer__ = "Jonas Stein"
__copyright__ = "Copyright 2015, Jonas Stein"
__license__ = "GPL-3"
__version__ = "1.0.1"


# Simple menu for everyday commands

import subprocess

def my_cmd(thecommand):    
    return_code = subprocess.call(thecommand, shell=True)
    
def my_quit_fn():
    raise SystemExit


def invalid():
   print("Wrong key. Please try again.")

   
menu = {"1":("sync package list:  ","eix-sync"),
        "2":("clean:     ","emerge --depclean && eclean-dist --deep"),
        "3":("update:    ","emerge --update --newuse --deep --keep-going @world"),
        "4":("show logs: ","elogv"),
        "5":("read news: ","eselect news read new"),
        "6":("tidy up package.*: ","portpeek -arf -"),
        "7":("run libtool", "libtool --finish /usr/lib64"),
        "8":("build kernel", "make -j32 modules_prepare && make all -j32 && make modules_install && make install && grub-mkconfig -o /boot/grub/grub.cfg && emerge --ask @module-rebuild"),
        "q":("Quit       ","echo bye!")
       }
for key in sorted(menu.keys()):
     print(key+": " + menu[key][0] + menu[key][1])

ans = input("please select: ")

my_cmd(menu.get(ans,[None,invalid])[1])

