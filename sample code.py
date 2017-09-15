# SMICStudent Usage Sample
from SMICStudent import SMICStudent
student = SMICStudent(username='username_here', password='password_here')
student.login()
result = student.retrieve_calendar()

print("There are {} calendar events".format(len(result['result'])))
