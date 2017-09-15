import json
login_url = 'https://www.smicschool.com/userlogin.cfm'
profile_url  = 'https://www.smicschool.com/cf_directory/cp.cfm'
calendar_url = 'https://www.smicschool.com//cf_calendar/ajax/fullcalendar.cfm'


import urllib.request, http.cookiejar

# Create an opener
cookieJar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJar))
userAgentHeader = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' }

data = {
    'do'      : 'login',
    'p'       : '144',
    'username': 'username',
    'password': 'password',
    'submit'  : 'login'
}

details = urllib.parse.urlencode(data).encode('UTF-8')

req = urllib.request.Request(
    login_url,
    details,
    headers = userAgentHeader,
)

req.add_header( 'Referer', 'https://www.smicschool.com/userlogin.cfm' )

# Get cookies from the SMIC school website
opener.open(login_url)

# Login to the website (associate the cookie with the current student)
opener.open(req)

# Retrieve calendar
data = {
    'action'         : 'getEvents',
    'startDate'      : '08/27/2017',
    'endDate'        : '10/01/2017',
    'isMobile'       : 'false',
    'isArchived'     : 'false',
    'calendarIDList' : '353,354,355,357,358,359,702,729,761,2467,2469,2665,2666,2771',
    'teamIDList'     : ''
}

details = urllib.parse.urlencode(data).encode('UTF-8')

req = urllib.request.Request(
    calendar_url,
    details,
    headers = userAgentHeader
)

req.add_header('Referer', 'https://www.smicschool.com/groups.cfm?groupDashboardView=calendar')

with opener.open(req) as resp, open("response.txt", 'w') as out:
    out.write(str(resp.read()))
    out.close()


# Read grade
##import re
##grade_pattern = re.compile("<div class=\"fieldValue\">\S+?(\d+)")
##
##with opener.open(profile_url) as r:
##    html = str(r.read())
##    if html.find('<form name="userlogin"') < 0:
##        print( data['username'], 'is in Grade', re.findall(grade_pattern, html)[0] )
##    else:
##        print( 'Please login with the right username or password' )
