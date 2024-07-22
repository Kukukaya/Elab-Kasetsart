# Example 1
# s: 1235
# 1235 seconds equals 0 hour(s) 20 minute(s) and 35 second(s)

# Example 2
# s: 20456
# 20456 seconds equals 5 hour(s) 40 minute(s) and 56 second(s)

sec = int(input("s: "))

def caltime(x):
    hour = x // 3600
    mi = (x%3600) // 60
    outsec = x - (mi*60) - (hour*60*60)
    return hour,mi,outsec


func = caltime(sec)
print(f"{sec} seconds equals {func[0]} hour(s) {func[1]} minute(s) and {func[2]} second(s)")