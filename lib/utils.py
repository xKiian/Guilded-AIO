import requests, json, uuid
config = json.load(open('./input/config.json', 'r+'))
class Util:
    def __init__(self, proxy: str= None):
        self.base_url = "https://www.guilded.gg/api"
        self.session = requests.Session()
        self.session.proxies = {"http": proxy, "https": proxy} if proxy else None

    
    def login(self, email: str, password: str): # getting the cookie was inspired from its-vichy c:
        r = self.session.post(f'{self.base_url}/login', json={'email': email, 'password': password, 'getMe': True})
        if 'Email or password is incorrect.' in r.text or r.cookies.get('guilded_mid') == None:
            return False, None
        else:
            return True, {'mid': r.cookies.get('guilded_mid'), 'hmac_signed_session': r.cookies.get('hmac_signed_session')}
    
    def token_login(self, cookie: str):
        self.session.cookies.set('hmac_signed_session', cookie)

    def join_server(self, invite_code: str):
        r = self.session.put(f'{self.base_url}/invites/{invite_code}', json={"type":"consume"})
        return r

    def set_activity(self, number: int = 1):
        r = self.session.post(f'{self.base_url}/users/me/presence', json={'status': number})
        return r

    def set_status(self, status: str):
        r = self.session.post(f'{self.base_url}/users/me/status', json={"content":{"object":"value","document":{"object":"document","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":status,"marks":[]}]}]}]}},"customReactionId":90000094,"expireInMs":0})
        return r

    def ping(self):
        self.session.get(f'{self.base_url}/users/me/ping')

    def set_pfp(self, pfp: str):
        r = self.session.post(f'{self.base_url}/users/me/profile/images', json={'imageUrl': pfp})
        return r

    def send_message(self, channel_id: str, message: str):
        r = self.session.post(f'{self.base_url}/channels/{channel_id}/messages', json={
            "messageId": str(uuid.uuid1()),"content": {"object": "value","document": {"object": "document","data": {},"nodes": [{"object": "block","type": "paragraph","data": {},"nodes": [{"object": "text","leaves": [{"object": "leaf","text": message,"marks": []}]}]}]}},
            "repliesToIds": False,
            "confirmed": False,
            "isSilent": False,
            "isPrivate": False
        })
        return r