# Spring Boot Interview Question

## Inteview Questions:

1. What is Spring Boot
2. Why Spring Boot came?
3. Working of Spring Boot? : Pom.xml Starts scanning and then it autoConfigures alot of packages.
4. How Spring Boot Starts? :
- It starts execution from main class although.
- It starts from the SpringBootApplication.run() -> that would starts and auto-configure all the libirary. and creating the application context and initializinf it.
- Once the application context is initiated the run() method starts the application's embedded web server.

5. Top Spring Boot Annotations : 

-> @SpringBootApplication -> @Configuration, @EnableAutoConfiguration, @ComponentScan (it scans all sub-packages of the currentpackage where it is declared.)
-> @Component 
-> @Autowired
-> @Service 
-> @RestController 
@Controller
@ResponseBody, @RequestMapping, @Repository
@ConfigurationPropertie
@Primary
@Secondary
@Bean


6. What are the spring Boot starters?

Starters are collection of pre-configured dependencies that make it easier to develop particular kind off application.


7. Spring Boot cli :
spring version
spring help
spring init 
-  here -d (dependencies )
- --list (that would show the whole information).
- spring init -d web cli-project

Spring Cli we can use to setup the project structure in less time and configuration and dependency and all things it would take care of it.
-------------------------------------------------------------------------------------------------
spring-boot-starter-parent
spring-boot-starter-web
spring-boot-starter-cloud
spring-boot-starter-actuator
spring-boot-starter-jpa

- parent-starter will provide the basic configuration  like java version , version setup for mentioned dependency and, maven jar, maven build file configuring and downloading there dependency.

- Here we can do it this thing manually also but then we have to use DependencyManagement Section of pom.xml file and define spring-boot-starter-spring -> Now you just can define the dependency and versioning should be done by this and we can manually configure the maven dependency.