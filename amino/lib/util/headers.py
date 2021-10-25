from amino.lib.util import device

sid = None

class Headers:
    def __init__(self, data = None, type = None, deviceId: str = None, sig: str = None):
        if deviceId:
            dev = device.DeviceGenerator(deviceId=deviceId)
        else:
            dev = "22C238D43575D538070F4D9794CFA2968235D18929869E747B17A5F2735EC6E2E74F5962662B8A861C"

        headers = {
            "NDCDEVICEID": dev.device_id,
           
            "Accept-Language": "en-US",
            
        }

        if data: headers["Content-Length"] = str(len(data))
        if sid: headers["NDCAUTH"] = f"sid={sid}"
        if type: headers["Content-Type"] = type
        if sig: headers["NDC-MSG-SIG"] = sig
        self.headers = headers
