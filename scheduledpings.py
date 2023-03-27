import json
import time
import managementmodes as mm
mm.create_schedule_settings_if_not_exists()
dir = "history"
readschedule = open(f"{dir}/schedule.json","r",encoding="UTF-8")
settings = json.load(readschedule)
sec = 0.0
while settings["do-scheduled-ping"]:
    if (settings["schedule-time-in-minutes"]*60) < 2.0:
        break
    if sec >= (settings["schedule-time-in-minutes"]*60):
        mm.perform_ping_check()
        sec = 0.0
    else:
        time.sleep(1.0)
        sec += 1.0
