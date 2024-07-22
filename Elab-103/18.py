# ตัวอย่าง Input/Output
# Start time:
# >> Enter hour: 8
# >> Enter minute: 15
# >> Enter second: 0
# Finish time:
# >> Enter hour: 13
# >> Enter minute: 20
# >> Enter second: 0
# Elapsed time is 5 hours 5 minutes 0 seconds.

# read_hour() เพื่อคืนค่าชั่วโมงในระบบ 24 ชั่วโมง (นั่นคือ ค่าที่เป็นไปได้มีค่าตั้งแต่ 0 ถึง 23)
# read_minute() เพื่อคืนค่านาที (ค่าที่เป็นไปได้มีค่าตั้งแต่ 0 ถึง 59)
# read_second() เพื่อคืนค่าวินาที (ค่าที่เป็นไปได้มีค่าตั้งแต่ 0 ถึง 59)
# to_seconds(h, m, s) เพื่อคืนค่าจำนวนวินาทีทั้งหมดของเวลา h ชั่วโมง m นาที และ s วินาที
# time_elapsed(start, finish) เพื่อคืนค่าระยะเวลานับจากวินาทีที่ start ถึงวินาทีที่ finish


def read_hour():
    global h
    h = int(input("Enter hour: "))
    return h
def read_minute():
    global m
    m = int(input("Enter minute: "))
    return m
def read_second():
    global s
    s = int(input("Enter second: "))
    return s

def to_seconds(h,m,s):
    return (h*3600)+(m*60)+s

def time_elapsed(start,finish):
    vex = finish - start
    hour_s = vex // 3600
    minute_s = (vex-(hour_s*3600)) // 60
    second_s = vex-(hour_s*3600)-(minute_s*60)
    return f"{hour_s} hours {minute_s} minutes {second_s} seconds."
    
def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is',time_elapsed(start_time, finish_time))