def checkLeap(year):
      if(year%4==0):
            if(year%100==0):
                  if(year%400==0):
                        return True
                  else:
                        return False
            else:
                  return True
      else:
            return False
if __name__ == "__main__":
      di = {'January':31,
            'February':28,
            'March':31,
            'April':30,
            'May':31,
            'June':30,
            'July':31,
            'August':31,
            'September':30,
            'October':31,
            'November':30,
            'December':31
            }
      instr = input().split()
      month = instr[0]
      date = instr[1][:-1]
      year = int(instr[2])
      time = instr[3].split(':')
      hh = time[0]
      mm = time[1]

      #print(month,date,year,hh,mm)

      #If leap year
      totalD = 365
      if(checkLeap(year)):
            di['February'] = 29
            totalD += 1

      #no.of days
      days = 0
      for i in di.keys():
            if(i==month):
                  if(date[0] == '0'):
                        date.lstrip('0')
                  days += int(date)
                  break
            else:
                  days += di[i]
      print(days)

      #hours
      h = 0
      if(hh[0] == '0'):
            hh.lstrip('0')
      h = int(hh)

      #minutes m
      m = 0
      if(mm[0] == '0'):
            mm.lstrip('0')
            m = int(mm)

      elapse = float(days*24*60 + h*60 + m)
      total = totalD*24*60
      progress = float(elapse/total)
      print(progress)