That is first define an abstract class, program to that (write tests) and then follow up with the implementation.  

```python
from abc import ABC, abstractmethod

def Animal(ABC):
	@abstractmethod
	def sound(self):
		pass
		
def Dog(Animal):
	def sound(self):
		print("Woof!")

def Cat(Animal):
	def sound(self):
		print("Meow!")
		
def talking(sender: Animal, receiver: Animal):
	sender.sound()
	receiver.sound()