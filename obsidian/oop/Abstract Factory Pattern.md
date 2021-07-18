This allows you to initalize at compilation time, run-time, through user input, or from system lookup.  System designers can then implement their own factory, saving you the work of porting to every variation.  

Note:  These usually materialize around creating families of objects as opposed to single classes or instances as seen with the [[Composite Pattern]].
```
lexi.gui_factory = WindowsFactory()
lexi.button = lexi.gui_factory.create_button()
lexi.gui_factory.draw_button()

lexi.gui_factory = MacFactory()
lexi.button = lexi.gui_factory.create_button()
lexi.gui_factory.draw_menu()
```

![[Pasted image 20210328001058.png]]

Lastly, note again the focus on creating a factory per interface, and then an abc for factories in general.  [[Principal - Program to an interface, not an implementation | Program to the interface.]]


#oop #pattern