from pathlib import Path
import os

class VideoSharing:
    def __init__(self):
        self.folder = "uploads/videos"
        Path(self.folder).mkdir(parents=True, exist_ok=True)
        self.allowed = {'.mp4', '.avi', '.mov', '.mkv'}
        self.max_size = 100 * 1024 * 1024  # 100MB
    
    def save_video(self, file, user_id):
        """Save video and return filename"""
        if Path(file.filename).suffix.lower() not in self.allowed:
            return None
        
        filename = f"{user_id}_{file.filename}"
        filepath = os.path.join(self.folder, filename)
        file.save(filepath)
        
        return filename
    
    def get_video(self, filename):
        """Get video filepath"""
        filepath = os.path.join(self.folder, filename)
        return filepath if os.path.exists(filepath) else None