

import socket
import threading


print("""
                                                                                                
                                             .   ..''.                                              
                                           ',.  .,:dK0o'                                            
                                         .;;.    'lOWMWKl.                                          
                                         ;;   ..'ld0WMMMNo.                                         
                                        ,c.  .';cdkOKNWWMNl                                         
                                       .xx;'''''',,,;lxXWMX:                                        
                                      .l0kc,'..        .ckX0:                                       
                                     .xd,                 ,kKl                                      
                                     l0;                   ,Ol.                                     
                                     .ox;                 'oo.                                      
                                   ,lokNXo.             .lKNKkdc,                                   
                                 .lOo;;xkOd'           .oxoodxKWXd.                                 
                                .l0c    ..,;.         .''    .loo0x.                                
                              .cxl,.                         .'. ;0d.                               
                             ;xx;                                 cK0x'                             
                           .oKk;    .cccc::cc:::::::::::::;;;:c,  .coOOc.                           
                         .,dXOc.    ;o,...................   .c;     'kNO'                          
                        ;ONWNx,     ':.                       ;,     .lKNo                          
                       ,dxddxxlcc,. .,.        .',,'.         '.   ..;dKXOl,.                       
                            ...;;'. .'.        :OXKO;         .. .'cdkKOl,...                       
                                     ..        .;cc;.         .      ....                                 
""")


# Ağdaki IP aralığını belirleyin (Örn: 192.168.1.0/24 için "192.168.1.")
network_prefix = "192.168.1."

# Taranacak port aralığını belirleyin (Örn: 1-65535)
port_range = range(1, 1025)

# Açık portları saklamak için liste
open_ports = []

# Belirli bir IP adresinde portları kontrol eden fonksiyon
def scan_ports(ip):
    for port in port_range:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Her bağlantı için zaman aşımı süresi
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append((ip, port))
                print(f"[+] {ip}:{port} açık")

# Ağdaki cihazları tarayan fonksiyon
def scan_network():
    threads = []
    for i in range(1, 255):  # 192.168.1.1 - 192.168.1.254
        ip = f"{network_prefix}{i}"
        t = threading.Thread(target=scan_ports, args=(ip,))
        threads.append(t)
        t.start()

    # Tüm thread'lerin bitmesini bekle
    for t in threads:
        t.join()

    # Tarama sonuçları
    print("\nAçık Portlar:")
    for ip, port in open_ports:
        print(f"{ip}:{port}")

# Tarama başlat
if __name__ == "__main__":
    scan_network()

