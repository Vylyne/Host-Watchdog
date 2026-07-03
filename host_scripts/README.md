
example moonraker output
```shell
curl -s http://localhost:7125/printer/info | jq ".result"
{
  "state": "ready",
  "state_message": "Printer is ready",
  "hostname": "sv08",
  "klipper_path": "/home/biqu/klipper",
  "python_path": "/home/biqu/klippy-env/bin/python",
  "process_id": 1114,
  "user_id": 1000,
  "group_id": 1000,
  "log_file": "/home/biqu/printer_data/logs/klippy.log",
  "config_file": "/home/biqu/printer_data/config/printer.cfg",
  "software_version": "v0.13.0-701-g7e64fc84-dirty",
  "cpu_info": "4 core ?"
}
```