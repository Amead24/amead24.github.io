class that determines how classes are created

see type object instantiation for more details

```python
class Meta(type):
	def __new__(self, base, name, dict):
	    new_dict = copy(dict)
		new_dict["foo"] = lambda self: print("bar")
	    return __new__(self, base, name, new_dict)
		
class Base(metaclass=Meta):
	pass
	
base = Base()
base.foo()
bar
```

More advanced example of dynamically creating Data-API functionality:

```python
FUNCTIONS = [
    {
		"name": "losses", 
		"args": ["start", "end"], 
		"account": "pricing", 
		"async": True
	},
    {
		"name": "premium", 
		"args": ["high", "low"], 
		"account": "pricing", 
		"async": False
	},
]

def query_api(self, account, async_status, *args, **kwargs):
    print(args, kwargs)


class DataAPIMeta(type):
    def __new__(cls, what, bases=None, dict=None):
        new_dict = dict
        for function in FUNCTIONS:
            # args = ", ".join(function["args"])
            # new_dict[function["name"]] = eval(f"lambda self, {args}, *args, **kwargs: print({args}, args, kwargs)")

            new_dict[function["name"]] = eval(f"query_api(account={function['account']}, async_status={function['async']}, *args, **kwargs)")

        return type.__new__(cls, what, bases, new_dict)

    def __init__(self, name, bases=None, dict=None):
        self.api = "https://data-api.com"


class PricingAPI(metaclass=DataAPIMeta):
    pass
	
	
pricing = PricingAPI()
pricing.losses(start="2020", end="2021")