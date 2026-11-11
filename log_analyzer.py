
from pathlib import Path


class LogAnalyzer:

    @staticmethod
    def run(directory):

        path = Path(directory)

        if not path.is_dir():
            raise ValueError("Invalid log directory")

        errors = 0
        warnings = 0
        info = 0

        print("\n===== LOG ANALYSIS =====")

        for log_file in path.glob("*.log"):

            print(f"\nAnalyzing: {log_file.name}")

            with log_file.open(
                "r",
                encoding="utf-8",
                errors="replace"
            ) as file:

                for line in file:

                    text = line.upper()

                    if "ERROR" in text:
                        errors += 1

                    elif "WARNING" in text or "WARN" in text:
                        warnings += 1

                    elif "INFO" in text:
                        info += 1

        print("\n===== SUMMARY =====")
        print("Errors:", errors)
        print("Warnings:", warnings)
        print("Info:", info)
