def params():
    return {
        "url": "https://example.com",
        "username": "your_username",
        "password": "your_password",
        "email": "your_email@example.com",
        
        "browser": "chromium", # or "firefox", "webkit"
        "headless": True, # debug - show browser
        "viewport": {"width": 1280, "height": 720},
        "console": False, # debug - show console logs
    }