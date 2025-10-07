from .local_parameters import params

parameters = None

def get_parameters():
    return parameters

def load_parameters():
    global parameters
    try: 
        from configuration.local_parameters import params
        parameters = params()
    except ImportError:
        # Set to default
        parameters = dict()
        parameters["url"] = "https://example.com"
        parameters["username"] = "your_username"
        parameters["password"] = "your_password"
        parameters["email"] = "your_email@example.com"

        parameters["browser"] = "chromium" # or "firefox", "webkit"
        parameters["headless"] = True # debug - show browser
        parameters["viewport"] = {"width": 1280, "height": 720}
        parameters["console"] = False # debug - show console logs