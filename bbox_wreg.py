
import _winreg  # Registry code example by Jonas Wagner (29a.ch) (found with help of google:)

_registry = _winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER)


def get_key():
        return _winreg.OpenKey(_registry, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, _winreg.KEY_ALL_ACCESS)


def add(name, application):
    key = get_key()
    _winreg.SetValueEx(key, name, 0, _winreg.REG_SZ, application)
    _winreg.CloseKey(key)


def check(name):
    key = get_key()
    exists = True
    try:
        _winreg.QueryValueEx(key, name)
    except WindowsError:
        exists = False
    _winreg.CloseKey(key)
    return exists


def delete(name):
    key = get_key()
    _winreg.DeleteValue(key, name)
    _winreg.CloseKey(key)
