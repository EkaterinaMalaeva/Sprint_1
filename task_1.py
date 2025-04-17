line = '1h 45m, 360s, 25m, 30m 120s, 2h 60s'
all_min = 0

part_of_line = line.split(',')

for part in part_of_line:
    units = part.strip().split()

    for unit in units:
        if 'h' in unit:
            hours = int(unit.replace('h', ''))
            all_min += hours * 60
        elif 'm' in unit:
            minutes = int(unit.replace('m', ''))
            all_min += minutes
        elif 's' in unit:
            seconds = int(unit.replace('s', ''))
            all_min += seconds // 60

print(all_min)