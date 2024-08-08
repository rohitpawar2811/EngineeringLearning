# AWS

##  Aws Services

- AWS EC2 Elastic Cloud Compute Services
- AWs Lambda: aws service which runs the code with serverless model and it is stateless in nature but with aws rds or mongodb we can provide the state.

	- It is scallable reliable fast, provides the pre-integration for all most all aws services.
	- Provides support with s3, RDS, Mongodb.
	- Event-Driven: It can be triggerd based on the events happend in s3(recived a file), api-gateway certain request recieved.
	- Billing: you will only charged for compute time of code and rest of the not charged.
	- Intially it was providing the charging time about 5min and after that it moved to 15 min.

- AWS S3 : File storage for all types of formate.
- Aws SNS : simple notification service which is managed messaging service. It is designed to distribute notification to wide range of reciepients. With SNS you can send message to individual
reciepients or to large number of recipients.
	- Pub/Sub Messaging : topic, pub -subscriber policy
	- Multiple Protocols : Http, Email, SMS ,Aws Lambda, Simple Queue service(SQS), 					Application Endpoint 
	- Flexibility
	- Durability
	
Recievers can be : Lambda, SQS, Email.

## Aws SQS

AWs SQS provides the Queue based communication support over the multi-microservices, Distributed-system, serverless application etc.

- Managed by Aws
- Durability 



## Polling 
Long Polling: Reduces unnecessary network traffic with empty responses by waiting until a message is available in the
queue before sending a response.


Short Polling: This involves frequent and regular requests from the client to the server to check for updates. If no updates are available, the server responds with an empty or null response.

Long Polling: As mentioned earlier, this technique keeps the connection open until new data is available. It reduces the frequency of requests and allows the server to push updates to the client as soon as they are available.

WebSocket: Unlike traditional HTTP polling, WebSocket provides a full-duplex communication channel over a single, long-lived connection. This allows for real-time, low-latency communication between the client and server.

Server-Sent Events (SSE): SSE is a standard allowing servers to push data to clients over HTTP connections. It's particularly useful for applications that require real-time updates from the server, such as live feeds or notifications.

Interval Polling: This involves periodic polling at fixed intervals. The client makes requests to the server at regular time intervals to check for updates.


Event-Driven: Webhooks are triggered by specific events or actions, such as a new message, a payment received, or a status change. When the event occurs, the server sends an HTTP POST request to a URL (endpoint) specified by the client.
