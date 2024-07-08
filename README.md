# number_to_french_converter

Convert a number to a french word.

### Installation

Clone to directory to your local computer:
```git clone xxx```

### Use

Following options exist to run the code:
- Provide numbers separated by a space: ```python main.py --list_numbers 0 10 893 3211```
- Provide numbers as a string in list format: ```python main.py --list_numbers_str "[21, 94, 345, 4000, 894534]"```

In addition you can add the flag ```--lang``` with possible values ```french``` or ```belgium``` to change the accent. 
The default value is french.

Ex.: 
- ```python main.py --lang belgium --list_numbers 0 10 893 3211```
- ```python main.py --lang french  --list_numbers_str "[21, 94, 345, 4000, 894534]"```

