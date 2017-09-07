days ={
    1 : "MO",
    2 : "TU",
    3 : "WE",
    4 : "TH",
    5 : "FR"
}
dtdaysa ={
    1 : "04",
    2 : "05",
    3 : "06",
    4 : "07",
    5 : "08"
}

dtdaysb ={
    1 : "11",
    2 : "12",
    3 : "13",
    4 : "14",
    5 : "15"
}

beginingh ={
    1 : "0850",
    2 : "0950",
    3 : "1120",
    4 : "1220",
    5 : "1440"
}
endingh ={
    1 : "0945",
    2 : "1045",
    3 : "1215",
    4 : "1315",
    5 : "1545"
}

lessons = []


class Lesson(object):
    def __init__(self):
        self.name = ""
        self.day = ""
        self.room = ""
        self.period = ""
        self.begtime = ""
        self.endtime = ""
        self.dtstartday = ""
        self.aorb = ""

    def process(self):
        self.begtime = beginingh[self.period]
        self.endtime = endingh[self.period]
        if self.aorb == "A":
            self.dtstartday = dtdaysa[self.day]
        else:
            self.dtstartday = dtdaysb[self.day]
        self.day = days[self.day]

    def writeout(self):
        print("BEGIN:VEVENT\r\nDTSTART;TZID=Europe/London:201709"+self.dtstartday+"T"+self.begtime+"00Z")
        print("DTEND;TZID=Europe/London:201709"+self.dtstartday+"T"+self.endtime+"00Z")
        print("RRULE:FREQ=WEEKLY;UNTIL=20180705T235959Z;INTERVAL=2;BYDAY="+self.day)
        print("LOCATION:"+self.room)
        print("DTSTAMP:20170906T081800Z\r\nSEQUENCE:0\r\nSTATUS:CONFIRMED\r\nCREATED:20170906T075102Z\r\nDESCRIPTION:\r\nLAST-MODIFIED:20170906T075137Z")
        print("SUMMARY:"+self.name)
        print("UID:" + self.aorb + self.day + str(self.period) + "@dziedzic.cf")
        print("STATUS:CONFIRMED\r\nTRANSP:OPAQUE\r\nEND:VEVENT")


def masterwriteout():
    print("BEGIN:VCALENDAR\r\nPRODID:-//Google Inc//Google Calendar 70.9054//EN\r\nVERSION:2.0\r\nCALSCALE:GREGORIAN\r\nMETHOD:PUBLISH\r\nX-WR-CALNAME:TT\r\nX-WR-TIMEZONE:Europe/London\r\nX-WR-CALDESC:\r\nBEGIN:VTIMEZONE\r\nTZID:Europe/London\r\nX-LIC-LOCATION:Europe/London\r\nBEGIN:DAYLIGHT\r\nTZOFFSETFROM:+0000\r\nTZOFFSETTO:+0100\r\nTZNAME:BST\r\nDTSTART:19700329T010000\r\nRRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU\r\nEND:DAYLIGHT\r\nBEGIN:STANDARD\r\nTZOFFSETFROM:+0100\r\nTZOFFSETTO:+0000\r\nTZNAME:GMT\r\nDTSTART:19701025T020000\r\nRRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU\r\nEND:STANDARD\r\nEND:VTIMEZONE")
    for lesson in lessons:
        lesson.process()
        lesson.writeout()
    print("END:VCALENDAR")


def loaddata(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        num = len(lines)/6
        for i in range(int(num)):
            templesson = Lesson()
            n = i*6
            templesson.name = lines[n].strip()
            templesson.aorb = lines[n+1].strip()
            templesson.day = int(lines[n+2].strip())
            templesson.period = int(lines[n+3].strip())
            templesson.room = lines[n+4].strip()
            lessons.append(templesson)

loaddata("data.txt")
masterwriteout()

