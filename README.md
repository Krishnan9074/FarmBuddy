# FarmBuddy
The Farmbuddy application is designed to assist farmers with various tasksrelated to crops and selling produce. Here's an overview of what the server
does:
Welcome Message: When a farmer connects to the server, it sends awelcome message to greet the farmer.
Crop Information: The server asks the farmer to specify the crop they needhelp with (rice, wheat, corn, or sugarcane). Based on the crop selected, theserver provides information about the crop, such as cultivation practices,
growth requirements, and harvesting techniques.
Crop Links: If there are additional resources or helpful links related to theselected crop, the server provides the farmer with those links. The links canbe accessed by the farmer to explore more detailed information about thecrop.
Bill Calculation: The server generates a bill for the selected crop, indicatingthe amount the farmer needs to pay for availing the server's services or
accessing the crop information.
Crop Selling: The server asks the farmer if they want to sell their crop. If thefarmer is interested, the server prompts the farmer to specify the type of cropthey want to sell (rice, wheat, corn, or sugarcane).
Quoted Price: Based on the selected crop type, the server provides the farmerwith a quoted price for their crop. This price represents the estimated value at
which the server is willing to purchase the crop from the farmer.
Accept or Reject Price: The server asks the farmer if they accept the quotedprice. If the farmer accepts, the server deducts the price from the total bill,
indicating the reduced amount the farmer needs to pay. If the farmer rejects,
the server increases the quoted price by 10 units and adjusts the bill
accordingly.
Repeat Selling: After completing a crop selling transaction, the server asksthe farmer if they want to sell another crop. If the farmer chooses to continueselling, the process repeats. Otherwise, the server bids farewell and ends theconversation.
The Farmer server aims to provide helpful information about crops, assist
farmers in selling their produce, and manage billing based on the servicesrendered.
PROTOCOL USED:
TCP
Connection Establishment: TCP establishes a connection between the farmerfarmbuddy (client) and the farmbuddy server (server) using a three-wayhandshake. This process ensures that both ends are ready to exchange dataand establishes a reliable connection for communication between the farmerand the farmbuddy.
Reliable Data Transfer: TCP ensures reliable data transfer by breaking thefarmer's input and farmbuddy responses into packets, assigning sequencenumbers to each packet, and ensuring that all packets are received correctlyand in the correct order. This guarantees that the farmer's queries and thefarmbuddy's responses are transmitted accurately, minimizing data loss or
corruption during transmission.
Flow Control: TCP implements flow control mechanisms to manage the rate of
data transmission between the farmer and the farmbuddy server. It regulatesthe pace at which the farmer can send queries and receive responses fromthe farmbuddy, preventing data overload and ensuring that both sides canprocess the information effectively.
Congestion Control: TCP includes congestion control mechanisms to handlenetwork congestion. In the farmer farmbuddy application, TCP monitors thenetwork for congestion signs and adjusts the data transmission rateaccordingly. This prevents the farmer's queries and the farmbuddy'sresponses from overwhelming the network, maintaining a stable and efficient
communication channel.
Connection Termination: When the farmer is finished interacting with thefarmbuddy, TCP performs a connection termination process to gracefullyclose the connection. This involves a four-way handshake to ensure that all
pending queries and responses are transmitted and received beforeterminating the connection. It ensures that no data is lost or left incompleteduring the termination process.
In summary, TCP ensures that the farmer's queries and the farmbuddy'sresponses in the farmer farmbuddy application are transmitted reliably, inorder, and without errors. It establishes and terminates connections, manages
data flow to prevent overload, and handles network congestion to provide asmooth and efficient communication experience between the farmer and thefarmbuddy server
