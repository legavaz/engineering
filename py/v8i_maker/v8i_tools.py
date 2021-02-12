import requests
import settings


def request_api_1c(param: str):
    url = param
    req = requests.get(url, auth=(settings.LOGIN_1C, settings.PASSWORD_1C))

    if settings.DEBUG:
        print(url)

    return req.json()


def scan_write_bases():
    m_text = ''
    iterator = 1
    for each in settings.URL_1C_API:
        baseName = request_api_1c(each)

        for each_basename in baseName:
            if settings.DEBUG:
                print(each_basename)
            iterator += 1
            r_temp = settings.template

            name = '{}/{} ({})'.format(each_basename['server'], each_basename['Name'], each_basename['Descr'])

            r_temp = r_temp.replace('%name%', name)
            r_temp = r_temp.replace('%server%', each_basename['server'])
            r_temp = r_temp.replace('%basename%', each_basename['Name'])
            r_temp = r_temp.replace('%folder%', each_basename['server'])
            r_temp = r_temp.replace('%order_list%', str(iterator))
            r_temp = r_temp.replace('%order_tree%', str(iterator+1))

            m_text = m_text + r_temp

    f = open(settings.v8i_file, 'w', encoding='utf-8')
    f.write(m_text)
    f.close()