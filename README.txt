The Hydroflask class is a representation of a real life Hydro Flask water bottle. 
Each Hydroflask object has a custom owner, color, and size, each of which are represented by data variables.


The owner data variable is a string representing the Hydroflask owner's name.
The color data variable is a string representing the Hydroflask's color.
The size data variable is a float representing the maximum amount of water (in ounces) that the Hydroflask can contain.
The water data variable is a float representing the current amount of water in the Hydroflask.
If no amount of water is given, the default value is set to the Hydroflask's size.


Each data variable has its respective get method which returns the value of the data variable.
These methods do not take arguments.

The fill method 'fills' up the Hydroflask, setting the amount of water in the object to the Hydroflask's size.
It takes no arguments, and has no return value.

The drink method takes in a float argument, and subtracts it from the object's current amount of water.
If the operation would result in a water value less than or equal to 0, the water amount is set to 0.
An 'empty' message is also printed if the Hydroflask contains no water.
The method has no return value.


The demo program creates two unique Hydroflask objects and performs the drink and fill methods on each one.
The amount of water in each object is also printed to show the effect of each method call.
