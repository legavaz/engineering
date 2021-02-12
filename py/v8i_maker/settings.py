
DEBUG = False

# ИНТЕГРАЦИЯ С 1С

URL_1C_API = [r'http://1c-www-server/Buh-L-PACK/hs/query/query_data/BazyNaKlastere',
              r'http://localhost/danv_copy_lpack_buh3/hs/query/query_data/BazyNaKlastere',]


LOGIN_1C = '1CV8'
PASSWORD_1C = ''

v8i_file = r'D:\scan1C.v8i'

template = """
[%name%]
Connect=Srvr="%server%";Ref="%basename%";
OrderInList=%order_list%
Folder="%folder%"
OrderInTree=%order_tree%
External=0
App=Auto
WA=1
Version=8.3
AdditionalParameters=/UC 2233"""
