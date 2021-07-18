The intention here was to easily be able to replace the linebreaking algorithm without having to change a bunch of classes.  By using composition you can enable run-time changes.

Creating a Glyph subclass called a Composition which maintains a list of children which are also glyphs.  It also maintains a pointer to a second class which has a factory method/member of it's own. 

Not sure how this isn't the [[Bridge Pattern]] whereby you can have a classes move independently from each other.

By [[Principal - Program to an interface, not an implementation | programming to an interface]] you've encapsulated any changes from the algorithm.  New algorithms can be picked up instantly as long as they implement the interface correctly.

```
from lexi import Composition
from lexi.compositor import ArrayCompositor, TexCompositor

composition = Composition([Glyph("G"), Glyph("car.png")], ArrayCompositor)
composition.draw()

composition.setCompositor(TexCompositor)
composition.draw()
```
![[Pasted image 20210327225836.png]]

This also mirrors the [[Strategy]] design pattern. ??

#oop #pattern