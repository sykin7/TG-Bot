import os
ADMIN_IDS = [int(x) for x in os.environ.get("ADMIN_IDS", "").split(",") if x]

def is_admin(user_id: int):
    return user_id in ADMIN_IDS

def is_safe_file(filename: str):
    allowed_ext = [".txt", ".pdf", ".jpg", ".png", ".mp3", ".ogg"]
    return any(filename.lower().endswith(ext) for ext in allowed_ext)
