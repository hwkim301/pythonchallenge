import xmlrpc.client

class MyTransport(xmlrpc.client.Transport):
    accept_gzip_encoding = False 

conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php", transport=MyTransport())

print(conn.system.listMethods()) # ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']

print(conn.phone('Bert')) # 555-ITALY

