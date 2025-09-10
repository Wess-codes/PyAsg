import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_image():
    url = input("🌐 Enter the image URL: ").strip()

    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  


        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)


        if not filename or '.' not in filename:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"image_{timestamp}.jpg"


        image_path = os.path.join(folder_name, filename)
        with open(image_path, "wb") as file:
            file.write(response.content)

        print(f"✅ Image saved as '{filename}' in '{folder_name}'.")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Failed to fetch image: {e}")
        print("🙏 Respecting the web—some connections may not succeed.")

if __name__ == "__main__":
    fetch_image()
