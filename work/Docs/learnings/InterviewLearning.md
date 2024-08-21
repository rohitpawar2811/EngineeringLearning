## 𝟴 𝗟𝗼𝗮𝗱 𝗕𝗮𝗹𝗮𝗻𝗰𝗶𝗻𝗴 𝗔𝗹𝗴𝗼𝗿𝗶𝘁𝗵𝗺𝘀 𝗬𝗼𝘂 𝗦𝗵𝗼𝘂𝗹𝗱 𝗞𝗻𝗼𝘄:


𝟬.💡 𝗥𝗼𝘂𝗻𝗱 𝗥𝗼𝗯𝗶𝗻: 
It sends each new request to the next server in line, like taking turns.
➡️ Useful when: You have servers with similar capabilities and want to spread the load evenly.

𝟭.💡 𝗟𝗲𝗮𝘀𝘁 𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻𝘀:
It sends new requests to the server handling the fewest tasks right now.
➡️ Useful when: Your servers have different processing speeds or some tasks take longer than others.

𝟮.💡 𝗪𝗲𝗶𝗴𝗵𝘁𝗲𝗱 𝗥𝗼𝘂𝗻𝗱 𝗥𝗼𝗯𝗶𝗻:
It gives more work to stronger servers and less to weaker ones, but still takes turns.
➡️ Useful when: You have a mix of powerful and less powerful servers in your system.

𝟯.💡 𝗪𝗲𝗶𝗴𝗵𝘁𝗲𝗱 𝗟𝗲𝗮𝘀𝘁 𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻𝘀: 
It considers both how busy each server is and how strong it is when assigning new tasks.
➡️ Useful when: You have servers with different strengths and want to balance their workload efficiently.

𝟰.💡 𝗜𝗣 𝗛𝗮𝘀𝗵: 
It always sends requests from the same user to the same server.
➡️ Useful when: Users need to stay connected to the same server for their entire session, like in online shopping.

𝟱.💡 𝗟𝗲𝗮𝘀𝘁 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 𝗧𝗶𝗺𝗲: 
It chooses the server that's both quick to respond and not too busy.
➡️ Useful when: Speed is crucial, and you want to provide the fastest possible service to users.

𝟲.💡 𝗥𝗮𝗻𝗱𝗼𝗺: 
It picks a server at random for each new request.
➡️ Useful when: You want a simple way to distribute tasks and your servers are all similar in capability.

𝟳.💡 𝗟𝗲𝗮𝘀𝘁 𝗕𝗮𝗻𝗱𝘄𝗶𝗱𝘁𝗵: 
It sends new tasks to the server using the least amount of internet capacity at the moment.
➡️ Useful when: Your main concern is network traffic, and you want to avoid 
overloading any single server's connection.


## Solid Principles

1.Single Responsibility Design Pattern : A  class should have only one reason to change, meaning it should have only one job responsibility.

2. Open/Closed
3. Liskov Substitution
4. Interface Segregation
5. Dependency Inversion

Design Principle of Rest API

1. Statelessness : The Data transfered from the client to the server must contains the all information needed to understand and process the request.

2. Client-Server Architecture : The client and server should be able to evolve sepratly

3. Right Rest Method used while communicating.

4. Proper Authentication and Authorization for Rest-Based calls to secure our data.

5. ProperResponseCode It is must. For success and failure scenerious both. 

6. Internationalization : For providing the data in user-local.

7. Cacheability: Response must define themselves as cacheable or not to prevent the client from reusing stale or inappropriate data.

DRY (Don't REpeat Yourself) : Avoid duplication of code by abstracting and reusing pieces of logic.

Yagni (You are not gonna need it) : Do not add functinality untill it is not needed.

Kiss (keep it simple, stupid) : Keep the design and code as simple as possible, Don't add the unnessary functionality.

## Event-Driven Design Pattern : 
 LMAI
Definition: The flow of the program is determined by events such as user actions, sensor outputs, or messages from other programs.


## Databases Concept that would I can Highligt and we can talk about it.

Joins
Subqueries
Window functions
Indexing
Partitioning : I don't know about it and it is possibel in mysql it is itself an questions now.
Normalization: The process of organizing data in the database to reduce redundancy and improve data integrity.
Sharding




## Java Basics:


1. Multithreading

Definition: A feature that allows concurrent execution of two or more threads for maximum utilization of CPU.
Example: Extending Thread class or implementing Runnable interface.

2. Creating a lock for synchronization over the method

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class MyLock {
    private final Lock lock = new ReentrantLock();

    public void doSomething() {
        lock.lock();
        try {
            // critical section
        } finally {
            lock.unlock();
        }
    }
}

Or we can cover the piece of code in the certain block of code.

3. Character Count Using Java8
Example: Using streams to count character occurrences in a string.



public class CharacterCount {
    public static void main(String[] args) {
        String input = "example";
        Map<Character, Long> charCount = input.chars()
            .mapToObj(c -> (char) c)
            .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        System.out.println(charCount);
    }
}


## Microservice Components

1. Service Registry and Discovery
Definition: Mechanism to dynamically register and locate services.
Example: Using Eureka for service registry and discovery in a Spring Boot application.
2. API Gateway
Definition: A server that acts as an API front-end, handling requests, routing them to appropriate services, and aggregating results.
Example: Using Zuul or Spring Cloud Gateway.


## Design Patterns: 
1. Singleton : In this design pattern generally we want the single Instance of class generated and served to all dependent class. Exmple: like database connection,  SFTP, FileIO, Session

2. Facade : 
3. Observer :
4. CQRS (Command Query Responsibility Segragation) : 
Separating read and write operations for better scalability and performance.

5. Saga  : this pattern generally used in microservices.
-  It is used to manging the distributed transaction by breaking them into a series of smaller transactions that can be coordinated and completed independently.

Example: Implementing a saga orchestrator to manage the sequence of events.

6. Factory Method

--------------------------------------------------------------------------------
## Microservice Communications

Synchronous Communication
Definition: In synchronous communication, the client waits for the server to respond before proceeding with the next step. This is typically done using HTTP/REST or gRPC.

// Using RestTemplate in Spring Boot for synchronous communication
@RestController
public class MyController {
    @Autowired
    private RestTemplate restTemplate;

    @GetMapping("/sync-call")
    public String makeSyncCall() {
        String response = restTemplate.getForObject("http://example.com/api", String.class);
        return response;
    }
}



Technical Interview

1. Your Projects : SpringBoot , Apache-Solr, Apache-Kafka, SQL, AWS-Services  
2. There Need: Spring, Spring-Boot, Java, Apache-KAFKA streming, Sql
EKS, Kubernetes

















1. performance and security of MS. kubernetes, aws, kafka, system design, component design.
2. What is JDK JRE and JVM? And the difference?


0

▼
Answer: I would make recommendations where I could, and I would if allowed, create a timeline to manage the process with a curvy approach for delivery, rather than a straight one, to avoid a repetitive and unproductive process, and ensure that I write something new or different every day while meeting the conditions set by the content strategy.


core java concepts, cloud computing, microservices. What I liked more about this round was that the panel member was more interested in understanding my logic and thought process behind attempting a problem and not very keen on arriving at just the right answer. My second round was probably with a tech lead who focused more on architecture and design patterns. It seemed like a techno managerial round. Third round was finally with the HR Manager which was more of an interaction and less of an interview. I enjoyed this discussion thoroughly and this was because of the candid way in which the HR provided insights which were never known to me. One thing I can be sure of that this place has a lot of smart people and it will be fun working here.


https://www.linkedin.com/in/aseem-agrawal-aa1279a8/
1. aseem.agrawal@perennialsys.com https://www.linkedin.com/in/aseem-agrawal-aa1279a8/ Software devloper with 6 years of experience around.
2. payal.pardeshi@perennialsys.com https://www.linkedin.com/in/payal-pardeshi/ : not technical
3. pooja.patil@perennialsys.com https://www.linkedin.com/in/pooja-patil-1621231ab/
4. sayan.mondal@perennialsys.com HR
5. vidula.bodke@perennialsys.com Hiring Java Developers for Perennial Systems ( Fintech Experts ).


 
PL/SQL
Microservices
Spring-framework
Docker
Kubernetes
Mysql
Java
Spring Boot



Innointel Global

Java Full Stack Developer
Accion Labs

ribin@stockal.com
EmbarkX

IsThread always async : parallely all tasks executes depict the same.

Java and Python basics and according to job role prepare well versed. 

and be good at the communication part, because it will be an major part of your selection because you are delaling with the client directly. 

So you must be fluent and go with sound words and word by word/


D
10th Certificate
12th marksheet
Btech Degree
Driving License
Pan Card
Photograph
Form 16
Statement Axis Bank : I have to confirm this with them.

Experience Letter : It would be delayed slightly
UAN card : no I have not activated 
Bank Kyc for PF A/c : How this I have not done yet


