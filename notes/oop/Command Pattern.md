By converting a function into an object you can more easily extend it while passing around the "state" of the program.

The authors also note that it's helpful that these arn't tied to any parent class, and thus a different type other than a Menu could hold a single object that executes the same functionality, with the same state.

The Command pattern prescribes a uniform interface for issuing requests that lets you configure clients to handle different requests. 

Is this right?? 
Think of a web application that might take a Request interface type.  Depending on the current context (they are on a certain page or authenticated as an admin) then the central service can then safely decide what to do with such Request.  Maybe they shepard it out to proxy service or connect to a databse.


![[Pasted image 20210328003931.png]]

#oop #pattern