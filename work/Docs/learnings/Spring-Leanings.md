# Spring Boot

## TODO Learnings 


### Aim : Designing a website using spring stack

https:start.spring.io -> This website generates the basic-structure of spring-boot project with default-dependency.

 • Spring Boot Primer   
 • Spring Cloud Primer  
 • Spring Microservices Primer  
 • Spring JPA Primer  
 • Java 8 Streams    
 • Spring Security Primer  

1. Application.properties where we can write all configuration related details.

2. Model are implemented using JPA, so that it will reflect the real-time-table of mysql-db.
 - Quote 
 - Quotes : Pojo for Username,list<Quote>

 3. repository
 - QuotesRepository

 4. resource
 - DbServiceResource - add,get,delete quotes by user-name

 5. DbServiceApplication

 DB-Service Microservices is ready for deleteting, adding and retriving the Quotes from the mysql-db.

----------------------------------------------------
### Stock Service Microservice

- we need here eureka-service-discovery for calling  eureka-client.

Netflix Eureka serves as a registry for services in a software system, functioning like a digital map that helps locate and connect to various services. It continuously updates its records to reflect changes in service locations, ensuring efficient and reliable service discovery for users. In essence, Eureka streamlines the process of identifying and accessing services within the application ecosystem.

Netflix Eureka is a Java-based open source project that provides a RESTful interface for service discovery and registration. It consists of two main components: Eureka Server and Eureka Client. Eureka Server is a centralized registry that maintains a list of all the registered services and their instances. Eureka Client is a library that interacts with the Eureka Server to register, deregister, and discover other services. Eureka Client also provides a client-side load balancer that can route requests to the best available service instance.

Here are some important functions to know.

- Service Registry: Each microservice that starts automatically registers itself (name, id, host, port).

- Service Discovery: Microservices can query Eureka to discover and communicate with other services. 

- Load Balancing: Microservices retrieve a list of available instances from Eureka and choose one based on a load-balancing strategy. Microservice A can have many instance(replication)

- Dynamic Updates: If a service restart, Eureka handles dynamic changes in the microservices landscape, allowing services to register, deregister, and update status in real-time.


Eureka-service: consule,ribbon

https://spring.io/blog/2015/01/20/microservice-registration-and-discovery-with-spring-cloud-and-netflix-s-eureka

AutoWiered
Config Class needed to do that
@LoadBalanced
@Bean
@Configuration

https://www.youtube.com/watch?v=ifBFwH59gGA

---------------------------------------------------------------------------------------------------------------







--------------------------------------------------
## Plan what to study 


1. Java Developer
Required Skills: Java, Core Java, Spring boot, Hibernate, Cassandra, Microservices, Mongodb, Struts, Servlets, Tomcat, API
Experience: 2-6 years

Java, Core Java, Spring boot, Hibernate,
lakshana.sundaresan@exterro.com
Problem is on my resume is that I have used the tools and don't brag what is that, so how could they know what is that.However we should now show details that much.

kehna kya chata ho vo clear nahi hai from my resume

1. JAVA
2. Spring
3. Spring-Boot
4. Spring-cloud
5. JPA and Hibernate
6. Maven and Gradle
7. Docker
8. Kubernetes 
8. AWS,GCP,Azure cloud platforms


https://status.hotwax.io/

-----------------------------------------------------------------------------------------

Courese Notes from 28minutes

Resolution of Recurring Error on Instances


Q: How could we run multiple Spring IOC container ?

Q: Java singleton (GOF) vs Spring Singleton
- Spring singleton : one object per spring IOC container.
- Java singleton (GOF) one object per jvm.

Q: Gang off four design pattern I have to study

Q: What is difference b/w war and jar file?
---------------------------------------------------------
Part 47:
@PreConstruct : After the all dependency wired-in or performing dependency injection and then to perform something then you can use this annotation on top of method. ex: like feach mysql data or connection initialization.


@PreDestory : It is used for capturing event of application/Bean termination,& send to attached method where we could perform the cleanup work/tasks.

imported from jakrata annotations 

--------------------------------------------------
Part 48:
J2EE , Java EE, Jakarta EE 
1. Java 2 platform enterprise edition
2. Java Platform Enterprise edition
3. Jakarta EE (Oracle gave java ee right to ecllipse foudation)
and they named as Jakarta EE

-JSP,JSTL,JAX-RS,JBean-Validation, Jakarta context and dependency injection
-Jakarta persisten api

All are same things but acquired and standard-nameing would change there names thats it.
------------------------------------------------------------------------------------------
Part 49:
# jakarta EE Has some annotation which is just similiar to spring-annotations

like: 
@Named ->@Component
@Autowired  -> @Inject

 - sping framwwork v1 released in 2004
 - CDI specifiacation introduced into java EE 6 platform dec 2009
 - now called Jax CDI
- CDI is specification and spring framework implements it.
- Important Inject Api annotations:
  - inject 
  - named
  - Qualifier
  - scope
  - singleton
  
Spring also performs CDI so it supports cdi annotations also


------------------------------------------------------------------------------
part 50:
Java Annotation vs xml spring configuration

1. easy to write vs cubersome
2. recent project widly used vs rearly now
3. no not mix either of one are good.
4. hard to debug java annotations vs medium
5. Pojo not clean as we are using spring annotation and import statement vs totaly cleaned
because we are reffreing the class from the xml, After that we would create the object.

6. and xml also support the component scan via tag.


## Spring with xml configuration file

1. ClassPathXmlApplicationContext
2. AnnotationApplicationContext
3. not used very frequently


-------------------------------------------------------------------------------------

Part 51: copy
52: diffrent annotations
53: please watch

TALISMAN_CONFIG

---------------------------------
Section 5

1. @RestController
2. @RequestMapping


It is easy to setup things with spring boot and writing a rest api and accessing it at the browser end simply.

But the real goal is to know what is happening behind the scene.


---------------------------------------------------------------------
61) Goal of this thing.: There is so much things which spring auto-configured for looking on it you have to see logs section.

62) Spring boot provides a lot of starter projects 
For building a applicaiton we would have to integrate all dependency according to your usecase like

WebApplication and Rest API - Spring Boot Starter Web spring-webmvc, spring-web,spring-boot-starter-tomcat, spring-boot-starter-json
unit-test 
talk to database then use DATA JPA 
talk to jdbc then use Spring Boot starter JDBC
security then use Spring boot starter security



-----------------------------------------------------------------------------
63). Spring-Boot AutoConfigurations


Spring-boot-autoconfigure-3.0.0-M3.jar 
How springboot internally does lot of configuration based on the package class

1. Dispacher servlet
2. Jakson bean which is an object to json converter.
3. Error throwing page 
4.

etc see pdf
Here I have to see how things internally works more in depth.

Here while running projects It logs the information about auto-congutation performed bydefault and what not. It provides full details.

Unconditional class?
-----------------------------------------------------------------------------------
64). Spring boot devops tools 

1. Productivity is improved by devops tool
2. No need to restart the spring server whenever you make changes, Because of devops tools it would auto-detect the changes and restart the server simply.
3. If we make change in pom.xml auto-server restart won't be working except this it would work for each and every thing like properties file , java , grovvy and html .

-----------------------------------------------------------------------------------
65). Spring Boot different profile setup like dev, prod, qa 

Based on the profile we would create spcific application.properties for managing specific configuration.

spring.boot.profile=dev

application-dev.properties

application.properties

we would define common properties in application.properties and profile specifc defined in profile.properties file elegantly.

@ConfigurationProperties
@Component
class CurrencyPropertieConfiguration {

//props
//getter and setters

}  

1. @Compoenent
2. @Configuration
3. @EnableConfigurationProperties(ConfigProperties.class)
4. 


Now spring would create configuration bean for that class and inject dependency based on the application.properties, it lets us utilize the configuration bean where we need,That's how complex application properties managed.

We can define properties as much we wanted to for Application, Use @ConfigurationProperties.

---------------------------------------------------------------------------------------------

66). Spring-Boot application deployment using embedded-server

maven-build clean build 

tomcat-starter-embedded

java -jar jar_location



-------------------------------
## Important Point Related @ConfigurationScan and @Configuration Class.

ByDefault @Configuration class include @Component annotation because of that its object is maintained as Spring-Bean. We can print it in console.

1. @ConfigurationScan only used with @Configuration class which said to scan all class for the autowiring and bean Registering. standalone we can't use and other reson from @Configuration we are creating the context.
Because @Configuration annotated class helps in creating bean.
@CompoenetScan work with it to tell where is @Compoenent, @Service @Repository @Controller



2. We can create mutiple configuration class and composed them 

With the @Import annotation
@Configuration classes may be composed using the @Import annotation, similar to the way that <import> works in Spring XML. Because @Configuration objects are managed as Spring beans within the container, imported configurations may be injected — for example, via constructor injection:

 @Configuration
 public class DatabaseConfig {

     @Bean
     public DataSource dataSource() {
         // instantiate, configure and return DataSource
     }
 }

 @Configuration
 @Import(DatabaseConfig.class)
 public class AppConfig {

     private final DatabaseConfig dataConfig;

     public AppConfig(DatabaseConfig dataConfig) {
         this.dataConfig = dataConfig;
     }

     @Bean
     public MyBean myBean() {
         // reference the dataSource() bean method
         return new MyBean(dataConfig.dataSource());
     }
 }
Now both AppConfig and the imported DatabaseConfig can be bootstrapped by registering only AppConfig against the Spring context:

 new AnnotationConfigApplicationContext(AppConfig.class);


 3. We can Manage profile based dependecy injection for diffrent env like prod,uat,qa etc
 
 With the @Profile annotation
@Configuration classes may be marked with the @Profile annotation to indicate they should be processed only if a given profile or profiles are active:

 @Profile("development")
 @Configuration
 public class EmbeddedDatabaseConfig {

     @Bean
     public DataSource dataSource() {
         // instantiate, configure and return embedded DataSource
     }
 }
  
4. In ComponentScan we can provide patterns for package searching and as well specific-path. But when we do not specify it points current package we have to avoid this.
We should avoid putting the @Configuration class in the default package (i.e. by not specifying the package at all). If we do, Spring scans all the classes in all jars in a classpath, which causes errors and the application probably doesn’t start.



# Spring JPA Topic 

@Repository 
@Transactional

@PresistenceContext
EntityManager springEntityManager;

 Spring Mvc use internally view-resolver in case of jsp 
 
 @RequestMapping
 public String jspRequest() {
 	return "sayHello.jsp"; //Here this returns view Resolver
 } 
 
 and View Resolver configuration is configured here
 
 spring.mvc.view.prefix=/WEB-INF/jsp/
 spring.mvc.view.suffix=.jsp
 logging.level.org.springframework=debug
 
 login page
 request-response
 @RequestParam
 

--------------------------------------------------------------------------------------
# We did not need to define Version explicity it will pick from parent version of pom.xml, It is good practice to define dependency-version


While it's true that some Maven dependencies may inherit versions from parent POMs or use default versions provided by Maven's dependency management, it's still a good practice to explicitly declare versions in your project's POM.xml to ensure clarity, consistency, and maintainability of your project's dependencies.
---------------------------------------------------------------------------------------
bg-danger,wanring,info,light,dark,white 
text.p,s,success,mute,warning
padding and margin : ms,b,t,x,y-(1-5level)
shadow-lg p-3 rounded
rounded-circle,sqare

----------------------------------------------------------------------------------------
# REST API Intro with Microservices Architecture

https://stoplight.io/api-types#:~:text=and%20the%20server.-,SOAP%20APIs,ways%2C%20SOAP%20is%20more%20restrictive.
----------------------------------------------------------------------------------------
Linkding Knwoledge : 

Saumya AwasthiSaumya Awasthi
(She/Her) • Following(She/Her) • Following
Software EngineerSoftware Engineer
5h • 5h •
Writing an API isn't just about the code.

It's about designing a strong foundation and following best practices that empower your applications and services.

Here are 10 best practices for writing SpringBoot APIs:

1. RESTful API Design Principles:
- Clear and Consistent Resource Naming
- Standardized HTTP Methods
- Meaningful Status Codes

2. Leverage Spring Boot Annotations:
- @RestController
- @RequestMapping
- @GetMapping, @PostMapping, @PutMapping, @DeleteMapping
- @PathVariable
- @RequestBody
- @ResponseBody

3. Embrace Dependency Injection (DI):
- Use @Autowired to inject dependencies
- Promote loose coupling and testability

4. Implement Exception Handling:
- Create custom exception classes for specific API errors
- Use @ControllerAdvice and @ExceptionHandler to handle exceptions gracefully

5. Model Data with Clear and Concise DTOs:
- Create dedicated classes (DTOs) to represent data exchanged between API endpoints and services

6. Security Best Practices:
- Implement authentication and authorization mechanisms
- Validate and sanitize user input
- Secure communication using HTTPS

7. Versioning:
- Consider versioning APIs to manage changes and maintain compatibility with clients

8. Documentation:
- Use Springfox Swagger or OpenAPI to generate interactive API documentation

9. Testing:
- Write thorough unit and integration tests for controllers, services, and repositories

10. Monitoring and Logging:
- Implement logging to track API requests, responses, and errors

By following these best practices, you can create well-structured, robust, and maintainable Spring Boot APIs that empower your applications and services.

-----------------------------------------------------------------------------------------------------------------------------------------------------
# ModelAttribute

@ModelAttribute Method: The addAttributes method annotated with @ModelAttribute is called before every request handling method in the controller. It ensures that the username attribute is always added to the model, avoiding the need to repeat this line in each request handling method.

-------------------------------------------------------------------------------------------------------------------------------------------------
## ⚡️ What is the Microservice Saga Pattern? Lakshya Bansal
The Microservice Saga Pattern is used to handle distributed transactions in a microservice environment. In microservices, different services work together to accomplish complex tasks, and failures can happen. The Saga Pattern provides a way to ensure that these transactions are completed consistently, even when failures occur.

🌐 How does it work?
Imagine you have an e-commerce system composed of multiple microservices: one for inventory, payment, order, and delivery. When a customer places an order, all these services need to coordinate their actions to complete the transaction. The Saga Pattern breaks down this process into smaller steps.

If any step fails:
- The Saga Pattern uses a compensating action to undo the effects of the previous steps and bring the system back to a consistent state.
- For example, if the inventory service fails, a compensating action would be triggered to reverse the payment made by the payment service.

💡 Benefits of the Microservice Saga Pattern
🔺 Reliability: By using compensating actions, the Saga Pattern helps maintain consistency even when failures occur during distributed transactions.
🔺 Flexibility: Each microservice can handle its part independently, allowing for easier scaling and maintenance.
🔺 Resilience: The system can recover from failures and continue processing transactions without blocking the entire process.

Here are some resources to learn more about the Saga Pattern:
https://lnkd.in/dJiCXB4c
https://lnkd.in/dt8ak_uP

-------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------
Spring Security Last Part

Oauth in Spring-Security and GoogleOauth simply configure in spring boot, you just have to generate the username and security credentials from the google oauth platform.

- On spring side there are some of predefind properties as we imported the dependency for the springboot-oauth


-------------------------------------------------------------------------------------------
Which of these is NOT a Principle of Building Secure Systems?

-> Assign Least Privilages  

6 Principles Of Building Secure Systems 1) Trust Nothing 2) Assign Least Privileges 3) Have Complete Mediation 4) Have Defense In Depth 5) Have Economy Of Mechanism 6) Ensure Openness Of Design




Form Based Authentication is used by most web applications. It uses a Session Cookie - `JSESSIONID`: `E2E693A57F6F7E4AC112A1BF4D40890A`.

Basic Authentication is the most basic option for securing REST API. It has many flaws.It is NOT recommended for production use. Base 64 encoded username and password is sent as request header - `Authorization`: `Basic aW4yOG1pbnV0ZXM6ZHVtbXk=`.

success alert
Good job!
Cross-Origin Resource Sharing (CORS) is specification that allows you to configure which cross-domain requests are allowed. In Spring Security, you can configure Global Configuration by adding `addCorsMappings` callback method in `WebMvcConfigurer`. You can also create local configuration in controllers by adding `@CrossOrigin` annotation.


Recommended: Use adaptive one way functions with Work factor of 1 second. It should take at least 1 second to verify a password on your system. Examples: bcrypt, scrypt, argon2, ..


JWT contains Header(Type: JWT, Hashing Algorithm: HS512), Payload ( iss: The issuer, sub: The subject, exp: When does token expire?, iat: When was token issued?, Custom Attributes), Signature(includes a Secret)




Symmetric encryption algorithms use the same key for encryption and decryption. HOWEVER Asymmetric Key Encryption uses two keys - Public Key and Private Key. One for encryption and the other for decryption.


-------------------------------------------------------------------------------------------------

## Aspect Oriented programming

AOPConcepts 
Pointcut
Aspect
@After
@Before
Annotations
Advice
@Around 
BestPractice

----------------------------------------------------------------------------------------------------

## Aspect Oriented Programming

There are multiple layers while building a project
1. WEB Layer
2. Buisness Layer
3. Data Layer
Although all has diffrent responsiblity.
But In each layer there are some few common aspects that apply to all layers.

1. Security: Like all service need authenticationa ans autherization
2. Performance : Each exective controller request needs tracking and performance  
3. Logging

These common aspects are called cross cutting concerns.

1. we would define this commone aspects as core.
2. we then define point cuts where the aspects should be applied.


There are 2 ways to do it

1. Spring AOP
 - Not a complete AOP solution but very popular as wide audience are using spring framework.
 - Only works with spring Beans
 - Examples : intercepts method calls to spring Beans.
 
2. AspectsJ 
 - Complete AOP solution BUT rearly used
 - Example: Intercept any method call on any java class.
 - Example: Intercept change of values in a field. It is amazing
 
 we will be focusing on the spring AOP in the section.
 
 
 -----------------------------------------------------------------------------------------------
 ## Create a Project AOP simply
 
 1. Define a configuration class for AOP where you would define 2 things
 
 - when : At what pointcut
 - where and what : Where intercept and put
 @Configuration
 @Aspect : throw which define what this class contains aspect oriented programming.
 
 @Pointcut()
 execution( * PACKAGE.*.*(..))
 
 
 * = any return value
 .*.*(..)= Intercept all class calls withing specific pakages
 
 @Pointcut("execution(* com.in28minutes.learnspringaop.aopexample.buisness.*.*(..))")
 public void logMethodCall( JointPoint joinPoint) {
 	logger.info("Method is called- ", joinPoint);
 }
 
 - Here we can can define what calls and in which specific pakage I have to intercept the calls.
 - After that identify the specific method execution using the join points.
 
 ## When we do call our specified method before or after the intercepted method execution
 we use @Before for calling our logic first and then intercepted method let finish there work. 
 
 @Before("execution( * PACKAGE.*.*(..))")
 public void logMethodCall( JointPoint joinPoint) {
 	logger.info("Before AspectMethod is called- ", joinPoint);
 }
 
 We have created two sub pakages 
 1. Data 
 2. Buisness 
 
 we wanted to capture if both then just make *.*.*
 
 
-------------------------------------------------------------------------------------------------
## Aspect Oriented Programming

#Compile Time

-> Advice - What code to execute? Before the certain method.
-> Pointcut - Expression that identifyes method calls to be intercepted 
Example - > execution(com.in28min.aop.data.*(..))

-> Aspect - It is combination of what and when Advice + Pintcut
-> Weaver - Waever is the framework that implements AOP. Weaver is the responsible for determining  execution of Advice on mentioned poitcut or right point of cut.

Runtime
-> JointPoint : It would helps us to identify to know for which method-call event occured. And based on that we can make conditions.

joinPoint.getArgs()

When pointcut condition is true, the advice is executed. A specific execution instance of an advice is called a join Point.


-------------------------------------------------------------------------------------------------
## More AOP Annotations


@Before- Do somthing before a method is called
@After - Do somthing a method is executed irrespective of wheather :
1. Method executes successfully OR Mthod throws an exeception.

@AfterReturning -> run only when successfully method call executed and we can get the returned result  and we can whatever we can do that. 
@AfterThrowing -> run only when method throws any exception.

@AfterThrowing(
pointcut = ,
throwing ="exceptions" 
)

public void logMethodToCall(JoinPoint jp, Exception e){
logging.info("exception occured at", jp, e);
}

@AfterReturning(
pointcut = ,
returning ="exceptions" 
)

public void logMethodToCall(JoinPoint jp, Exception e){
logging.info("exception occured at", jp, e);
}
------------------------------------------------------------------------------------------------
## Performane-Calculating-Aspect.

Behind that we are using Reflection API.

- How to get the time of exection of method and stop.


@Around- Do something before and after a method exection
Like time calculations;

-------------------------------------------------------------------------------------------------
## Best Practice

Imagine if I have change some pakages, I have to make changes every where.


1. Include all pointcut in the common file that wil make mangement better.
2. Instead of using execution pointcut you can use Bean throw which you can directly point out the Bean

CommonPointConfig

@Pointcut(
pointcut="bean(*Service*)"
)
Capture all calls of Beans which is specified as Service
All beans which has service in there name.
---------------------------------------------------------------------------------------------

## Create Our Custom Annotations

1. We can simply create an Inteface named TrackTime 


//Methods
//Runtime

@Target(ElementType.METHOD)
@Retention(RententionPolicy.RUNTIME)
public interface TractTime {

}

2. Use @annotations

@Pointcut("@annotation(com.in28minutes.learnspring.aopexample.annotation.tracktime)")
public void trackTimeAnnotation(){}

3. Now Bind above  trackTimeAnnotation method call with timecalculation advice method.

@Around("com.*.trackTimeAnnotation()")
public Object findExecutionTime(ProceedingJoinPoint processjp) throw {
	
	long startTimeMillis = System.currentTimeMillis();
	Object returnValue = proceesingJoinPoint.proceed();
	long stopTimeMillis = System.currenttimeMillis();
	long exedurationtime = start-end;
	return exedurationtime; 
}


Now we are only getting tracTime for specific methods only
and Other usecases for that like opting specific security for certain methods then on that case you can define your own custom method.

-------------------------------------------------------------------------------------------------
1) Advice - What code to execute? Example: Logging, Authentication. 2) Pointcut - Expression that identifies method calls to be intercepted. Example: execution(* com.in28minutes.aop.data.*.*(..)). 3) Aspect = Advice + Pointcut


-----------------------------------------------------------------------------------------------


-----------------------------------------------------------------------------------------------
## Maven 

pom.xml -> project object model
Transitive dependency : These are the dependecy inside a dependency 
Example : There is spring-boot-starter dependency which contains the pom.xml which contiains some dependency on which spring-boot-starter depedency depend.

throw pom.xml we are also able to download the transative dependecy also.

1. Responsibility of Maven is dependecy management.
2. Transitive and parent depedency avail by Maven.

Spring dependency management is about the object availing then and all those beans are efficently managed by spring.
------------------------------------------------------------------------------------------------

## DependencyManagement

- Here we just mention the dependency version which we wanted to be used in our project setup.



## Dependency
- Here This are the actual dependency that are to be downloaded.
- It will pick the version from the DependencyManagment.

But question like

what if DependencyManagement does not have the inventory


---------------------------------------------------------------------------------------------------------------------------------
# Keystore and trustore 

Keystore : self Identity which tells about ourself and it must be private  
Trustore : It contains entry of trust-certificate of all other instance which we trust and we have to connect.

Currently in hotwax both keystore and Trustore are both same.

------------------------------------------------------------------------------------------------------------------------------------------
Jul/12/2024/-------------------------------------------------------------------------------------------------------------------------------
# Microservice Architecture : 

1. Monolithic Architecture:

- Monlithic Application has single code base with multiple modules.
- Monlithic Application has divided in Controllers , services, dao , db
- It may contain the fulfillment, OrderManagement, PaymentManagement modules but they all are part of single jar/ application that's why we are saying it monlithic architecture.
- Even if can deploy this apllication on multiple server, We can't say the microservice architecture. Because they are not communicating with each other and even we are not able to get feature like scalability, manitanability, reliability, flexibility, customizable scalable, working with diffrent language (language agnostic architecture) according to need.

Disadvantage:
What is the disadvantage 
- As Project Scale, it becomes difficult to manages.
- For single change redeployment of whole application needed. If we took example of amazone think about how much time does it took redeploy whole amazone application.
-Difficult to adapt new technology for single functionality. Not impossible but it makes complez to incorporate both programmaing language to work in same monolith env in m1 java, m2 python.


Advantage:

- simple to develop
- simple to build and develop.
- problem of network latency are relatively less. because monolith contains modules in same application same server instead in microservices they are on different server so latency delay it is expected and optimized by using right/fast protocol. 


2. Microservice Archtecture

- Microservices are the small services that work togethere. Here difference is that in monolith those service that are working as coupled manner in application now we would make losely coupled and deploy and manage seperately and they would simply communicate with each other in losely coupled manner.

-These smaller service communicating with each other directly using light weight protocols like Http2.0 etc.

- Microservices code-base different and db seperate.

Advantages: 
- It is possible to change or upgrade each services individually rather than upgrading in the entire application.
- One service may down without impacting to others.
- Easily use different technolgy(Language agnostic but you rearely do it like that if you are using spring boot than you are continuing with that only.) for building diffrent microservices.
- Less dependency. Loosely coupled , That means 
  If there any error in perticular microservice occures than only that 
  
  
## Microservices Architecture

1. Api-Gateway
- single end point 
- Authentication and security
- Example : Zule Server, Spring Cloud gateway.

2. Hystrix Dashboard

It is Fault Tolerant Library which handles the fault/failure around the failure of microservices.


3. Eureka Server for Service Discovery : 

- Here we would simply deploy register our microservice with the help Eureka client.
- And there is a Config-Server also which fatches the stored-configuration for registered microservices from Github Source .

4. There are also multiple-things work in this architecture according to our need like lib for loadbalancing, Http etc.


## How microservicces contact each other : simply Rest Call.

## Use CASES

1. There would this 2 seprate services which is hosted in differrent server and the port. That would cause problem. -> 

2.So here we would configure the Api-Gateway which provides the single endpoint.

1. 
UserService : ip:port

ContactServices : ip:port


2. Api-Gateway is itself an microservice.

3. Create a Eureka server(microservices) and with the help of Eureka-client 
- We would register all microservices over there.
- That would resiliently manages our all microservices. 

That would maintain the inter-communication of microservices and remove that locahost thing throw virtual IP it will manage all things.


Project-Setup:

1. user-service

- application.yml properties which is used to maintain properties heirarchy in a better manner.

Jul/12/2024/-----------------------------------------------------------------------------------------------------------------------------------------------------
## Creating User Service and Contact Service 

1. 
- Simply define some of entity,dao (data-access-object), services, controllerRequestMapping specific to microservices
- We would run both service in localhost but in different port.

2. For calling a Rest Service from another microservice we would use RestTemplate;

@Bean 
public RestTemplate restTemplate() {
	return new RestTemplate();
}


3. Use the RestTemplate object while retriving the user and call for retriving the contacts information from contact service 


@Autowired
public RestTemplate restTemplate;

@RequestMapping("/user/{userId}")
public User getUserInfo(@PathVariable long userId){
	User user = userlist.getUserByID(userId);
	List contact = this.restTemplate.getForObject("http://localhost:9002/contact/user"+ user.getUserId(), List.class);
	user.addContactList(contact);
	return user;
}

RestTemplate help us to connect with another microservices. Just like RestClient

4. Problem above we have used statically hards coded uri to call another microservice, instead of this we can register these microservices/url in Eureka-Server and access/call throw(VirtualHost) it via Eureka-Client configured in the microservices. That would remove this hardcoding and in future we somehow we change IP/URI of microservices we simply have re-register it on Eureka-server no need to change every-where/no obstruction over microservices communication.

Because Eureka maintain the Virtual_host which is is used in microservices and it is resolved by Eureka at the calling time.



5. Simply add dependecies Eureka-Server pom

- @EnableEurekaServer

- dydefault port 8761
- Here we have created a microservice which is Eureka-Server so we need to mention that do not register with itself.
---------------------------------------------------
- application.properties

server: 
	port: 8761

eureka:
	client:
		register-with-eureka: false
		fetchRegistry: false
	server:
		waitTimeInMsWhenSyncEmpty: 0
---------------------------------------------------	

Here we succefully created our server but not the eureka-client so you are not able to see the registered microservices.

6. Next Step Is to Create Eureka-Client in the running services.

Dependency 
- Eureka Discovery Client

Other things-to-copy 
- Spring-cloud	
- DependencyManagement section
- spring-cloud-starter-netflix-eureka-client


By Doing this just restart it will work and able to see microservices in registered section. But came with Unknown Application name.

7. Now we have to configure the name 

# For configuring the name of microservices 
spring.application.name = contact-service
spring:
	application:
		name: contact-services
		
		
# for configuring write IP on eureka-server
eureka:
	instance:
		hostname: localhost	
		
8. Now we can call the microservice by the registered application name on eureka-server instead of localhost:port.

List contact = this.restTemplate.getForObject("http://contact-service/contact/user"+userId,List.class)
9. Above step throw us an error unknown host exception, @LoadBalanced

On RestTemplate we have to use @LoadBalanced so that it would first resolve host from eureka and then went to actual request.


@Bean 
@LoadBalanced
public RestTemplate restTemplate() {
	return new RestTemplate();
}

10. API Gateway
Here we are building a microservice which acts as api gateway.


- Add dependency Spring Cloud Routing Or Zuul (But only works under Spring boot version 2.0.0 and < 2.40)
- Add Eureka Client, Actuator.

- Configure the api-gatway microservice in eureka-server and define the mappings for routing into different service in api-gateway.

server :
	port:8999

eureka:
	instance:
		hostname:localhost

spring:
	application:
		name:api-gateway
	cloud:
		gateway:
		routes:
			- id:user-service
			  uri: lb://user-service
			  predicates:
			    - Path=/user/**
			- id:contat-service
			  uri: lb://contact:service
			  predicate;
			    - Path=/contact/**
			    
			    
## Currently All Microservice are bydefault calling to default port of eureka, we you wanted to deine custome then how?
eureka.instance.port
eureks.instance.hostname


## Hystrix Service For Monitoring and Dashboarding.

Hystrix and Hystrix-Dashboard for vizvlizing the fault-ocuured in all microservices.
Hystrix-Dashboard featches the all fault occured and vz on the 

-----------------------------------------
##IMP Section:
## Dependency-Management section in pom.xml file

Any module that inherits from this parent POM can declare these dependencies without specifying the versions. The versions will be inherited from the dependencyManagement section.

The dependencyManagement section in a Maven pom.xml file is used to centralize the dependency information for a project, particularly when dealing with multi-module projects. It allows you to specify the versions of dependencies and their transitive dependencies in a single place, ensuring consistency across all modules of the project.

1. Centralized depedency managment and configuration acroose all modules
2. Version control : We can specify the version here so that all over modules use it same version so lib version confilts problem would never arrive.
3. Inheritance/ Transitive dependency: 

  <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework</groupId>
                <artifactId>spring-core</artifactId>
                <version>5.3.9</version>
            </dependency>
            <dependency>
                <groupId>org.springframework</groupId>
                <artifactId>spring-context</artifactId>
                <version>5.3.9</version>
            </dependency>
        </dependencies>
    </dependencyManagement>
    
 

----------------------------------------------------------------------------------------------	 

## For initalizing the Bean and doing task before distroying that object.

# PreDestroy(Before just it got destroyed) and PostConstruct (After object is autowired)

- IntializingBean -> afterPropertiesSet
- DisposableBean -> destroy

# What is life of Spring IOC

Container started -> Bean Init -> Dependecy Injected -> custom init method -> customer utitily method -> custom destroy method.


# There are many ways to implement lifecycle methods.

1. Annotation : PreDestroy and PostConstruct
2. Java : Interface available I have ovveride 
- IntializingBean -> afterPropertiesSet
- DisposableBean -> destroy
3. XML : do not used but there is init attribute throw which we can do that.


------------------------------------------------------------------------------------------------

Q 14). What is Bean Factory, have you used XMLBEANFACTORY ? 

ConfigurableApplicationContext  -> It is indirect ofbject ->Applicationcontect -> BeanFactory




Question : What is profile in spring boot application.
The @Profile annotation tells Spring that those beans in the file should be instantiated only when the specified profile is active. The profile is activated using the spring.profiles.active JVM argument or the property defined in application.properties file.


Activate statment
1. spring.profiles.active=dev

2.JVM
java -jar your-application.jar -Dspring.profiles.active=local



## profile 

1. prefix application.props
2. spring.profile.on.enabled=prod

@Profile()

- we can give a condition to configure the Bean or Not.  based on the profile and we can pass or activate the profile based on the jvm enviroment.



---------------------------------------------------------------------------------------
Databse concept
Docker kubernetes and my projects.