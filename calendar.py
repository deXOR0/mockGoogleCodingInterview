def time_to_number(time):
    hours = float(time[:time.find(':')])
    minute = float(time[time.find(':')+1:])
    return hours + (minute / 60)

def find_available_time_blocks(cal, bound, duration_converted):
    available_time_blocks = []
    prev_end = bound[0]
    for start, end in cal:
        if time_to_number(start) - time_to_number(prev_end) >= duration_converted:
            available_time_blocks.append([prev_end, start])
        prev_end = end

    if time_to_number(bound[1]) - time_to_number(prev_end) >= duration_converted:
        available_time_blocks.append([prev_end, bound[1]])

    return available_time_blocks

def find_available_meeting_time(cal1, bound1, cal2, bound2, duration):
    duration_converted = (duration / 60)

    merged_calendar = []

    max_cal1 = len(cal1)
    max_cal2 = len(cal2)

    i = j = 0

    while (i < max_cal1 and j < max_cal2):
        if (time_to_number(cal1[i][0]) < time_to_number(cal2[j][0]) and time_to_number(cal1[i][1]) <= time_to_number(cal2[j][1])):
            merged_calendar.append(cal1[i])
            i += 1
        else:
            merged_calendar.append(cal2[j])
            j += 1

    while (i < max_cal1):
        merged_calendar.append(cal1[i])
        i += 1

    while (j < max_cal2):
        merged_calendar.append(cal2[j])
        j += 1

    merged_bound = []
    merged_bound.append(bound1[0] if time_to_number(bound1[0]) >= time_to_number(bound2[0]) else bound2[0])
    merged_bound.append(bound1[1] if time_to_number(bound1[1]) <= time_to_number(bound2[1]) else bound2[1])
    print(find_available_time_blocks(merged_calendar, merged_bound, duration_converted))

cal1 = [['09:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
bound1 = ['09:00', '20:00']

cal2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
bound2 = ['10:00', '18:30']

duration = 30

find_available_meeting_time(cal1, bound1, cal2, bound2, duration)
