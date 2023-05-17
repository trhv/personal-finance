import pywhatkit

class WhatsupService():
    
    def __init__(self) -> None:
        pass
    
    def send(self):
        pywhatkit.sendwhatmsg('+972542465284', 'Message 666', 17, 45,15, True, 2)
