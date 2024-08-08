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

Distributed tracing
How would we can communicate to our api to other api
Microservices 
How we can build a microservices using **docker** and how we are able to deploy in the containerized environement. 

StreamAPi
@Qualifier
@GlobalExceptionHandling
@Bean Vs @Component
@ConfigurationPropertie
Kafka and Zookeeper
One Programming based question : reversal programme
Java Concept Spring Bean what is lifecylce

OOPs why to use ops in project?
Design Pattern I would know
Runtime polymorophish
Docker
PortForwarding
RestTemplate
Apache Solr what is that and how you integrate in springBoot system.? Let US Know

Updated Solr Doc SolrInputDocument(fields: [picklistItemStatusId={set=PICKITEM_COMPLETED}, shipmentStatusId={set=SHIPMENT_SHIPPED}, itemShippedDate={set=Mon Jul 22 22:54:14 EDT 2024}, orderStatusId={set=ORDER_COMPLETED}, picklistItemStatusDesc={set=Completed}, docType-identifier=OISGIR-43439-00101-00001-90533, updatedDatetime={set=Mon Jul 22 22:54:14 EDT 2024}, fulfillmentStatus={set=Completed}])

------------------------------------------------------------------
Question 1.
Regression vs Re-testing , smoke vs sanity testing , bug life cycle , sdlc & stlc, api testing related questions , database testing questions.
------------------------------------------------------------
Question 2.
Oops Concepts & Automation API & UI
---------------------------------------------------------------------

questions.
1. clouser
2.let and var hoisting concept
3. shallow and deep copy

------------------------------------------------------------



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
