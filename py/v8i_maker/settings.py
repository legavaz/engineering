
DEBUG = True

# ИНТЕГРАЦИЯ С 1С

bases = "danilin-vi; srv-1ctest; 1c-server"

URL_1C_API = """http://danilin-vi/dnv_note/hs/query/query_data/{"id_api_query": "BazyNaKlastere","param": {"servers": "{%bases%}" }}"""
URL_1C_API = URL_1C_API.replace('%bases%', bases)


LOGIN_1C = '1CV8'
PASSWORD_1C = '1CV8'

v8i_file = r'D:\scan1C.v8i'

template = """
[%name%]
Connect=Srvr="%server%";Ref="%basename%";
OrderInList=%order_list%
ID=%guid%
Folder="%folder%"
OrderInTree=%order_tree%
External=0
App=Auto
WA=1
Version=8.3
AdditionalParameters=/UC 2233"""
