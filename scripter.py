import hashlib
import json
import socket
import time


class Scripter:

    local_host_id=""
    def __init__(self):
        self.account=""

        self.init_id()

    def init_id(self):
        data=self.load("localhost.json")

        if "local_host_id" in data:
            Scripter.local_host_id=data["local_host_id"]
        
        # initialize local_host_id with host name and time 
        else:
            name = socket.gethostname().encode("utf-8")
            instant_time = time.asctime().encode("utf-8")

            m = hashlib.md5()
            m.update(name+instant_time)
            data["local_host_id"]= m.hexdigest()
            Scripter.local_host_id=data["local_host_id"]
        
        self.dump("localhost.json", data)

    def load(self, filename):
        file=open(filename)
        contents=file.read()
        if len(contents) == 0:
            data = {}
            return data
            
        # make sure that contents is not null
        data = json.loads(contents)
        file.close()
        return data
            

    def dump(self, filename, json_data):
        file=open(filename, mode='r+')
        data = json.dumps(json_data)
        file.write(data)
        file.close()
