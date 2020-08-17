#!/Users/izzobacul/dev/Classroom/env/bin/python

from __future__ import print_function
import pickle
import os
import datetime
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from bs4 import BeautifulSoup

#VARS

sdir = os.path.dirname(__file__)
names = ['2nde C -- SNT', 'SECONDE', '2nde C', '2nde C English', '2e   C', 'seconde C', 'HG', 'SES-SECONDES- M. SARDOU', '2C', '2C matematicas', '2C Español', '2C Groupe1 Arts Plastiques', '2A-B-C-D-E-F-G']
rnames = ['SNT', 'SVT', 'EPS', 'Inglés', 'Historia Nacional', 'Physique Chimie', 'Histoire Géo', 'SES', 'Math', 'Math PSU', 'Español', 'Arte', 'Música']

with open(os.path.join(sdir, "tareas.html")) as txt:
    html = BeautifulSoup(txt.read(), features="html.parser")
    update = html.update

update.string = "Actualizando..."

with open(os.path.join(sdir, "tareas.html"), 'w') as txt:
    txt.write(str(html))

with open(os.path.join(sdir, "tareasbase.html")) as txt:
    html = BeautifulSoup(txt.read(), features="html.parser")
    nodateh = html.nodate
    lateh = html.late
    todoh = html.todo
    today = todoh.today
    thisweek = todoh.week
    after = todoh.after
    nothatlate = lateh.nothatlate
    latelate = lateh.latelate
    update = html.update
    dateh = html.date


day = datetime.datetime.now().day
month = datetime.datetime.now().month
year = datetime.datetime.now().year
date = datetime.date(year, month, day)
daysmonthlater = (datetime.date(year, month+1, 1)-datetime.timedelta(days=1)).day

#####

#FUNCTIONS

def cred():
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.me', 'https://www.googleapis.com/auth/classroom.courses.readonly']
    creds = None
    trying = True
    while trying:
        try:
            if os.path.exists(os.path.join(sdir, "token.pickle")):
                with open(os.path.join(sdir, "token.pickle"), 'rb') as token:
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        os.path.join(sdir, "credentials.json"), SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open(os.path.join(sdir, "token.pickle"), 'wb') as token:
                    pickle.dump(creds, token)

            service = build('classroom', 'v1', credentials=creds)
            trying = False
            #print("Connected")
        except:
            pass
    return(service)

def add(sub, courseWork_data, course_data):
    ul = sub.ul
    li = html.new_tag("li")
    ul.append(li)
    url = courseWork_data[4][:29] + 'u/2/' + courseWork_data[4][29:]
    a = html.new_tag("a", href=url, target='_blank')
    for index, n in enumerate(names):
        if course_data[0] == n:
            name = rnames[index]
            a.string =f"{courseWork_data[5]} / {name} / {courseWork_data[1]:02d}/{courseWork_data[2]:02d}/{str(courseWork_data[3])[2:]}"
            break
    for x in ul.find_all('li'):
        if not x.a:
            x.append(a)
            break

def main():
    service = cred()
    courses = service.courses().list().execute().get('courses', [])
    for c in courses:
        course_data = c['name'] , c['id']
        courseWork = service.courses().courseWork().list(courseId=course_data[1], orderBy="dueDate desc").execute().get('courseWork', [])
        for cw in courseWork:
            submissions = service.courses().courseWork().studentSubmissions().list(courseId=course_data[1], courseWorkId=cw['id']).execute().get('studentSubmissions', [])
            for s in submissions:
                submission_state = s['state']
                if not submission_state in {'TURNED_IN', 'RETURNED'}:
                    if 'dueDate' in cw:
                        courseWork_data = [cw['id'] , cw['dueDate']['day'] , cw['dueDate']['month'] , cw['dueDate']['year'] , cw['alternateLink'] , cw['title'] , cw['dueTime']['hours']]
                        if courseWork_data[6]<4:
                            courseWork_data[1] = courseWork_data[1]-1
                        if (courseWork_data[2]<month) or (courseWork_data[1]<day and courseWork_data[2]==month):
                            if (courseWork_data[2]==month and courseWork_data[1]>day-14) or (courseWork_data[2]<month and (30-courseWork_data[1]+day<14)):
                                add(nothatlate, courseWork_data, course_data)
                            else:
                                add(latelate, courseWork_data, course_data)
                        else:
                            if day==courseWork_data[1] and month==courseWork_data[2]:
                                add(today, courseWork_data, course_data)

                            elif (month == courseWork_data[2] and courseWork_data[1]-day < 7-date.weekday()) or (month==courseWork_data[2]+1 and daysmonthlater-day+courseWork_data[1]+date.weekday<7) :
                                add(thisweek, courseWork_data, course_data)
                            else:
                                add(after, courseWork_data, course_data)


                    else:
                        courseWork_data = cw['id'] , cw['alternateLink'] , cw['title']
                        ul = nodateh.ul
                        li = html.new_tag("li")
                        ul.append(li)
                        url = courseWork_data[1][:29] + 'u/2/' + courseWork_data[1][29:]
                        a = html.new_tag("a", href=url)
                        for index, n in enumerate(names):
                            if course_data[0] == n:
                                name = rnames[index]

                        a.string = courseWork_data[2] + " / " + name
                        for x in ul.find_all('li'):
                            if not x.a:
                                x.append(a)
                                break


    t = time.localtime()
    update.string = "Actualizado a las {0:02d}:{1:02d}:{2:02d}".format(t[3], t[4], t[5])
    dateh.string = f"{t[2]:02d}/{t[1]:02d}/{str(t[0])[2:]}"
    with open(os.path.join(sdir, "tareas.html"), 'w') as out:
        out.write(str(html))

#####

main()
