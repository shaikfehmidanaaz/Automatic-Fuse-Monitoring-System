class AutomaticFuseMonitoringSystem:
    def __init__(self, rated_current):
        self.rated_current = rated_current
        self.current = 0
        self.fuse_status = "GOOD"

    def measure_current(self, current):
        self.current = current

    def check_fuse(self):
        print("\n----- FUSE MONITORING -----")
        print(f"Rated Fuse Current : {self.rated_current:.2f} A")
        print(f"Measured Current   : {self.current:.2f} A")

        if self.current == 0:
            self.fuse_status = "BLOWN"

            print("\nFUSE FAULT DETECTED!")
            print("Fuse Status : BLOWN")
            print("Alert       : ON")
            print("Load        : DISCONNECTED")

        elif self.current > self.rated_current:
            self.fuse_status = "OVERLOAD"

            print("\nWARNING: OVERLOAD CONDITION!")
            print("Fuse Status : AT RISK")
            print("Alert       : ON")

        else:
            self.fuse_status = "GOOD"

            print("\nSYSTEM STATUS: NORMAL")
            print("Fuse Status : GOOD")
            print("Alert       : OFF")
            print("Load        : CONNECTED")

    def display_status(self):
        print("\n----- FINAL STATUS -----")
        print(f"Fuse Status : {self.fuse_status}")


def main():
    print("======================================")
    print("    AUTOMATIC FUSE MONITORING SYSTEM")
    print("======================================")

    try:
        rated_current = float(
            input("\nEnter fuse rated current (A): ")
        )

        measured_current = float(
            input("Enter measured circuit current (A): ")
        )

        if rated_current <= 0 or measured_current < 0:
            print("Invalid input!")
            return

        system = AutomaticFuseMonitoringSystem(rated_current)

        system.measure_current(measured_current)
        system.check_fuse()
        system.display_status()

    except ValueError:
        print("Please enter valid numerical values.")


if __name__ == "__main__":
    main()
