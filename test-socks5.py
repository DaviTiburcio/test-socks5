import requests #instalar a biblioteca no terminal com o comando "pip install requests[socks]"

def check_fast_proxy(proxy_d):
    Timeout = 10
    url = "https://ifconfig.me/ip"
    
    socks_proxy = "socks5://" + proxy_d
    proxy = {"http": socks_proxy, "https": socks_proxy}
    
    try:
        req = requests.get(url, proxies=proxy, timeout=Timeout)
        if req.status_code == 200:
            print(socks_proxy, "is live and fast")
    except requests.exceptions.Timeout:
        print(socks_proxy, "timeout")
    except Exception as e:
        print(socks_proxy, "erro fi")

def read_data_from_file(filename):
    read_file = open(filename, 'r')
    file_data = read_file.readlines()
    read_file.close()
    
    for line in file_data:
        line = line.strip()
        check_fast_proxy(line)

if __name__ == "__main__":
    file = r"" #substituir para a localidade do socks5.txt instalado
    read_data_from_file(file)
    
    
