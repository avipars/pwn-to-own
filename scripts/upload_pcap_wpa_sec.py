# Script to bulk upload pcap files to wpa-sec from your desktop computer
import os
import requests
import time 

class WpaSecUploader:
    def __init__(self, api_url, api_key):
        """
        Initialize the uploader with API URL and API key.
        """
        self.api_url = api_url
        self.api_key = api_key

    def upload_to_wpasec(self, file_path, timeout=30):
        """
        Uploads a .pcap file to the specified WPA-SEC endpoint.
        
        :param file_path: Path to the .pcap file to be uploaded.
        :param timeout: Request timeout in seconds.
        :return: Response object from the server.
        """
        try:
            with open(file_path, 'rb') as file_to_upload:
                cookies = {'key': self.api_key}
                files = {'file': file_to_upload}
                
                response = requests.post(
                    self.api_url,
                    cookies=cookies,
                    files=files,
                    timeout=timeout
                )
                response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

                if 'already submitted' in response.text:
                    print(f"File {file_path} was already submitted.")
                else:
                    print(f"File {file_path} uploaded successfully." )

                return response

        except FileNotFoundError:
            print(f"File {file_path} not found." )
            raise
        except requests.exceptions.RequestException as e:
            print(f"Failed to upload file {file_path}: {e}" )
            raise
    
def upload_pcap_files_in_directory(directory_path, api_url, api_key, whitelist_file, sleep_time=5):
    """
    Uploads all .pcap files in the specified directory to the WPA-SEC endpoint.
    
    :param directory_path: Path to the directory containing .pcap files.
    :param api_url: URL of the WPA-SEC API endpoint.
    :param api_key: API key for authentication.
    """
    uploader = WpaSecUploader(api_url, api_key)

    if not os.path.isdir(directory_path):
        print(f"Directory {directory_path} does not exist.")
        return
    
    # Get all .pcap files in the directory
    pcap_files = [f for f in os.listdir(directory_path) if f.endswith('.pcap')]
    
    if not pcap_files:
        print(f"No .pcap files found in directory {directory_path}.")
        return

    print(f"Found {len(pcap_files)} .pcap files in directory {directory_path}.")
    
    for pcap_file in pcap_files:
        file_path = os.path.join(directory_path, pcap_file)        
    
        print(f"Uploading file: {file_path}", )
        
        try:
            response = uploader.upload_to_wpasec(file_path)
            print(f"Server response: {response.text}")
        except Exception as e:
            print(f"Failed to upload {file_path}: {e}")
        
        print(f"Waiting for {sleep_time} seconds")
        time.sleep(sleep_time)
if __name__ == "__main__":
    # Configuration
    API_URL = "https://wpa-sec.stanev.org"
    API_KEY = "YOUR_KEY"
    DIRECTORY_PATH = r"C:\temp\pcaps"

    WHITELIST_FILE = r"C:\temp\whitelist.txt"

    # Upload all .pcap files in the directory
    upload_pcap_files_in_directory(DIRECTORY_PATH, API_URL, API_KEY,WHITELIST_FILE, 2)
