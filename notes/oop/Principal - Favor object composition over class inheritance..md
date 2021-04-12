Rather than subclass employee as person, we can use composition.  Think "has a" or "uses a" when picking this methodology.


```java
// https://stackoverflow.com/questions/49002/prefer-composition-over-inheritance
class Person {
   String Title;
   String Name;
   Int Age;

   public Person(String title, String name, String age) {
      this.Title = title;
      this.Name = name;
      this.Age = age;
   }

}

class Employee {
   Int Salary;
   private Person person;

   public Employee(Person p, Int salary) {
       this.person = p;
       this.Salary = salary;
   }
}
```