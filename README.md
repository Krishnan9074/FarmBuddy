## Farmbuddy Application Overview

The Farmbuddy application assists farmers with various tasks related to crops and selling produce. Below is a detailed description of the server's functionality and the protocol used.

### Server Functions

1. **Welcome Message**
   - When a farmer connects to the server, it sends a welcome message to greet the farmer.

2. **Crop Information**
   - The server asks the farmer to specify the crop they need help with (rice, wheat, corn, or sugarcane).
   - Based on the selected crop, the server provides information on cultivation practices, growth requirements, and harvesting techniques.

3. **Crop Links**
   - If additional resources or helpful links are available for the selected crop, the server provides those links for further exploration.

4. **Bill Calculation**
   - The server generates a bill for the selected crop, indicating the amount the farmer needs to pay for accessing the server's services or crop information.

5. **Crop Selling**
   - The server inquires if the farmer wants to sell their crop.
   - If interested, the server prompts the farmer to specify the type of crop they want to sell (rice, wheat, corn, or sugarcane).

6. **Quoted Price**
   - The server provides a quoted price for the selected crop, representing the estimated value at which the server is willing to purchase the crop from the farmer.

7. **Accept or Reject Price**
   - The server asks the farmer if they accept the quoted price.
   - If accepted, the server deducts the price from the total bill.
   - If rejected, the server increases the quoted price by 10 units and adjusts the bill accordingly.

8. **Repeat Selling**
   - After completing a crop selling transaction, the server asks if the farmer wants to sell another crop.
   - If the farmer chooses to continue selling, the process repeats. Otherwise, the server bids farewell and ends the conversation.

### TCP Protocol Details

1. **Connection Establishment**
   - TCP establishes a connection between the farmer (client) and the Farmbuddy server (server) using a three-way handshake to ensure both ends are ready to exchange data.

2. **Reliable Data Transfer**
   - TCP ensures reliable data transfer by breaking the farmer's input and Farmbuddy's responses into packets, assigning sequence numbers, and ensuring correct order and integrity of packets.

3. **Flow Control**
   - TCP implements flow control mechanisms to manage data transmission rates, preventing data overload and ensuring effective processing on both sides.

4. **Congestion Control**
   - TCP handles network congestion by monitoring congestion signs and adjusting the data transmission rate to maintain a stable communication channel.

5. **Connection Termination**
   - TCP performs a four-way handshake to gracefully close the connection, ensuring all pending queries and responses are transmitted and received before termination.

### Summary
