import ChaiScript as ChaiScript
import os



def display_intro():
    ASCII_art = """
::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::
::::::::::::::;;;;::::::::::::;:::::::::
::::::::::;*%#@@@@#S?+::::+%##@##%+:::::
:::::::::*#@@#%??%S@@@S;:%@@@#S#@@@*::::
::::::::?@@@*::::::;?S*;;@@@S:::+*;:::::
:::::::;@@@*:::::::::::::S@@@S?+;:::::::
:::::::+@@@;:::::::::::::;?#@@@@@S?;::::
:::::::;@@@+::::::::::::::::+*%#@@@@*:::
::::::::%@@#+:::::::*?+;:;+;::::+@@@#:::
:::::::::?@@@S?***?#@@#+%@@#?*+*%@@@S:::
::::::::::;?S@@@@@@@S*;:+%#@@@@@@@@%;:::
:::::::::::::;;+++;:::::::;+**??*+;:::::
::::::::::::::::::::::::::::::::::::::::
    """

    print("ChaiScript Terminal (v - 1.1.0) - Created by Zishan (2025)")
    print(ASCII_art)
    print("Available commands:")
    print("  help - Show the help message")
    print("  run(\"filename\") - Run an external ChaiScript file")
    print("  exit - Exit the terminal")
    print()

def help_system(displayed):
    if not displayed:
        help_text = """
    Welcome to ChaiScripts 1.1.0's help utility!

    Dictionary and Exception Handeling has been added in this new version.
    For more, Please visit our documentation

    If this is your first time using ChaiScript, you should definitely check out
    the tutorial on the internet at zishan108.github.io/Zishan108-ChaiScript-Website-By-Zishan .
    
    To quit this help utility and
    return to the interpreter, just type "quit".

    To get a list of available keywords, symbols, escape sequence characters or built-in functions, type
    "keywords", "symbols", "escape" or "built"
        """
        print(help_text)
        print("Available topics:")
        displayed = True
    else:
        print("Available topics:")  # Only show available topics on subsequent calls

    print()
    return displayed, input("help> ").strip().lower()

def display_commands_help():
    commands_help = """
Available Commands:
  help               - Show this help message
  run(\"filename\")     - Run an external ChaiScript file
  exit               - Exit the terminal
"""
    print(commands_help)

def display_keywords_help():
    keywords = [
        'cup                # variable declaration',               
        'and                # and operator',               
        'or                 # or operator',                
        'not                # not operator',               
        'hot                # if',                
        'mild               # else if',              
        'chilled            # else',           
        'for_chai          # for loop',          
        'to_chai           # to keyword',           
        'STEP               # step',              
        'while_chai        # while loop',        
        'brew               # function',              
        'then_chai         # then keyword',         
        'sip                # end statement',               
        'return_chai       # return keyword',       
        'continue_chai     # continue keyword',     
        'break_chai        # break keyword',        
    ]
    print("ChaiScript Keywords:\n")
    for keyword in keywords:
        print(f"  {keyword}")
    print()

def display_symbols_help():
    symbols = {
        '+': 'Addition or Append elements operator for List',
        '-': 'Subtraction or Pop elements operator for List',
        '*': 'Multiplication or Concatenation operator for List',
        '/': 'Division or indexing operator for List',
        '^' : 'Power Operator',
        '==': 'Equal to',
        '!=': 'Not equal to',
        '>': 'Greater than',
        '<': 'Less than',
        '>=': 'Greater than or equal to',
        '<=': 'Less than or equal to',
        'and (keyword)': 'Logical AND',
        'or (keyword)': 'Logical OR',
        'not (keyword)': 'Logical NOT',
        '=': 'Assignment',
        '()': 'Parentheses',
        '[]' : 'Brackets (List Comprehension)',
        '#': 'Single-line comment',
        '->' : 'Arrow Operator (used for return statements in single line)',
        '{}' : 'Braces (Dictionary Comprehension)'
    }
    
    print("ChaiScript Symbols:\n")
    for symbol, description in symbols.items():
        print(f"  {symbol} - {description}")
    print()

def display_escape_characters_help():
    escape_chars = {
        '\\n' : 'Inserts a new Line',
        '\\\\' : 'Inserts a literal backslash',
        '\\t' : 'Inserts a horizontal tab'
    }
    
    print("ChaiScript Escape Sequence Characters:\n")
    for chars, description in escape_chars.items():
        print(f"  {chars} - {description}")
    print()
    
def display_builtIn_functions_help():
    utility_funcs = {
        'serveChai(arg)'       : 'Prints onto screen/system output',
        'serve_ret(arg)'       : 'Prints and returns the print value onto screen/system output',
        'orderChai(arg)'       : 'Takes input from the user through system in drivers and prints the arguments (argument is mandatory)',
        'orderChai_int(string)': 'Takes Number input from the user through system in drivers and prints the arguments (argument is mandatory)',
        'clean()'              : 'Clears the ChaiScript Terminal',
        'cls()'                : 'Clears the ChaiScript Terminal',
        'type_chai(arg)'       : 'Returns the type of the argument (String/Number/List/Null/Boolean)',
        'current_date_time()'  : 'Returns Current date and time',
        'list_len(list)'       : 'Returns the length of the list (arg should be list only)',
        'str_len(string)'      : 'Returns the length of the String (arg should be String only)',
        'len(arg)'             : 'Returns the length of any datatype',
        'int(arg)'             : 'Returns and Coverts arg datatype to integer datatype',
        'str(arg)'             : 'Returns and Coverts arg datatype to String datatype' ,
        'float(arg)'           : 'Returns and Coverts arg datatype to float datatype' ,
        'time_freeze(int)'     : 'Returns and Stops the flow of execution of program for specified amount of seconds (useful for Multithreading)' 
    }
    
    boolean_funcs = {
        'is_chai_num(arg)'  : 'Returns true if the arg is a ChaiScript Number',
        'is_chai_str(arg)'  : 'Returns true if the arg is a ChaiScript String',
        'is_chai_list(arg)' : 'Returns true if the arg is a ChaiScript List',
        'is_brew(arg)'      : 'Returns true if the arg is brew (ChaiScript Function)',
        'is_empty(arg)'     : 'Returns true if the arg is empty ("", [], null)'
    }
    
    list_funcs = {
        'append(list, arg)'            : 'Returns and appends the arg into the list',
        'pop(list, arg)'               : 'Returns and pops the arg index value from the list',
        'extend(list1, list2)'         : 'Returns and adds list1 into list2',
        'sort_list(list)'              : 'Returns the sorted list',
        'reverse_list(list)'           : 'Returns the reversed list',
        'range(start, end, step)'      : 'Returns a list from `start` integer to `end` integer with `step` steps',
        'element_at(list, index)'      : 'Returns the value at passed index in the list',
        'join_to_str(list, delimiter)' : 'Returns and converts the list into a string with a specified delimiter'
    }
    
    string_funcs = {
        'to_lower(string)'                                       : 'Returns and converts the string to lower cased',
        'to_upper(string)'                                       : 'Returns and converts the string to upper cased',
        'char_at(string, index)'                                 : 'Returns the character at specified index in the specified string',
        'index_of(string1, string2)'                             : 'Returns the index of string2 in string1',
        'slice(string, start_index, end_index, step)'            : 'Returns the sliced string or substring from start_index to end_index (exclusive) with the given steps',
        'starts_with(string1, string2)'                          : 'Returns true if the string1 start with string2',
        'ends_with(string1, string2)'                            : 'Returns true if the string1 ends with string2',
        'trim(string)'                                           : 'Returns and trims the trailing spaces from the string',
        'replace(string, string_to_replace, string_replacement)' : 'Returns and replaces string_to_replace in string with string_replacement',
        'split_to_list(string, delimiter)'                       : 'Returns and converts the string into a list with specified delimiter',
        'capitalize(string)'                                     : 'Returns and converts the string to a Capitalized string',
        'title(string)'                                          : 'Returns and converts the string into a Title cased string',
        'is_equals(string1, string2)'                            : 'Returns true if the string1 is equal to string2'
    }
    
    Math_funcs = {
        'Math_PI'  : 'Returns the constant Pi value',
        'Math_E'   : 'Returns the constant Euler\'s (e) value\n',
        
        'Math_mod_div(x, y)'      : 'Returns the remainder when x is divided by y',
        'Math_factorial(x)' : 'Returns the Factorial of x',
        'Math_sqrt(x)'      : 'Returns the square root of x',
        'Math_floor(x)'     : 'Returns the floor value of x',
        'Math_ceil(x)'      : 'Returns the ceil value of x',
        'Math_round(x, decimals)'     : 'Returns the round up value of x with specified number of decimals',
        'Math_absoluteval(x)' : 'Returns the absolute value of x',
        'Math_random_chai(min, max)' : 'Returns random integer from min arg to max arg\n',
        
        'Math_sin(x)' : 'Returns sin value of x',
        'Math_cos(x)' : 'Returns cos value of x',
        'Math_tan(x)' : 'Returns tan value of x',
        'Math_sec(x)' : 'Returns sec value of x',
        'Math_cosec(x)' : 'Returns cosec value of x',
        'Math_cot(x)' : 'Returns cot value of x\n',
        
        'Math_arcsin(x)' : 'Returns inverse sin value of x',
        'Math_arccos(x)' : 'Returns inverse cos value of x',
        'Math_arctan(x)' : 'Returns inverse tan value of x',
        'Math_arcsec(x)' : 'Returns inverse sec value of x',
        'Math_arccosec(x)' : 'Returns inverse cosec value of x',
        'Math_arccot(x)' : 'Returns inverse cot value of x\n',
        
        'Math_sinh(x)' : 'Returns the hyperbolic sin value of x',
        'Math_cosh(x)' : 'Returns the hyperbolic cos value of x',
        'Math_tanh(x)' : 'Returns the hyperbolic tan value of x',
        'Math_sech(x)' : 'Returns the hyperbolic sec value of x',
        'Math_cosech(x)' : 'Returns the hyperbolic cosec value of x',
        'Math_coth(x)' : 'Returns the hyperbolic cot value of x\n',
        
        'Math_arcsinh(x)' : 'Returns the hyperbolic inverse sin value of x',
        'Math_arccosh(x)' : 'Returns the hyperbolic inverse cos value of x',
        'Math_arctanh(x)' : 'Returns the hyperbolic inverse tan value of x',
        'Math_arcsech(x)' : 'Returns the hyperbolic inverse sec value of x',
        'Math_arccosech(x)' : 'Returns the hyperbolic inverse cosec value of x',
        'Math_arccoth(x)' : 'Returns the hyperbolic inverse cot value of x\n'
        
    }
    
    print("ChaiScript Utility Functions:\n")
    for util_funcs, description in utility_funcs.items():
        print(f"  {util_funcs} - {description}")
    print()
    
    print("ChaiScript Boolean Functions:\n")
    for bool_funcs, description in boolean_funcs.items():
        print(f"  {bool_funcs} - {description}")
    print()
    
    print("ChaiScript String Functions:\n")
    for str_funcs, description in string_funcs.items():
        print(f"  {str_funcs} - {description}")
    print()
    
    print("ChaiScript List Functions:\n")
    for l_funcs, description in list_funcs.items():
        print(f"  {l_funcs} - {description}")
    print()
    
    print("ChaiScript Utility Functions:\n")
    for util_funcs, description in utility_funcs.items():
        print(f"  {util_funcs} - {description}")
    print()
    
    print("ChaiScript Math Functions:\n")
    for math_funcs, description in Math_funcs.items():
        print(f"  {math_funcs} - {description}")
    print()
    
    
# Display the introduction
display_intro()

# Initialize help display flag
help_displayed = False

while True:
    text = input('ChaiScript > ')
    
    if text.strip() == "":
        continue
    elif text.strip().lower() == "help":
        while True:
            help_displayed, topic = help_system(help_displayed)
            if topic == "commands":
                display_commands_help()
            elif topic == "keywords":
                display_keywords_help()
            elif topic == "symbols":
                display_symbols_help()
            elif topic == "escape":
                display_escape_characters_help()
            elif topic == "built":
                display_builtIn_functions_help()
            elif topic == "quit":
                break
            else:
                print("Unknown topic. Please try again.")
        continue
    elif text.strip().lower() == "exit":
        print("Exiting ChaiScript terminal.")
        break  # Exit the loop
    

    # Process ChaiScript commands directly from input
    result, error = ChaiScript.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
