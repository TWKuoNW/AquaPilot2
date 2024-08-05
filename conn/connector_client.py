# 測試用，未來會刪掉
import socket
import threading
import time

class Connector(threading.Thread): # 建立一個連接器的class
    def __init__(self, host, port):  # 初始化Thread的設定，接收兩個參數(ip, port)
        super().__init__()
        self.host = host 
        self.port = port 
        # 創建一個socket物件，其中 socket.AF_INET 代表使用 IPv4 地址族；SOCK_STREAM 則代表使用 TCP 傳輸，若想使用 UDP 則宣告成 SOCK_DGRAM。
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.settimeout(3) # 判定十秒為超時連線
        self.client_socket.setblocking(1)
        self.client_socket.connect((host, port)) # 連接伺服器
        threading.Thread(target = self.listener, daemon = True).start()

    def transmitter(self, msg): # 執行續啟動後會啟動該function
        self.client_socket.send(msg.encode('utf-8'))
    
    def listener(self): # 監聽器
        try:
            while(True):
                msg = self.client_socket.recv(1024).decode('utf-8') # 接收客戶端發來的訊息
                if(msg != ""):
                    print("收到:", msg)
                
                time.sleep(1)
        except Exception as e:
            print(f"接收區 發生錯誤:{e}")
            print("關閉客戶端連線")
            self.client_socket.close()
            print("連線結束")
     
    

# 使用示例
if __name__ == "__main__":
    host = "100.81.241.109"
    port = 9999
    connector = Connector(host, port)
    
    while(True):
        msg = input("請輸入要傳送的訊息: ")
        if(msg == "EXIT"):
            break
        connector.transmitter(msg)
        
    
    print("Done.")
    
