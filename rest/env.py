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
    subnet
        The subnet to which the docker host server belongs.
        This subnet is required to reach the internet.
        Controllers, API servers, selenium hubs and seleniumi chromes need to
        belong to this subnet.
    gateway
        Docker host subnet gateway.
    cml2_
        Address of CML2 built in your environment.
    api_server
        Address of api_server.
        The API server is automatically deployed as a docker container.
    selenium_hub
        Address of selenium_hub.
        The selenium_hub is automatically deployed as a docker container.
    selenium_chrome01
        Address of selenium_chrome01.
        The sselenium_chrome01 is automatically deployed as a docker container.
    selenium_chrome02
        Address of selenium_chrome02.
        The sselenium_chrome02 is automatically deployed as a docker container.
    breakout_tool
        Address of breakout_tool0.
        The breakout_tool0 is automatically deployed as a docker container.
    controller
        Address of controller.
        The controller is automatically deployed as a docker container.
        This controller provides only minimal functionality.
         1.Stop the existing lab, wipe it, and delete it.
         2.Start lab from the yaml file.
         3.Make it possible to operate the nodes in lab with telnet via
           breakout_tool.
        It is your job to make a controller, so please refer to this form to
        make it.
    phsical_nic
        NIC name of docker host.
    """
    def __init__(self):
        self.my_env = {
            "your_username": "admin",
            "your_password": "Cisco.virl777",
            "cml2_0": "172.16.1.200",
            "tech": "srmpls_xr9k",
            "webex_token": "NzM3ZWFlYTctYjBmOS00NjYzLWFhYjItZjdmZDk0ZjEzYTEzMjFiODlmZWUtNGU5_P0A1_d1374410-57f8-4153-ad37-0e3a54fb2fd1",
            "webex_room": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYTc3MWU1MjAtYmRiZC0xMWViLTlhMDMtMzE5ODM0NjVjZDI0"
        }

