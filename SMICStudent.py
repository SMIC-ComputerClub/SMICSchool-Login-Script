import json
import urllib.request, http.cookiejar
import datetime

class SMICStudent(object):
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password
        self.cookie_jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie_jar))
        self.userAgentHeader = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

        self.login_url    = 'https://www.smicschool.com/userlogin.cfm'
        self.profile_url  = 'https://www.smicschool.com/cf_directory/cp.cfm'
        self.calendar_url = 'https://www.smicschool.com//cf_calendar/ajax/fullcalendar.cfm'

        self.opener.open(self.login_url)
                
    def login(self):
        parameters = {
            'do'      : 'login',
            'p'       : '144',
            'username':  self.username,
            'password':  self.password,
            'submit'  : 'login'
        }
        details = urllib.parse.urlencode(parameters).encode('UTF-8')
        req = urllib.request.Request(
            self.login_url,
            details,
            headers = self.userAgentHeader
        )
        req.add_header('Referer', 'https://www.smicschool.com/userlogin.cfm')

        self.opener.open(req)

    def retrieve_calendar(self, start_date, end_date):
        if type(start_date) != datetime.datetime or type(end_date) != datetime.datetime:
            raise Exception("Plase use datetime.datetime for the time")

        date_format = '%m/%d/%Y'
        parameters = {
            'action'         : 'getEvents',
            'startDate'      :  start_date.strftime('%m/%d/%Y'),
            'endDate'        :  end_date.strftime('%m/%d/%Y'),
            'isMobile'       : 'false',
            'isArchived'     : 'false',
            'calendarIDList' : '353,354,355,357,358,359,702,729,761,2467,2469,2665,2666,2771',
            'teamIDList'     : ''
        }
        details = urllib.parse.urlencode(parameters).encode('UTF-8')
        
        req = urllib.request.Request(
            self.calendar_url,
            details,
            headers = self.userAgentHeader
        )

        req.add_header('Referer', 'https://www.smicschool.com/groups.cfm?groupDashboardView=calendar')

        with self.opener.open(req) as resp:
            return json.loads(resp.read().decode())

        
