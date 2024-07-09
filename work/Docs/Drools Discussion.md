Drools is rule-based Engine
Intitally we started from moqui where a kie component is exposed. and we can pass our object and based on that.
we would apply some condition and apply actions
in action we store the result and in service we would get that
and based on that we took decision with results

Here we done things like grouping ,dependent rule execution, priority, ordering

At last Problem we are getting is formatting with manual edits in linux word, it is providing unexpected outcomes.
which leads to stop this task.


Part 2.

Here we started from GUI, and we tried to test what capability does it have

Here in GUI we can create the rule , we can get the data from rest there are custom task compoenets. 
But configuring and capability are so much less and not suites our requiremnt

IT is like CRM BPMN

Here we tries the GUI Rest Capability but passing a nested object like order with multiple order-item is so much complex task. but it works 

we have to pass it in json and on the other side we have to make a form where we have to configure manually 
and litterally that thing is too bugy.

2nd thing we tested is GUI but too complex for that reason we drop the idea 


we can discuss the architecture if you want it 

main and have some delegatore where the all rule will be published.

Final blocker
UI sa spread sheet mai likhna, parsing, rule changing throw api its manual task and tedious.