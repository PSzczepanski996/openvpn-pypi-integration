import shutil


def string_replacer(filename, string, to):
    """Hacky way to replace string in file."""
    with open(filename, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(string, to)
    with open(filename, 'w') as file:
        file.write(filedata)


with open('vpnid.txt') as f:
    connection_id = f.readlines()[0]
string_replacer('pypi-down', '___VPN___ID___', connection_id)
shutil.copyfile('./debug-up', '/etc/network/if-up.d/debug-up')
string_replacer('pypi-up', '___VPN___ID___', connection_id)
shutil.copyfile('./debug-up', '/etc/network/if-up.d/debug-up')
string_replacer('pypi-up', connection_id, '___VPN___ID___')
string_replacer('pypi-up', connection_id, '___VPN___ID___')
print('Moved files successfully.')
