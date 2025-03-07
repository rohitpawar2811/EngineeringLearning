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

2. Facade : It just provide abstraction over the concreate implementation and just provide us quick use to functionality.

3. Observer :
4. CQRS (Command Query Responsibility Segragation) : 
Separating read and write operations for better scalability and performance.

5. Saga  : this pattern generally used in microservices.
-  It is used to manging the distributed transaction by breaking them into a series of smaller transactions that can be coordinated and completed independently.

Example: Implementing a saga orchestrator to manage the sequence of events.

6. Factory Method : we would got readymate object we just have to quer and we got.

7. Builder Method
8. Abstract Factory Method
9. Decorator Design Pattern : Pass in a simple objecte it will just got transformed.
10. 

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

2. Asyncronous Communication : Kafka or something topic wise thing.


## Technical Interview

1. Your Projects : SpringBoot , Apache-Solr, Apache-Kafka, SQL, AWS-Services  
2. There Need: Spring, Spring-Boot, Java, Apache-KAFKA streming, Sql
EKS, Kubernetes

















1. Performance and security of MS. kubernetes, aws, kafka, system design, component design.
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


## Document Needed : 

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


------------------------------------------------------------------------
## Token Vs Session
Session-Based Authentication
- Session Creation: When a user logs in, the server authenticates the credentials and creates a unique session ID, usually stored in a server-side database or in-memory store like Redis.
- Session Storage: This session ID maps to the user’s data on the server, so the actual session data (user details, roles, etc.) remains secure on the server side.
- Session ID Cookie: The server then sets this session ID in a cookie on the client’s browser. The client doesn’t access the session data directly – it only holds the session ID.
- Request Verification: For every new request, the browser automatically sends this session ID back to the server via the cookie. The server retrieves the associated session data based on the ID and verifies the user.

2️⃣ JWT-Based Authentication
- Token Generation: After the user logs in, the server generates a JWT (JSON Web Token), typically composed of three parts: the Header, Payload, and Signature.
 - Header: Contains token type (JWT) and hashing algorithm.
 - Payload: Includes user data and claims like `user_id` and `role`. This part is usually base64 encoded, not encrypted, so anyone with the token can decode it.
 - Signature: Created using a secret key and the hashing algorithm, this ensures the token hasn’t been tampered with.
- Token Transmission: The JWT is then sent back to the client, usually as a cookie or within a response header. Since JWTs are stateless, the server doesn’t store them; instead, the client retains the JWT.
- Token Verification: For each request, the client sends the JWT, which the server verifies by re-computing the signature with the secret key. The server then extracts user details directly from the JWT.


------------------------------------------------------------------------------------------------------------------------------------------------

Struggling with JavaScript interviews?

Prepare these essential JavaScript interview Questions to boost your confidence and expand your knowledge: 

1. What are the possible ways to create objects in JavaScript? 
2. What is a prototype chain? 
3. What is the difference between Call, Apply, and Bind ? 
4. What is JSON, and what are its common operations? 
5. What is the purpose of the array.slice() method? 
6. What is the purpose of the array.splice() method? 
7. What is the difference between slice and splice ? 
8. How do you compare Object and Map ? 
9. What is the difference between == and === operators? 
10. What are lambda expressions or arrow functions? 
11. What is a first-class function? 
12. What is a higher-order function? 
13. What is a unary function? 
14. What is a curried function? 
15. What is a pure function? 
16. What is the purpose of the let keyword? 
17. What is the difference between let and var ? 
18. What is the Temporal Dead Zone? 
19. What is an IIFE (Immediately Invoked Function Expression)? 
20. What is memoization? 
21. What is hoisting? 
22. What are closures? 
23. What are ES6 classes? 
24. What are modules, and why do you need them? 
25. What is scope in JavaScript? 
26. What is a service worker? 
27. What is IndexedDB? 
28. What is web storage? 
29. What are the differences between cookies, localStorage, and sessionStorage? 
30. How do you access web storage? 
31. What is a promise? 
32. What are the three states of a promise? 
33. What is promise chaining? 
34. What is Promise.all ? 
35. What is the purpose of the Promise.race() method? 
36. What is strict mode in JavaScript? 
37. Why do you need strict mode? 
38. What is the purpose of the delete operator? 
39. What is the typeof operator? 
40. What is the difference between null and undefined ? 
41. What is the difference between window and document ? 
42. What is the difference between document load and DOMContentLoaded events? 
43. What is event bubbling? 
44. What is event capturing? 
45. How do you submit a form using JavaScript? 
46. What is the same-origin policy? 
47. What is the difference between native, host, and user objects? 
48. What are the tools or techniques used for debugging JavaScript code? 
49. Is JavaScript a case-sensitive language? 
50. What are events in JavaScript? 

More JavaScript Learning Material :
1. Async code in JavaScript​: https://lnkd.in/dT_Pxr5N
2. Free React Courses: https://lnkd.in/gMSJ7BwP
3. 40 React Interview Questions: https://lnkd.in/d3BB8gzA
4. Abstract Data Types in JavaScript​: https://lnkd.in/dXTsb9cm
5. Node Js Interview Questions: https://lnkd.in/dJyyBbFm
6. Node & Express Roadmap: https://lnkd.in/dEQpBNts
7. SQL Interview Preparation Kit : https://lnkd.in/dQSvwMKi

Join my WhatsApp Channel Here: https://lnkd.in/d4YiB9xt

Follow Ashish Misal for more insightful content on System Design, JavaScript and MERN Technologies!

## Different ways to Solve the DP problem
The following problems cover DP topics:
- strings
- distinct ways
- decision-making
- merging intervals


https://www.linkedin.com/posts/karan-saxena-466b07190_31-dp-problems-of-all-patterns-you-should-activity-7284912183715479552-OHaF?utm_source=share&utm_medium=member_desktop

https://www.linkedin.com/posts/jainshrayansh_softwareengineer-activity-7292521274554077184-MPP_?utm_source=share&utm_medium=member_desktop



Java Developer Interview Questions for Experienced
hashtag#realtime hashtag#java hashtag#scenario hashtag#interview hashtag#questions
1.     You need to prevent API abuse by implementing a rate limiter in Spring Boot.
·       How would you implement it?
·       Which algorithms would you use? (Token Bucket vs. Leaky Bucket)
·        How can Redis help in rate limiting?
2.     Your system expects 1M+ requests per second during peak load.
·       How do you scale your system?
·       What caching mechanisms would you implement?
·       How do you handle sudden traffic spikes?

3.     Users are uploading large files (1GB+), and the service is slowing down.

·       What’s the best way to handle file uploads efficiently?
·       Would you use S3, MinIO, or another storage solution?
·       How to implement a resumable upload?

4.     Identify and fix the memory leak in the following code:
class MemoryLeakExample {
 private static List<String> cache = new ArrayList<>();

 public void addData() {
 for (int i = 0; i < 1000000; i++) {
 cache.add("Data-" + i);
 }
 }
}
·       What is wrong with this code?
·       How do you fix the memory leak?

5.     The following code is not thread-safe. Why?

class Counter {
 private int count = 0;

 public void increment() {
 count++;
 }
}
·       What’s wrong with this implementation?
·       How would you make it thread-safe?

6.     Your REST API is slow. Fix this code:

@GetMapping("/users")
public List<User> getAllUsers() {
 return userRepository.findAll();
}
·       Why is this method slow for large datasets?
·       How can you optimize it using pagination?



Part1- Java Developer Interview Q&A

1. Rate Limiter Implementation in Spring Boot
- Implementation Use Spring AOP or a Filter/Interceptor with Redis. Create a `@RateLimited` annotation and track requests per user/IP using Redis counters. 
- Algorithm: Token Bucket (allows controlled bursts) or Sliding Window (tracks precise time windows). Redis can manage tokens or timestamps. 
- Redis Role: Stores request counts atomically (e.g., `INCR` and `EXPIRE`). Enables distributed rate limiting across service instances. 

2. Scaling to 1M+ Requests
- Scaling: Horizontally scale with Kubernetes/Docker. Use auto-scaling, load balancing (NGINX), and stateless services. 
-Caching: Redis for hot data, CDN for static assets. Cache-aside pattern with TTL. 
- Traffic Spikes: Auto-scaling, queue-based load leveling (Kafka), and circuit breakers (Resilience4j). 

3. Large File Uploads
- Efficient Uploads: Chunk files (e.g., 5MB chunks) and upload in parallel. 
- Storage: Use AWS S3 (managed, scalable) or MinIO for private cloud. 
- Resumable Uploads: Implement the tus protocol or track chunks with unique IDs. Resume using chunk offsets.


Part2- Java Developer Interview Q&A

4. Memory Leak Fix 
-Issue: Static cache list grows indefinitely. 
- Fix: Use a bounded cache (LinkedHashMap with LRU).

Java Code:
 private static Cache<String, String> cache = CacheBuilder.newBuilder()
 .maximumSize(1000)
 .build();
 

5. Thread-Safe Counter
- Issue: Non-atomic count++ causes race conditions. 
- Fix: Use AtomicInteger

 Java Code:
 class Counter {
 private AtomicInteger count = new AtomicInteger();
 public void increment() {
 count.incrementAndGet();
 }
 }
 

6. Optimize Slow REST API
- Issue: Fetching all users without pagination. 
- Fix: use pagination 
 
Java code:
 @GetMapping("/users")
 public Page<User> getAllUsers(@RequestParam int page, @RequestParam int size) {
 return userRepository.findAll(PageRequest.of(page, size));
 }
 
 Use Page in Spring Data to return paginated results.

 https://www.linkedin.com/posts/dipali-chandankar-66927b215_springboot-java-interviewprep-activity-7292410417308471297-33Pi?utm_source=share&utm_medium=member_desktop


 ------------------------------------------------------------------------------------------------------
IMP  

 https://www.linkedin.com/posts/jainshrayansh_udemy-youtube-softwareengineer-activity-7292904159584952320-X2wV?utm_source=share&utm_medium=member_desktop

 https://www.linkedin.com/posts/lakshman-reddy_java-developer-scenario-activity-7293181208631427073-UlzP?utm_source=share&utm_medium=member_desktop

 https://www.linkedin.com/posts/devopsguylohith_interview-devops-aws-activity-7293164992193867776-TDLy?utm_source=share&utm_medium=member_desktop

 https://www.linkedin.com/posts/sahil-wankhade-858015185_microservicesarchitecture-interviewtips-techinterviews-activity-7292017775684812801-vHni?utm_source=share&utm_medium=member_desktop

 https://www.linkedin.com/posts/shashwatbangar_data-scientist-azira-activity-7293199997251022850-qQLd?utm_source=share&utm_medium=member_desktop

Amazing Learning :
 https://www.linkedin.com/posts/karan-saxena-466b07190_5-years-ago-i-watched-a-talented-guy-from-activity-7292519905868808192-zYvt?utm_source=share&utm_medium=member_desktop

 https://walmart.wd5.myworkdayjobs.com/WalmartExternal/job/IN-KA-BANGALORE-Home-Office-PW-II/Software-Engineer-II_R-2095791

System-Design
 https://www.linkedin.com/posts/goyalshalini_youre-not-prepared-for-a-system-design-interview-activity-7293613331909623808-ceuy?utm_source=share&utm_medium=member_desktop

 https://www.linkedin.com/posts/neha-dhameniya-8648a2128_java-microservices-springboot-activity-7293231185831284736-GWDX?utm_source=share&utm_medium=member_desktop

 https://www.linkedin.com/posts/karan-saxena-466b07190_if-you-want-to-become-a-better-software-engineer-activity-7293627398296592387-fJpy?utm_source=share&utm_medium=member_desktop