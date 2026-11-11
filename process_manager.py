
import subprocess
import platform


class ProcessManager:

    @staticmethod
    def run():

        print("\n===== RUNNING PROCESSES =====")

        system = platform.system()

        if system == "Windows":
            command = ["tasklist"]

        elif system in ["Linux", "Darwin"]:
            command = ["ps", "-eo", "pid,comm,%cpu,%mem"]

        else:
            print("Unsupported operating system")
            return

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(result.stdout)
        else:
            print(result.stderr)
