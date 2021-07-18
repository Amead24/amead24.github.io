everything in python is an object, classes inherit from Object.  Under the hood all objects are CPython pointers to a PyObject C struct.  

type is it's own type but also is an object while object has no type.

Type is of type `type`.

All objects could implement __call__() to make it callable.  When a Call is parsed by the AST CPython will push the keyword parameters, positional parameters and lastly the function object itself is pushed onto the stack.  These get popped off then, evaluated, and the return value pushed back onto the stack.

#complexity-analysis