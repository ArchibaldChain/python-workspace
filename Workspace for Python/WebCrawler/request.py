import requests
from bs4 import BeautifulSoup


def getSessionid(session):
    r = session.get('https://booked.concordia.ca/Web/?')
    phpsessid = r.headers['Set-Cookie'].split(";")[0]
    return phpsessid


def login(session, phpsessid):
    login_url = "https://booked.concordia.ca/Web/index.php"
    payload = {
        'email': "Z_YUGU",
        'password': 'HfkexAB0',
        'login': 'submit'
    }

    result = session.post(
        login_url,
        data=payload,
        headers=dict(referer=login_url, cookie=phpsessid)
    )
    return result

# return all the reservable slots on that day and the cookie for future use


def getReservables(date, phpsessid):
    # date in the query parameter
    payload = {'sid': 1, 'sd': date}

    r = requests.get(
        'https://booked.concordia.ca/Web/schedule.php', headers={'Cookie': phpsessid}, params=payload)

    # store the response for debug
    f = open("page.html", 'w')
    f.write(r.text)
    f.close()

    # get the new cookie and modify for some reason
    _cookie = r.headers['Set-Cookie']
    # print('cookie before modify')
    # print(_cookie)
    _cookie = _cookie.split(';')[0]
    _cookie += '; schedule_calendar_toggle=false'
    # print('cookie after modification')
    # print(_cookie)

    # get the tbody data for the html parser
    soup = BeautifulSoup(r.text, 'html.parser')
    reservableSlots = soup.find_all('td', class_='reservable clickres slot')
    reservables = []
    for x in reservableSlots:
        ref = x['ref']
        year = ref[:4]
        month = ref[4:6]
        day = ref[6:8]
        hour = ref[8:10]
        minute = ref[10:12]
        num = ref[14:]
        reservables.append(
            {'year': year, 'month': month, 'day': day, 'hour': hour, 'minute': minute, 'room number': num})
    return (reservables, _cookie)

# Procedure:
# 1. get php session id (first cookie)
# 2. login. Looks like that the server marks the session as a login status
# 3. a get request to get a new cookie
# 4. try to figure out how booking status data are loaded.

session = requests.session()

# get first cookie: phpsession
phpsessid = getSessionid(session)

# login to tell the server that this session has logged in
login(session, phpsessid)

# in the tbodydate, room are represented by numbers
reservables = getReservables('2020-01-01', phpsessid)
for slot in reservables:
    print(slot)

roomNumber = {
    '61': 'Webster Library LB-251 (Luxembourg)',
    '62': 'Webster Library LB-257 (Croatia)',
    '63': '***NO HDMI CONNECATION*** Webster Library LB-259 (New Zealand)',
    '53': 'Webster Library LB-351 (Netherlands)',
    '54': 'Webster Library LB-353 (Kenya)',
    '55': 'Webster Library LB-359 (Vietnam)',
    '6': 'Webster Library LB-451 (Brazil)',
    '5': 'Webster Library LB-453 (Japan)',
    '4': 'Webster Library LB-459 (Italy)',
    '58': 'Webster Library LB-518 (Ukraine)',
    '56': 'Webster Library LB-522 (Peru)',
    '59': 'Webster Library LB-547 (Lithuania)',
    '60': 'Webster Library LB-583 (Poland)'
}
