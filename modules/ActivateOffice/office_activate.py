import os


def office_activate(version):
    if version == 1:
        os.startfile('src\ActivateOffice\script.bat')
    elif version == 2:
        os.startfile('src\ActivateOffice\scriptV2.bat')
