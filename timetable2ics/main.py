import csv
from datetime import datetime, timedelta, time

BASE_MONDAY = datetime(2027, 3, 1)
WEEKS = 16

lines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//timetable2ics//CN",
]

with open("courses.csv", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        weekday = int(row["星期"])
        day = BASE_MONDAY + timedelta(days=weekday - 1)
        start = datetime.combine(day.date(), time.fromisoformat(row["开始"]))
        end = datetime.combine(day.date(), time.fromisoformat(row["结束"]))

        lines += [
            "BEGIN:VEVENT",
            f"UID:{start.strftime('%Y%m%dT%H%M%S')}-{row['课程']}",
            f"DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%SZ')}",
            f"DTSTART:{start.strftime('%Y%m%dT%H%M%S')}",
            f"DTEND:{end.strftime('%Y%m%dT%H%M%S')}",
            f"RRULE:FREQ=WEEKLY;COUNT={WEEKS}",
            f"SUMMARY:{row['课程']}",
            f"LOCATION:{row['地点']}",
            "END:VEVENT",
        ]

lines.append("END:VCALENDAR")

with open("courses.ics", "w", encoding="utf-8", newline="") as f:
    f.write("\r\n".join(lines))

print("生成完成")