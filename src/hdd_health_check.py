def parse_smart_output(output):

    health = {
        "overall_health": "UNKNOWN",
        "temperature": None,
        "reallocated_sectors": None,
        "power_on_hours": None
    }

    for line in output.splitlines():

        # Overall health PASS/FAIL
        if "SMART overall-health self-assessment" in line:
            if "PASSED" in line:
                health["overall_health"] = "PASS"
            else:
                health["overall_health"] = "FAIL"

        # Temperature
        if "Temperature_Celsius" in line:
            try:
                health["temperature"] = int(line.split()[-1])
            except:
                pass

        # Reallocated sector count
        if "Reallocated_Sector_Ct" in line:
            try:
                health["reallocated_sectors"] = int(line.split()[-1])
            except:
                pass

        # Power on hours
        if "Power_On_Hours" in line:
            try:
                health["power_on_hours"] = int(line.split()[-1])
            except:
                pass

    return health
