import socket

def is_socket_connected(socket):
    try:
        # 發送一個非阻塞的零字節消息
        socket.sendall(b'\0')
    except Exception as e:
        return False  # 未連接
    return True  # 仍然連接

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(10) # 判定十秒為超時連線
client_socket.connect(("100.81.241.109", 9999)) # 連接伺服器

while(True):
    try:
        if(is_socket_connected(client_socket) != True):
            print("Socket disconnected.")
            break

        command = input("Enter command: ")
        client_socket.sendall(command.encode('utf-8'))
        
        if(command == "EXIT"):
            #break
            pass
    except Exception as e:
        print(f"Error: {e}")
        client_socket.sendall("EXIT".encode('utf-8'))
        break