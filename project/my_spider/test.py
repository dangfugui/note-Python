from pyaria2 import Aria2RPC
jsonrpc = Aria2RPC(url="http://192.168.0.11:6800/rpc")
options = {"dir": '/srv/dev-disk-by-label-share/_download/test/', "out": 'test.jpg', }
hook_id = jsonrpc.addUri(['https://pppp.642p.com/image/202004/81ztxANt.jpg'], options=options)