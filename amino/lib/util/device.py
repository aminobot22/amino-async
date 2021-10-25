import json
from .helpers import generate_device_info

class DeviceGenerator:
    def __init__(self, deviceId ="22C238D43575D538070F4D9794CFA2968235D18929869E747B17A5F2735EC6E2E74F5962662B8A861C"):
        try:
            with open("device.json", "r") as stream:
                data = json.load(stream)
                self.user_agent = data["user_agent"]

                if deviceId:
                    self.device_id = deviceId
                else:
                    self.device_id = data["device_id"]

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            device = generate_device_info()
            with open("device.json", "w") as stream:
                json.dump(device, stream, indent=4)

            with open("device.json", "r") as stream:
                data = json.load(stream)
                self.user_agent = data["user_agent"]

                if deviceId:
                    self.device_id = deviceId
                else:
                    self.device_id = data["device_id"]
