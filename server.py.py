import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('169.254.13.172', 1234))
    server_socket.listen(1)
    
    print("Server is up and running. Listening for connections...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")
        handle_client(client_socket)

def handle_client(client_socket):
    client_socket.send("Welcome to the Farmbuddy! Made by KRISHNAN\n".encode())
    
    crop = client_socket.recv(1024).decode()
    response = get_crop_info(crop)
    client_socket.send(response.encode())
    
    if "information" in response:
        bill = get_bill(crop)
        client_socket.send(str(bill).encode())
        
        sell_choice = client_socket.recv(1024).decode()
        if sell_choice.lower() == "yes":
            crop_type_prompt = "Please enter the crop type (rice, wheat, corn, sugarcane): "
            client_socket.send(crop_type_prompt.encode())
            crop_type = client_socket.recv(1024).decode()
            price = get_quoted_price(crop_type)
            client_socket.send(str(price).encode())
            
            accept_choice = client_socket.recv(1024).decode()
            if accept_choice.lower() == "yes":
                new_bill = reduce_bill(bill)
                client_socket.send(str(new_bill).encode())
            else:
                new_price = increase_price(price)
                client_socket.send(str(new_price).encode())
                new_bill = increase_bill(bill)
                client_socket.send(str(new_bill).encode())
        else:
            client_socket.send("Thank you for visiting. Goodbye!\n".encode())
    
    client_socket.close()

def get_crop_info(crop):
    if crop == "rice":
        return "Here is the information about rice: https://en.wikipedia.org/wiki/Rice"
    elif crop == "wheat":
        return "Here is the information about wheat: https://en.wikipedia.org/wiki/Wheat"
    elif crop == "corn":
        return "Here is the information about corn: https://en.wikipedia.org/wiki/Maize"
    elif crop == "sugarcane":
        return "Here is the information about sugarcane: https://en.wikipedia.org/wiki/Sugarcane"
    else:
        return "Invalid crop. Please select from rice, wheat, corn, or sugarcane."

def get_bill(crop):
    if crop == "rice":
        return 150
    elif crop == "wheat":
        return 160
    elif crop == "corn":
        return 110
    elif crop == "sugarcane":
        return 180

def get_quoted_price(crop_type):
    if crop_type == "rice":
        return 100
    elif crop_type == "wheat":
        return 120
    elif crop_type == "corn":
        return 90
    elif crop_type == "sugarcane":
        return 150

def reduce_bill(bill):
    return bill - 10

def increase_price(price):
    return price + 10

def increase_bill(bill):
    return bill + 10

start_server()
