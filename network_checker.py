
import socket


class NetworkChecker:

    @staticmethod
    def run():

        print("\n===== NETWORK CONNECTIVITY =====")

        hosts = [
            "google.com",
            "github.com",
            "aws.amazon.com"
        ]

        for host in hosts:

            try:

                ip = socket.gethostbyname(host)

                print(f"{host}: REACHABLE ({ip})")

            except socket.gaierror:

                print(f"{host}: UNREACHABLE")
