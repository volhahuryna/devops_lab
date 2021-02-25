import psutil
import time
from datetime import datetime
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--time_interval', type=float, default=300,
                    help='Time interval which snapshot is proceeded in')
parser.add_argument('-f', '--file_type', type=str,
                    help='File type which is used for output saving"')


class Write:
    def __init__(self, file_type, data_dict):
        self.file_type = file_type
        self.data_dict = data_dict

    def write_file(self):
        if self.file_type == 'json':
            with open('snapshot.json', 'w') as json_file:
                json.dump(self.data_dict, json_file)
        else:
            f = open("snapshot.txt", "w+")
            for key in self.data_dict.keys():
                one_str = key + " : " + \
                    self.data_dict[key]["TIMESTAMP"] + \
                    " : " + str(self.data_dict[key]["Stats"]) + "\n"
                f.write(one_str)
            f.close()


def main():
    iteration_number = 1
    data_dict = {}
    snapshot_interval = parser.parse_args().time_interval
    file_type = parser.parse_args().file_type
    while True:
        value_dict = {}
        timestamp = str(datetime.now())
        cpu_load = psutil.cpu_percent(interval=0)
        mem_usage = psutil.virtual_memory().percent
        io_info = "read: " + str(psutil.disk_io_counters(perdisk=False).read_time) \
            + " " + "write: " + str(psutil.disk_io_counters(perdisk=False).write_time)
        net_info = str(psutil.net_io_counters(pernic=True))
        snapshot_number = "SNAPSHOT" + " " + str(iteration_number)
        value_dict = {
            "TIMESTAMP": timestamp,
            "Stats": {
                "CPU total, %": cpu_load,
                "vMemory total, %": mem_usage,
                "IO read/write time": io_info,
                "NET_INFO": net_info,

            }
        }
        data_dict[snapshot_number] = value_dict
        writer = Write(file_type, data_dict)
        writer.write_file()
        time.sleep(snapshot_interval)
        iteration_number += 1


if __name__ == "__main__":
    main()
