import requests


class LineNotify:
    API_URL = 'https://notify-api.line.me/api/notify'

    def __init__(self, access_token):
        self.__headers = {'Authorization': f'Bearer {access_token}'}

    def send_message(self, message):
        payload = {'message': message}
        r = requests.post(LineNotify.API_URL, headers=self.__headers, params=payload)
        return r.status_code
