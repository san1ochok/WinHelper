#  = = = = = = = = = = = = = = = = = = = = = = =
#   Project was created by Ukrainian Developer
#   Github: alexndrev
#   Telegram: alexndrev
#  = = = = = = = = = = = = = = = = = = = = = = =


import win32api
import ctypes
import sys
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import init
import time

from modules.ActivateOffice.office_activate import *
from modules.InstallBrowser.install_browser import *
from modules.ActivateWindows.activate_windows import *
from modules.ResetTCPIP.reset_tcpip import *
from modules.FixDNS.fix_dns import *

init(strip=not sys.stdout.isatty())


def start():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if start():
    cprint(figlet_format('Win Helper!', font='slant'),
           'red', attrs=['bold'])
    choose = input(
        f'\n\nChoose tool to start:\n\n\t[0] Exit\n\n\t[1] Activate Office365 (OLD VERSION)\n\t[2] Activate Office365 (NEW VERSION)\n\t[3] Install Browser (Google Chrome)\n\t[4] Activate Windows (Professional Edition)\n\t[5] Reset TCP/IP\n\t[6] Fix DNS\n\n\t[99] About coder\n\nPress key to start...\n\n<!>>')
    if choose == '1':
        office_activate(1)
    elif choose == '2':
        office_activate(2)
    elif choose == '3':
        install_browser()
    elif choose == '4':
        activate_windows()
    elif choose == '5':
        reset_tcpip()
    elif choose == '6':
        fix_dns()
    elif choose == '0':
        print('')
        time.sleep(1)
    elif choose == '99':
        win32api.MessageBox(0, '👨🏻‍💻 Author: alexndrev\nTelegram: @alexndrev\nGithub: @alexndrev\n\nVersion Script: 1.0', '👨🏻‍💻 WinHelper v1.0')
    else:
        win32api.MessageBox(0, 'Please restart script and press valid key input', '👨🏻‍💻 WinHelper v1.0')
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
                                        __file__, None, 1)
    exit()


if __name__ == '__main__':
    start()
	
