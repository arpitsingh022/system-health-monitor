
import argparse

from system_monitor import SystemMonitor
from file_manager import FileManager
from log_analyzer import LogAnalyzer
from process_manager import ProcessManager
from network_checker import NetworkChecker


def main():

    parser = argparse.ArgumentParser(
        description="Python DevOps Automation Toolkit"
    )

    parser.add_argument(
        "task",
        choices=[
            "system",
            "files",
            "logs",
            "processes",
            "network"
        ],
        help="Select automation task"
    )

    parser.add_argument(
        "--path",
        default=".",
        help="File or log directory"
    )

    args = parser.parse_args()

    if args.task == "system":
        SystemMonitor.run()

    elif args.task == "files":
        FileManager.run(args.path)

    elif args.task == "logs":
        LogAnalyzer.run(args.path)

    elif args.task == "processes":
        ProcessManager.run()

    elif args.task == "network":
        NetworkChecker.run()


if __name__ == "__main__":
    main()
