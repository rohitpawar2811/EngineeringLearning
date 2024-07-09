## JS Learnings

1. Function inside function
2. Closure : It is related to binding.
3. Function-Factory : function takes a param and then inside a function decalared in which upperparm will binds and top one return child function. and we can pass parm to that child and child will calculate the value from topPram(binded) + childPram
 4. Callback-Function : function passing to function is called a callback function.
 5. Function Statements : Function method, function expression just diffrence is that method will got memory at the time comiling, but functional expression got memory at the runtime.
 6. Script has 2 mode of loading : differ, async
 7. Callback in SetTimeout(callback,2000) : Here Browser lets CallStack to execute for 2000 and then callback function executes.
 8. CallbackHell : Here callbackHell use is deprecated because if creates problem when we have to wait for undesired amount of time if something missed whole thing broked up. Now we are using promise for this purpose.
 9. Promise: It just executes its execution async and based on result it will return {reject,resolve} and on top of these response we can perform some actions. 
    1. And for doing so we can use
        - then : It will perform for both resolve and reject scenerios.
        - catch : Here we got the reject one response and the Exception is catched here because we know in then clause on performing some action we can get the exception so we can use this.
        - finally : Which executes surely at the end
    2. Here we can chain those 3 in the sequences.
    3.promise.all([]).then().catch() : Here we can execute multiple promise at once.
10. throw new Error("error msg") : just custom exception throwing.
11. async-await : It is upgraded/extended version to handle promise.
12. Architecture: I have to look on it,
    Components : 1. Call-Stack 2. Event-loop 3. Web-Api-Broker 4. Callback Queue 5. Mtq Micro-TaskQueue (Here )

13. CORS

