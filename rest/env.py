#!user/bin/python

class MyEnv:
    """
    Define variables for your environment.

    key
    ---
    your_username:
        Username with administrator privileges for cml2 rest API.
    your_password:
        Password for "your_username".
    cml2_0
        Address of CML2 built in your environment.
    """
    def __init__(self):
        self.my_env = {
            "your_username": "admin",
            "your_password": "admin_password",
            "cml2_0": "172.16.1.200",
            "tech": "simple_network",
            "webex_token": "token of webex bot",
            "webex_room": "token of webex room"
        }
