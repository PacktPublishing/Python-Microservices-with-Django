
class RespSender(object):

    def __init__(self):
        self.resplist = []
        self.respdict = {}

    def send_response(self, code, msg, data):
        self.respdict["status"] = code
        self.respdict["message"] = msg
        self.respdict["data"] = data
        self.resplist.append(self.respdict)
        return self.resplist