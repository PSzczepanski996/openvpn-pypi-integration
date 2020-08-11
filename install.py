import shutil
import os
import stat


def string_replacer(filename, string, to):
    """Hacky way to replace string in file."""
    with open(filename, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(string, to)
    with open(filename, 'w') as file:
        file.write(filedata)


def chmod_x(file):
    """Give +x permission to file."""
    st = os.stat(file)
    os.chmod(file, st.st_mode | stat.S_IEXEC)


with open('vpnid.txt') as f:
    content = f.readlines()
    user = content[0].rstrip()
    connection_id = content[1].rstrip()
string_replacer('pypi-down', '___USER___', user)
string_replacer('pypi-down', '___VPN___ID___', connection_id)
shutil.copyfile('./pypi-down', '/etc/network/if-post-down.d/pypi-down')
chmod_x('/etc/network/if-post-down.d/pypi-down')
string_replacer('pypi-up', '___USER___', user)
string_replacer('pypi-up', '___VPN___ID___', connection_id)
shutil.copyfile('./pypi-up', '/etc/network/if-up.d/pypi-up')
chmod_x('/etc/network/if-up.d/pypi-up')
string_replacer('pypi-down', connection_id, '___VPN___ID___')
string_replacer('pypi-up', connection_id, '___VPN___ID___')
string_replacer('pypi-down', user, '___USER___')
string_replacer('pypi-up', user, '___USER___')
print('Moved files successfully.')
