
# It is created for preparing the API response.
def send_response(code, msg, data):
    dictionary01 = {}
    dictionary01['status_code'] = code
    dictionary01['status'] = msg
    dictionary01['data'] = data
    return dictionary01