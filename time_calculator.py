def add_time(start, duration,week="default"):
    weekDays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    time=start.split()
    minute=time[0].split(':')[1]
    hour=time[0].split(':')[0]
    day=0
    durationhour=int(duration.split(':')[0])
    if durationhour>=24:
        day+=durationhour//24
        durationhour=durationhour%24
    minute=int(minute)+int(duration.split(':')[1])
    hour=int(hour)+durationhour
    if minute>59:
        minute-=60
        hour+=1   
    if hour>=12:
        if hour!=12:
            hour-=12
        else:hour=12
        if time[1]=='AM':
            time[1]='PM'
        else:
            day+=1
            time[1]='AM'

    if week!="default":
        for k in weekDays:
            if week.lower()==k.lower():
                i=weekDays.index(k)
                
                nextweekday=0
                
                if day>=7:
                    nextweekday=day%7
                    total=i+nextweekday
                else:
                
                    total=i+(day%7)
        if total>6:
            total-=7
        week=weekDays[total]
       

    if day==0:
        return_time="{}:{} {}".format(str(hour),str(minute).zfill(2),time[1])
    elif day==1:
        return_time="{}:{} {} (next day)".format(str(hour),str(minute).zfill(2),time[1])
    else:
        return_time="{}:{} {} ({} days later)".format(str(hour),str(minute).zfill(2),time[1],day)
    if week!="default" and day==0:
        return_time="{}:{} {}, {}".format(str(hour),str(minute).zfill(2),time[1],week)
    if week!="default" and day==1:
        return_time="{}:{} {}, {} (next day)".format(str(hour),str(minute).zfill(2),time[1],week)
    if week!="default" and day>1:
        return_time="{}:{} {}, {} ({} days later)".format(str(hour),str(minute).zfill(2),time[1],week,day)


    return return_time

