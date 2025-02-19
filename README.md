# number_to_french_converter

Convert a number to a french word.

### Installation

1. Clone to directory to your local computer:
```git clone https://github.com/Adahn/number_to_french_converter.git```
2. Go into the cloned directory: ```cd number_to_french_converter```

### Use

Following options exist to run the code:
- Provide numbers separated by a space: ```python src/main.py --list_numbers 0 10 893 3211```
- Provide numbers as a string in list format: ```python src/main.py --list_numbers_str "[21, 94, 345, 4000, 894534]"```

In addition you can add the flag ```--lang``` with possible values ```french``` or ```belgium``` to change the accent. 
The default value is french.

Ex.: 
- ```python src/main.py --lang belgium --list_numbers 70 73 89 90```
- ```python src/main.py --lang french  --list_numbers_str "[21, 94, 345, 4000, 894534]"```

