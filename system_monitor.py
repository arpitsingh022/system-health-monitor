
import os
import platform
import shutil


class SystemMonitor:

    @staticmethod
    def run():

        print("\n===== SYSTEM INFORMATION =====")

        print("Operating System:", platform.system())
        print("OS Version:", platform.version())
        print("Hostname:", platform.node())
        print("Architecture:", platform.machine())
        print("Python Version:", platform.python_version())
        print("CPU Cores:", os.cpu_count())

        disk = shutil.disk_usage(os.getcwd())

        print("\n===== DISK INFORMATION =====")

        print(f"Total: {disk.total / (1024**3):.2f} GB")
        print(f"Used: {disk.used / (1024**3):.2f} GB")
        print(f"Free: {disk.free / (1024**3):.2f} GB")

        usage = disk.used / disk.total * 100

        print(f"Disk Usage: {usage:.2f}%")

        if usage > 80:
            print("WARNING: Disk usage is high!")
        else:
            print("Disk Status: Healthy")
