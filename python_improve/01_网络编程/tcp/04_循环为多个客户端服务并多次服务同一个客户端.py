import socket


def main():
    # 1. 买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 插入手机卡（绑定本地信息）
    tcp_server_socket.bind(('192.168.1.11', 7890))

    # 3. 将手机设置为响铃状态（让默认的套接字有主动变为被动）
    tcp_server_socket.listen(128)

    while True:
        print("等待一个客户端到来....")
        # 4. 等待别人电话到来（等待客户端的链接）
        client_socket, client_add = tcp_server_socket.accept()

        print("客户段{}到来了".format(client_add))
        while True:
            # 5. 接收客户端发送过来的消息
            rec_data = client_socket.recv(1024)
            print(rec_data.decode("utf-8"))

            # 如果recv_data解堵塞，那么有两种方式：
            # 1. 客户端发送过来数据
            # 2. 客户端调用close，如果tcp客户端调用了close,会发送空信息
            if rec_data:
                # 6. 回送信息
                client_socket.send("OK".encode("utf-8"))
            else:
                break

        # 7. 关闭套接字
        # 仅关闭access返回的客户端的套接字，意味着不再为这个客户端服务
        client_socket.close()
        print("客户端服务完毕")

    # 关闭监听套接字，将不能再次等待新的客户端到来
    tcp_server_socket.close()


if __name__ == '__main__':
    main()