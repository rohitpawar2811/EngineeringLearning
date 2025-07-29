# Interview Experiences and Questions : 

## Perninal Interview Questions : 
interface Operator {
int plus (int a, int b);
}

(a,b)->{
	return a+b;
}

even number and *5

List l = list.stream.even().mul(5).collect(::LIST);

@Qualifer()
Bean
getNAme

@ConfigurationPropertie



@CompoentAdvice
Class CustomGlobalExceptionHandler{

@Exception(NullPointerException.class)
public ResponseEntity<T> handleAll(Web){

}


}



Aseem Perennial
3:11 PM
Parent p = new Child();
p.print();
You
3:14 PM
Collection.sort(list,(a,b)->a-b);
Hover over a message to pin it
keep
Aseem Perennial
3:17 PM
interface Operator {
int plus (int a, int b);
}
Aseem Perennial
3:39 PM
Input - > "My name is ABC"
Output -> "ym eman si cba"

- Distributed tracing
- How would we can communicate to our api to other api
- Microservices 
- How we can build a microservices using **docker** and how we are able to deploy in the containerized environement. 

- StreamAPi
- @Qualifier
- @GlobalExceptionHandling
- @Bean Vs @Component
- @ConfigurationPropertie
- Kafka and Zookeeper
- One Programming based question : reversal programme
- Java Concept Spring Bean what is lifecylce

- OOPs why to use ops in project?
- Design Pattern I would know
- Runtime polymorophish
- Docker
- Port-Forwarding
- RestTemplate
- Apache Solr what is that and how you integrate in springBoot system.? Let US Know

Updated Solr Doc SolrInputDocument(fields: [picklistItemStatusId={set=PICKITEM_COMPLETED}, shipmentStatusId={set=SHIPMENT_SHIPPED}, itemShippedDate={set=Mon Jul 22 22:54:14 EDT 2024}, orderStatusId={set=ORDER_COMPLETED}, picklistItemStatusDesc={set=Completed}, docType-identifier=OISGIR-43439-00101-00001-90533, updatedDatetime={set=Mon Jul 22 22:54:14 EDT 2024}, fulfillmentStatus={set=Completed}])

------------------------------------------------------------------
Question 1.
 Regression vs Re-testing , smoke vs sanity testing , bug life cycle , sdlc & stlc, api testing related questions , database testing questions.
------------------------------------------------------------------
Question 2. 
 Oops Concepts & Automation API & UI
------------------------------------------------------------------
Question 3.
1. closuer
2. let and var hoisting concept
3. shallow and deep copy
------------------------------------------------------------------



## Paratiti Tech Solution Question and answers

1. Singleton: Constructor Private was the condition P
2. Factory Design pattern : Interface based pattern P
3. Agile Methodalogy P
4. HashTable and Collision resolution technique d P
13. Injections Type and When to use setter injection.
5. RestBased  
6. RestFull and Soap(It just only supports XML) P
7. @Qaulifier
8. Overloading
9. Coding questions : Check for the palindrome
10. Exception handling in spring: GlobalException and throws
11. How could we create the  Our own Custom ExceptionClass : We just have to Override the the class 
12. Inheritance why to use it and what we are trying to achive with that.
14. PathVaribale and RequestParam
15. ArrayList vs LinkedList
16. Serialization why and in which format it will convert the data P
17. Spring Exception Handling
18. Profile creation and how can we activate it. mug up the statments.
19. Spring Intializer what is ?
20. Object class notifyAll () method what for we are using that.
21. Protected and Default access modifire scope.
22. What is the use case of Optional Keyword why we would use and different senerious. P
23. What is functional programming.

class A{

public int sum(int a, int b){
   return a+b;
}

public void sum(int a, int b){
System.out.println("Hello");
}

main(){
A obj = new A();

obj.sum(10,20);



}
}

import java.util.*;

public class Main {
    public static void main(String[] args) {
      // System.out.println("Hello, World!");
      //Palindrome check
      int num = 213312;
      String numstr = String.valueOf(num);
      int end = numstr.length() -1 ;
      int start = 0 ;
      boolean isPalin = true;
      while (start<=end) {
        if (numstr.charAt(start) != numstr.charAt(end)) {
          isPalin = false;
          break;
        }
        start++;
        end--;
      }
      
    System.out.println("The number is "+ num);
    if (isPalin) {
          System.out.println("Palindrome");
    }
    else {
      System.out.println("not a Palindrome");
    }
      
  }
}

https://www.youtube.com/watch?v=rliSgjoOFTs&list=PL6W8uoQQ2c63W58rpNFDwdrBnq5G3EfT7

9962309089 : compoundo

## Learning :

1. Design pattern Learning : SingleTon, builder, Factory, Abstract Factory, Observer, Adapter, Facade, Proxy. Microservices : Safa, CQRS, Strangler.
2. HashMap Internels and Collitions
3. Serialization
4. SetterInjection Why to use?
5. Distributed tracing
6. How would we can communicate to our api to other api
7. Microservices 
  7.1 Api Gatway : How we can do port forwarding.
  7.2 Service Discovery.
8. How we can build a microservices using **docker** and how we are able to deploy in the containerized environement. 
9. StreamAPi hands on : Optional
10. MultiThreading.
11. Kafka and Zookeeper


------------------------------------------------------------------------
## Innowite Tech Solutions

transaction details - id, txnAmt, txntype

List<TrasactionDetails> transactionDetailsList;

int amount = transactionDetailsList.stream().filter((txn) -> "credited".equals(txn.txntype))
						.reduce(0,(txn1,txn2) -> txn.txnAmt + tx2.txn2)
						
						
final class customImmutable {
  public final int var;
}

Signleton design Patern

class Singleton{

	private static Connection conn;

	private Singleton(){

	}

	public static Connection getConnection(){
		Syncornized{
			if(conn != null) return conn

			conn = new Connection();
			return conn;
			}
	}


}


@Controller
class ProductController{

@RequestMapping(method="post")
public void insertProd(@RequestBody Product product){

ProductDao.

}


}



employee - id, name, departId
department  - id, name


I have to find the count of employee on each department


select count(emp.id), dep.name 
from department as dep Left Join employee as emp ON dep.id == emp.departId 
group by dep.id;










Aayush a
6:03 PM
transaction details - id, txnAmt, txntype
Aayush a
6:14 PM
String s1 = "hello";
String s2 = "hello";
String s3 = new String("hello");

syso(s1 == s2);
syso(s2 == s3);
syso(s1.equals(s3));
syso(s1.compareTo(s2));
You
6:14 PM
true
false
true
Aayush a
6:16 PM
try {
	return 1;
} catch (Exception e) {
	return 2;
} finally {
	return 3;
}
Aayush a
6:17 PM
try {
  // some line of code
} catch (Exception e) {

} catch (IOException ex) {

}
Aayush a
6:23 PM
syso(s1.compareTo(s2));
Aayush a
6:45 PM
employee - id, name, departId
department  - id, name





- HashMap-Concurrent, HashMap
- Scope of Bean Singleton and Prototype
- Collection.sort()
- ArrayList vs LinkedList
- How I can create an immutable class
- How can I create the singleton class
- In a singleton class if we implement the clonable interface then it would break the aspects of singleton. So How I can we do it and how we handle the thing.
- stream api I have to perfect a way more to crack the interview.
- Multithreading executor method what is that I have to use that.
- what would be the return type of compareTo method


- What is bean Scope
- what would be the default scope.
- What are the different types of scope it is not just 2.
- RequestBody and ResponseBody.
- @RestController vs @RestBody
- @Qualifier best question
- Different types of injection in springBoot
- How I can return the XML Object from the controller service.
  Producer Object media.Application_XML

- Microservices Communication 
- Circuit Breaker : How gone we implement it
- fallback
- Service Discovery and its 2 usecases and which one we are using/used.
- Distributed Tracing : logging with uid thow that we could track the request. 
- Which Api gatway have you used
- How could we build a communication between microservices: Sync/Async restApi and there is something more.

- Exception handling and in which order we catch the exception
- Can we connect multiple database with spring boot how.
- How can we insert the data in Product Table
- notify and notifyAll
- How could we can create an custom Immutable class object.
- Database Sql query employee and department


------------------------------------------------------------------------
## L2 Round Of Innowity

1. Simply Frequency Counting programme using spring.
2. There are 2 String given you have to merge in such a manner that sequence contains a1b1a2b2a3b3remaining at Last
3. @Transactional @Query 
4. How You would give expected time to your lead for this work
5. How you able to work and you are confident on your skill. 
6. Multithreading have you worked and executor framework.
7. Two Database connection
8. Kafka : offset
9. Junit or any testCases I have written.
10. SonarQube like Quality and code pratice analyser used, What is used in your compnay and how would you ensure your code quality over there.
11. Cloud Platform : AWS, Azure
12. Write a Rest Api which does some x work. what would be its flow
13. Solid Principle and Design Pattern


14. Spring Security Configuration pre/post authorization, Basic/JwtAuth in restApi
15. Implementation of Docker File.
16. Strema Api Practice Must

------------------------------------------------------------------------
## LogiTech Company Round


1. Learn Elastic-Search what are the indices how can we use it efficently.
2. What is Postgresh and how it is different from the mysql.
3. How GC Work and it used to clean up the Varible and free the allocated memory.
4. How Generics work and Why to use to use it?
5. what is this <?> I think its for optional.
6. @Transactional
7. SpringMVC VS SpringMVC
8. Finally block it is used for resource free or deallocation of resources Which is very crutial for application.
9. Try with resource we can use it 8 th point as alternative.
10. How to build some of sample springBoot application from screach


List x = new ArrayList<>();
x.add(123);
x.add(“asdf”);

Without the generics it run perfectly 


List<?> x = new ArrayList<>();
x.add(123);
x.add(“asdf”);
Try{
}finally{
}
Try{
//some code
}finally{
//some more code
}

Sourabh 2:52 AM
“Robot is a great programmer”

List x = new ArrayList();
x.add(123);
x.add(“asdf”);

------------------------------------------------------------------------

## Impetus

1. Solid what is l here.
2. Access Modifiers which access modifier has the greater visibility Default, Protected?
3. throw vs Throws
4. Compile Time and runtime Exception
5. HashMap vs HashSet internal implication
6. HashMap store the Null while TreeMap not why because of key sorting.
7. can we change the access modifier of an varible by inheriting it.
8. While performing inheritance we are overiding an method in subclass can we change its return type in subclass
Answer : Only if return type are related to each other.
No, it will not work. In Java, if you override a method in a subclass, the return type of the overridden method must be either the same as the method in the superclass or a subtype (covariant return type) of the return type in the superclass.

class Animal {
    Animal getAnimal() {
        return this;
    }
}

class Dog extends Animal {
    @Override
    Dog getAnimal() { // Covariant return type: Dog is a subclass of Animal
        return this;
    }
}

9. HashMap store distinct element how can it verify because in case of collition there would be multiple different key stored at the same place.

class Employee {
    String name;

    Employee(String name) {
        this.name = name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Employee employee = (Employee) o;
        return name.equals(employee.name);
    }

    @Override
    public int hashCode() {
        return name.hashCode();
    }
}

9. What if we create a custom object of employee class emp1, emp2 and make them as Key in hashMap and emp1 and emp2 has name attribute that store same name , both object treated as different in the HashMap?

By default, if you do not override the hashCode() and equals() methods in your Employee class, the HashMap will treat emp1 and emp2 as different keys, even if their name attributes are the same. This is because the default implementations of hashCode() and equals() in the Object class behave as follows:

10. Equals method in String class.

11. Spark vs Hadoop
12. Spark vs Hadoop vs Reduce vs Apache Hadoop
13. Spark RDD
14. Hands on Program to read the data and spark connection , read csv , filter emp with greater >1000, and then collect all those employee.
Here we can we use DF, But we have to do with rdd. -> in csv rdd we got the line we have to split by using map and then filter out those employee information 

15. How can we retrive the corrupted RDD in spark.
17. How can we detect the slow job in spark.

from pyspark import SparkConf, SparkContext

-> Step 1: Initialize Spark context
conf = SparkConf().setAppName("EmployeeFilter").setMaster("local")
sc = SparkContext(conf=conf)

-> Step 2: Read the CSV file as an RDD
lines = sc.textFile("path/to/employee.csv")

-> Step 3: Split each line by comma and map to a list of strings
employees = lines.map(lambda line: line.split(","))

// Assuming the CSV has the following format: ID, Name, Salary
// Salary is at index 2 in the list

-> Step 4: Filter employees with salary > 1000
filtered_employees = employees.filter(lambda emp: float(emp[2]) > 1000)

-> Step 5: Collect the filtered employees
result = filtered_employees.collect()

-> Print the results
for emp in result:
    print(f"ID: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}")

-> Stop the Spark context
sc.stop()


------------------------------------------------------------------------



Wheels eye
Google
aditya sir one company.





Expedia Referrals
Wheels Eye
SDE II - Backend Engineer Ad-Tech, JioCinema
Software Engineer II and unleash your potential at Wayfair!
https://www.wayfair.com/careers/thank-you?jobId=7557674002
https://autodesk.wd1.myworkdayjobs.com/Ext/job/Novi-MI-USA/Java-Software-Engineer--Hybrid-_24WD79661?src=JB-10065&source=LinkedIn
Atomicwork
https://www.linkedin.com/company/honeywell/people/ : P HoneyWell
https://voidcareers.in/f/honeywell-is-hiring-software-engineer
ServiceNow Krish

PayPal : Shivani Refferal


/*
Welcome to JDoodle!

You can execute code here in 88 languages. Right now you’re in the Java IDE.

  1. Click the orange Execute button ▶ to execute the sample code below and see how it works.

  2. Want help writing or debugging code? Type a query into JDroid on the right hand side ---------------->

  3.Try the menu buttons on the left. Save your file, share code with friends and open saved projects.

Want to change languages? Try the search bar up the top.
*/
import java.util.*;
import java.util.stream.*;

public class MyClass {
  public static void main(String args[]) {
      
    int arr[] = new int[]{1,2,3,4,5,5};
    
    // Arrays.stream(arr).forEach(System.out::println);
    
// 1------------------------------------------------------------------------------------------------------------------------------
    
    // List<Integer> list = Arrays.asList(1,23,4,4,5,6,6);
    
    // int sum = list.stream().filter(x -> x%2==0)
    //                         .reduce(Integer::sum)
    //                         .orElse(0);
    
//reduce method in this case returning the Optional<Integer> so by using orElse(0) : it there value return actual one otherwise 0.

// 2------------------------------------------------------------------------------------------------------------------------------

    List<Integer> list = Arrays.asList(1,23,4,4,5,6,6);
    int sum = list.stream().filter(x -> x%2==0)
                            .reduce(0,(a,b) -> a+b);
                            // .orElse(0);
//Why rededuce not return optional in this case.
// Optional<T> reduce(BinaryOperator<T> accumulator):
// T reduce(T identity, BinaryOperator<T> accumulator)
// <U> U reduce(U identity, BiFunction<U, ? super T, U> accumulator, BinaryOperator<U> combiner):
// This version is used in parallel streams and involves a combiner function to combine partial results.


// 3------------------------------------------------------------------------------------------------------------------------------    
    
//we are not able to use sum(), count() method because it is decleared in premitiveStream IntStream, DoubleStream
// specialized streams like IntStream, LongStream, and DoubleStream, which are primitive specializations of the Stream interface.
//So It is always must to convernt the Stream<Integer> into IntStream<Integer> and then apply the operations;

    // sum = list.stream()
    //           .filter(x -> x % 2 == 0)
    //           .mapToInt(Integer::intValue)
    //           .sum();
    
    //Here we have convered intStream into the double and then took sum from that
//     double sum2 = list.stream()
//                  .filter(x -> x % 2 == 0)
//                  .mapToDouble(Integer::doubleValue) // Correct mapping
//                  .sum();
                 
                 
//  double sum = list.stream()
//                  .filter(x -> x % 2 == 0)
//                  .mapToDouble(Integer::doubleValue) // Correct mapping
//                  .sum();

//     System.out.println(sum2);

    List<Integer> input  = Arrays.asList(1,2,3,3,22,5,3,2,5,26,27);

// List<String> ans =  input.stream().map(x -> String.valueOf(x))
//                                     .filter(x -> x.charAt(0)=='2')
//                                     .collect(Collectors.toList());
    
    // Set<Integer> ans = input.stream().filter(x -> Collections.frequency(input, x) > 1).collect(Collectors.toSet());
    
    
//   Map<Integer,Integer> map =  input.stream().distinct().collect(Collectors.toMap(x -> x, x -> Collections.frequency(input, x)));


int  map = input.stream().max((a,b) ->  b-a).get();
    
    
    
    System.out.println(map);
 
  }
}

## UKG

### Round 1
1. Final class member variable vs public member variable in springBoot.
2. Stream Api producer, consumer.
3. How could we create immutable class
4. Try-catch
5. LinkedList nth node from the last.
6. Find the Height of the tree.
7. @Transactional & its diffrent propagations types.
8. Locking vs custom Locking
9. Sql-Query
10. What is filter
11. Puzzle one question you have given like 8 balls and there is one old ancient wheight balancing machine.

### Round 2
1. Book-My-Show Schema-Design. 
2. 2 Pointer algoritihm.
3. Sql question to get last2nd salary.
4. Rank Vs Dense Rank
5. Solr related Questions have asked


## Walmart Global Tech Coding round

1. Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
 
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
 
You must solve this problem without using the library's sort function.
 
Example 1:
 
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
 
 
 
Example 2:
 
Input: nums = [2,0,1]
Output: [0,1,2]


2. Shortest Subarray to be Removed to Make Array Sorted
=====================
Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
 
Example 2:
Input: arr = [5,4,3,2,1]
Output: 4
 
Example 3:
Input: arr = [1,2,3]
Output: 0


{3,3}

{10, 1}
{4,1}



Map map;
Int I =0
For ( int ele : arr) {

Map.put(ele, )
}
## Zimeterics
1. Immuatable class implementaion
2. Find first occurance of element.
3.  Filter
4. Sql writing something


## RiseSmart by Randstand

1. Spring-Boot
2. coding question 
3. what if there is class A which is instansiated with the new keyword and A class has dependecy with B and C and it used dependecy injection. So it will be able to resolve the dependency or not.
4. Compile time and Runtime Overiding and resolution of data-type.
5. Compile time overriding.

## Go-Daddy Interview 

1. Remove-LinkedList Node question.
2. which SpringBoot version is used if used the old one then 
3. JPA and Hibernet and Hibernet cache l1 and l2
4. Different states of hibernet.
5. Transaction management and diffrent propagation 
6. If you have miroservice then how would handle the distributed transactions.
7. HashMap internals and while using Object as key needed things to override -> equals and hashcode method to uniqely identify it.
8. How and What is the need of ConcurrentHashMap and which time of inconsistenecy of data occured while using normal not threadsafe HashMap.

## MinTech for JavaDeveloper Role
1. Dependency injection types : constructor(mandatored dependecy injection), setter(optional dependency injection), field based(visibility less, Junit complicate)
2. SpringBootTest vs Mockito : SpringBootTest -> we can utilize the springboot context here in the test cases while in Mockito we can't.
3. Bean ? -> Java object which is managed by spring
4. Multithreading and ExecutorService
5. @Async , @Scheduler(cron="*******")
6. @EnableAutoConfiguration(exclude="")
7. @SpringBootApplication -> @Configuration, @ComponentScan(path="/*"), @EnableAutoConfiguration
8. How could we create custom AutoConfiguration class ?
9. @Pageable
10. What is profile in spring-boot.
11. Microservice -> configServer, Zepkin, ServiceRegistry.

## TrueMeds For Senior Java developer

List<Product> ->
Product -> comanyName, ProductCode, PName


listProduct.stream()
.collect() 


Write a query to count the number of orders placed by each customer. Return only those who placed more than 5 orders.

Order -> id , custID
Select customer_id, count(order_id)
From order
group by customer_id
having count(order_id) > 5



Pankaj Patil
4:06 PM
https://leetcode.com/problems/container-with-most-water/description/
Pankaj Patil
4:56 PM
Write a query to count the number of orders placed by each customer. Return only those who placed more than 5 orders.
You
4:59 PM
Select customer_id, count(order_id)
From order
group by customer_id
having count(order_id) > 5


Map<String, List<Product>> groupedByCompany = products.stream()
            .collect(Collectors.groupingBy(Product::getCompany));
            
1. Constuctor Injection vs @AutoWired
2. Index how it internally works
3. How to design Api rate limiter and which datastructure is used for that
4. catch and finally block : 
	try {
		return 10;
	}
	catch () {

	}
	finally {
		return 20;
	}

ans : 20 because finally always runs it would suppress the try block return statement, There is case if System.exit(1) present in the try block then finally block would be execute as it interuppt the program itself.

5. @Query native and HPQL How can we decide: There is attribute nativeQuery = true.
6. SteroTypeAnnotation
7. What If in Repository class but @Service annotation , would we get any problem with it.
9. Except than JPARepository what are other 2 ways to execute DTO opration in SpringBoot query.
10. STREAM-QUESTION
11. FUNCTIONAL INTERFACE
12. How to debug a task.
13. Connection Polling
14. Indexes
15. Sharding DB.
17. How to solve dependency cycle problem.
18. What are the different strategy or type in which we can AutoIncrement @Id @GeneratedValue(strategy= )


## Cyient 

Java Interview questions 

1. How does the Java Stream API handle parallelism internally? What are the best practices for parallel streams?
2. What is the difference between final, const, and immutable in Java?
3. Explain how the PhantomReference class works and its use cases.
4. How does Java's CompletableFuture handle exceptions? Explain with an example.
5. What are the main differences between Hashtable and ConcurrentHashMap?
6. What is the role of Unsafe class in Java? Why should it be used cautiously?
7. Describe how you would implement a thread-safe singleton in Java.
8. What are Java annotations retention policies, and why are they important?
9. How do you implement a custom serializer/deserializer in Jackson for JSON processing?
10. What is the difference between Predicate, Function, and Consumer functional interfaces?

# Inteview Experience Cyient : 

1. Compile time and runtime polymorphism
2. SCP
3. Runnable and callable 
4. Encapsulation and abstration
5. IOC
6. Spring Intializer
7. @Autowired
8. Interface vs abstract class
9. @Controller Vs @RestController
10. Region and availability Zone
11. What is Keypair in S3: ssh public and private key pair for ec2 instance access.
12. EC2 instances
13. Pricing EC2 instancs
14. Princing S3 Instaces
15. Limit on S3 bucket creation. : Yes
16. CloudFront
18. CloudWatch

https://medium.com/@sujathamudadla1213/amazon-s3-bucket-creation-limitations-973d806a899f

# HCL Interview

1. Kadane algorithm
2. OoPS conecept and how it works in Java : Encapsulatio, Inheritance, Polymorphism, Abstraction
3. Return Type overloading.
4. Fail-safe and fail-fast in collection.
5. Volatile and AtomicInteger
6. transient vs @Transient annotation.
7. @EnableAutoConfiguation vs @ConditionalOnMissingBean @ConditionalOnClassLoad
8. Externalizable 
9. ArrayList vs LinkedList
10. What are the predefined functional-interface.
11. Association, Composition (stronger form of association), aggregation(Weaker form of association )



Question: What is Externalizable ?

Externalizable is an interface in Java (part of java.io package).
It is used for custom serialization and deserialization.
It extends Serializable interface, but gives you complete control over what and how to serialize/deserialize.

void writeExternal(ObjectOutput out) throws IOException;
void readExternal(ObjectInput in) throws IOException, ClassNotFoundException;

Question: Fail-safe and fail-fast in collection.

Ans -> A fail-fast iterator immediately throws a ConcurrentModificationException if you modify the collection (add/remove/update) structurally while iterating over it (except using iterator’s own remove() method).

A fail-safe iterator does not throw ConcurrentModificationException, even if the collection is modified during iteration.
It works on a clone (copy) or snapshot of the collection.

Example: 
	- ConcurrentHashMap
	- CopyOnWriteArrayList
	- CopyOnWriteArraySet


Question: What are the predefined functional-interface

Function<T, R>        → T → R
BiFunction<T, U, R>   → (T, U) → R
Predicate<T>          → T → boolean
BiPredicate<T, U>     → (T, U) → boolean
Consumer<T>           → T → void
BiConsumer<T, U>      → (T, U) → void
Supplier<T>           → () → T
UnaryOperator<T>      → T → T
BinaryOperator<T>     → (T, T) → T

Question : @EnableAutoConfiguation vs @ConditionalOnMissingBean @ConditionalOnClassLoad?
@EnableAutoConfiguration
        ↓
@Import(AutoConfigurationImportSelector)
        ↓
Reads META-INF/spring.factories
        ↓
Loads and registers auto-config classes
        ↓
Conditions decide which beans to create

Question: Volatile vs Atomic Integer



--------------------------------------------------------------------
# AWS

## AWS S3 limitation

- Bucket names must be globally unique and not IP-like.

- Bucket ownership stays with the creator; cannot transfer.

- Region is fixed after creation; can’t change.

- Default limit: 100 buckets per region (can request increase).

- No bucket size limit; single object max 5 TB.

- High request rates may cause throttling (503 errors).

- Access control must be configured carefully.

- Cannot rename buckets once created.

- Enable logging/versioning for safety.

- Buckets can be deleted only when empty; names reusable after ~24 hrs.

Ques. What are amazone AWS Services which is not region specific ?
Ans -> Route53, AWS IAM and Aws cloud-front

Ques. EC2 va Lambda

- Amazon Ec2 provide virtual serviers that you mange, while Aws lambda runs code in response to events and scales automatially.

- Choose EC2 for long-running taks or when you need more control over the environment.
	- example: hosting a website with specific software requirements or running a db server.

- Choose Lambda for even-driven, short-lived taks with automatic scalling. 
	- example : processing even-driven actions such as file uploads, database updates, or API requests, S3 event-driven action we can start.
	
Question:  Cloud-Formation 
Question: In VPC with private and public subnets, database servers should ideally be launched into whihc subnet ? NAt instances 

---------------------------------------------------------------------------------------------
# Work

1. Ay -ongoing
2. Tmax-AdScript
3. Mywork	
	
	
📌 LLD

1. Design a parking lot management system (Can be multilevel)
 2. Design Chess Game
 3. Design LRU Cache
 4. Design Tic Tac Toe Game
 5. Design a threadsafe hashmap.
 6. Design Rate-Limiter.

📌 HLD

1. Design a URL shortening service like tinyUrl.
 2. Design a distributed key-value store.
 3. Design a real-time messaging system like WhatsApp.
 4. Design a distributed cache like Memcached.
 5. Design a ride-sharing system like Uber.

This is based on both personal experience and what’s trending in real interviews.

Once I focused on understanding the “why” behind every component, things started clicking, and offers started coming.


--------------------------------------------------------------------------------------------------------------------------