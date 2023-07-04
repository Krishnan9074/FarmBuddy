import socket
import tkinter as tk
from tkinter import messagebox, simpledialog

def connect_to_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 1234))
    
    response = server_socket.recv(1024).decode()
    chat_log.insert(tk.END, response + "\n")
    
    crop = crop_entry.get()
    server_socket.send(crop.encode())
    
    response = server_socket.recv(1024).decode()
    chat_log.insert(tk.END, response + "\n")
    
    if "information" in response:
        bill = int(server_socket.recv(1024).decode())
        chat_log.insert(tk.END, f"The bill for {crop} is {bill}\n")
        
        sell_choice = messagebox.askquestion("Crop Selling", "Do you want to sell your crop?")
        server_socket.send(sell_choice.encode())
        
        if sell_choice.lower() == "yes":
            crop_type_prompt = server_socket.recv(1024).decode()
            crop_type = simpledialog.askstring("Crop Type", crop_type_prompt)
            server_socket.send(crop_type.encode())
            
            price = int(server_socket.recv(1024).decode())
            chat_log.insert(tk.END, f"The quoted price for {crop_type} is {price}\n")
            
            accept_choice = messagebox.askquestion("Accept Price", "Do you accept the price?")
            server_socket.send(accept_choice.encode())
            
            if accept_choice.lower() == "yes":
                new_bill = int(server_socket.recv(1024).decode())
                chat_log.insert(tk.END, f"The new bill after reducing the price is {new_bill}\n")
                chat_log.insert(tk.END, "Thank you for visiting! Goodbye\n")
            else:
                new_price = int(server_socket.recv(1024).decode())
                chat_log.insert(tk.END, f"The new price after increasing is {new_price}\n")
                new_bill = int(server_socket.recv(1024).decode())
                chat_log.insert(tk.END, f"The new bill after increasing the price is {new_bill}\n")
                chat_log.insert(tk.END, "Thank you for visiting! Goodbye\n")
        else:
            response = server_socket.recv(1024).decode()
            chat_log.insert(tk.END, response + "\n")
    
    server_socket.close()

# Create the main window
window = tk.Tk()
window.title("Farmbuddy")
window.geometry("400x500")
window.configure(bg="#F0F0F0")


# Create chat log
chat_log = tk.Text(window, height=25, width=50)
chat_log.pack()

# Create crop entry
crop_entry = tk.Entry(window, width=30)
crop_entry.pack()

# Create connect button
connect_button = tk.Button(window, text="Connect", command=connect_to_server)
connect_button.pack()

# Start the GUI event loop
window.mainloop()
