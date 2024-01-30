import socket


if __name__ == '__main__':
   target = input("Host's port to be scanned : ")
   ip = socket.gethostbyname(target)
   print(f"Start port's scan on {ip}")

   for i in range(0, 1023):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      conn = s.connect_ex((ip, i))

      if(conn == 0) :
         print (f"Port {i} is OPEN !")

      s.close()
