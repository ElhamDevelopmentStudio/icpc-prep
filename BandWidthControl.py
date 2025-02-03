def format_speed(speed):
  if speed < 1024:
    return str(round(speed, 2)) + "B"
  elif speed < 1024**2:
    return str(round(speed/1024, 2)) + "KB"
  elif speed < 1024**3:
    return str(round(speed/(1024**2), 2)) + "MB"
  else:
    return str(round(speed/(1024**3), 2)) + "GB"
  
  
num_cases = int(input())

for case in range(num_cases):
  num_lines = int(input())
  
  total_download = 0
  total_upload = 0
  total_time = 0

  for i in range(num_lines):
    line = input().split()
    time = int(line[0])
    downloaded = int(line[1])
    uploaded = int(line[2])
    
    total_download += downloaded
    total_upload += uploaded
    total_time += time

  total_time_secs = total_time / 1000
  down_speed = total_download / total_time_secs
  up_speed = total_upload / total_time_secs

  down_speed_str = format_speed(down_speed) 
  up_speed_str = format_speed(up_speed)

  print(down_speed_str + "/" + up_speed_str)

  if case != num_cases - 1:
    print("---")

