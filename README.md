# E1 Implementation of Lexical Analysis

## Description
When it comes to computational methods, the ability to comprehend and analyze languages is fundamental. In this evidence, we will delve into the development of a lexical analysis parser designed to accurately detect a specific language. The language in focus encompasses all possible combinations of the digits 0, 1, and 2, but it must adhere to a set of constraints, prohibiting certain sequences: '111', '222', '210', '221100', '110', and '000'. Therefore, recognizing patterns within languages and ensuring both efficient parsing and processing are crucial aspects of this understanding.

To tackle the problem effectively, we chose to employ the concept of Deterministic Finite Automata (DFA), a mathematical model used to recognize languages. A DFA comprises five objects:

1. **Q**: a finite set of states.
2. **Σ**: a finite set of input symbols, known as the alphabet.
3. **δ**: the transition function, which, given a state and an input symbol returns the next state. Formally, δ: Q × Σ → Q.
4. **q0**: the start state (an element of Q).
5. **F**: a set of accepting states (a subset of Q).

In other words, the model starts in a designated state and reads symbols from an input string, transitioning between states according to the transition function until it completely reads the input string. Then, the DFA accepts or rejects the string based on whether it ends in an accepting state. It's important to note that there must be exactly one transition exiting every state for each possible input symbol (Sipser, 2013). Essentially, constructing the DFA aims to capture the essence of the language while ensuring compliance with the specified constraints.

Moreover, we will utilize Regular Expressions, a powerful notation method that uses regular operations to build expressions describing patterns within strings to represent a language. This formulation consists of a set of symbols representing characters in the language and operators denoting operations on these symbols. Regular expressions can also describe languages recognized by DFAs, as any regular expression can be converted into a finite automaton and vice versa to recognize the language it describes (Sipser, 2013).

Once our models are complete, we will implement the DFA using Prolog, while also testing the Regular Expression with Python. This allows us to evaluate and compare various approaches, considering elements such as time and pattern complexity, until an optimal solution is chosen.

Ultimately, the implementation process will include a set of documented tests to demonstrate that the algorithm works as intended and correctly solves the problem. By combining theoretical concepts with practical application, this evidence serves as proof of the power of computational methods in language analysis.

## Models
In this section, we will discuss the two primary models utilized in our language analysis: Deterministic Finite Automata (DFA) and Regular Expression. Both models form the foundation of our approach, offering unique advantages in representing and parsing language patterns.

### Regular Expression 
Initially, the regular expression was identified taking into account the language constraints and possible combinations: 

(?!.*111|.*222|.*210|.*221100|.*110|.*000)[012]+

Let's break it down to understand how it represents our language pattern:

(**?!**.*111|.*222|.*210|.*221100|.*110|.*000)

The `?!` in a regular expression represents a negative lookahead assertion, ensuring that the string doesn’t contain a certain pattern immediately ahead. (GeeksforGeeks, 2021)

(?!.*111|.*222|.*210|.*221100|.*110|.*000)

Meanwhile, the `.*` inside each lookahead assertion separated by a `|`, indicates in this case that any sequence of characters before the specified prohibited sequences is allowed. 

 [012]+

The last part of the regular expression permits any combination of the characters '012', as indicated by the square brackets denoting a character set. The `+` ensures that there is at least one occurrence of any character within the set.

Therefore, the regular expression ensures that the language allows all possible combinations of '012' with the exception of the prohibited sequences '111', '222', '210', '221100', '110', or '000'. If any of these previous sequences are found, the assertion fails, and the regular expression match will not proceed.

Note: In addition, in order to test the correctness of the regular expression, first the built-in model for Regular Expressions in python was imported as you can see in the file regex_python.py. Then the file combinations.pdf, that contains all possible base case combinations of '012' was tested as well as the test cases from the implementation section. All tests turned out to be successful. To run the program in the terminal follow the instructions below: 

**Run file:**

python regex_python.py

**Enter input:**

Enter a string composed of 0s, 1s, and 2s: 012

The output will resemble the following:

The input string '012' conforms to the language's syntax.

**To exit the program write ‘exit’:**

Enter a string composed of 0s, 1s, and 2s: exit

### DFA 
After the regular expression was defined without any limitations, we explored its equivalent DFA. In order to build it, first of all the five objects that compose a deterministic model were identified. Then to begin constructing the diagram, the build up started from the smallest subexpressions as recommended by Michael Sipser, in this case taking as references the constraints: 
![image](https://github.com/paolamgarrido/Lexical-Analysis-/assets/111533069/090fb5c1-9239-4b46-a44b-f392d807d56d)

Then, we moved to larger subexpressions that explored the possible combinations in order to demonstrate the original expression. This resulted in our final automaton, shown in the diagram below:
![image](https://github.com/paolamgarrido/Lexical-Analysis-/assets/111533069/65f8377e-4ac4-408b-87ee-d486da071970)

## Implementation
For the lexical analysis parser implementation, the first choice was using prolog to code the automata as seen in the automata.pl file. To run the program in the terminal follow the instructions below: 

**Initiate Prolog:**

swipl

**Load file:**

["automata"].
true.

**Execute Function :**

parse_list([your input list]).

This function call initiates the parsing process for the input list, for example `[0,1,2]`. The program then evaluates the input based on the rules defined in the automata and outputs whether the input string is accepted or rejected based on the language constraints.

The output will resemble the following:

[0,1,2]: Accepted
true .

### Second Implementation
After successfully implementing the DFA in Prolog, I became curious about exploring the Regular Expression approach. Although the DFA provides an efficient way to recognize the language patterns, I wanted to compare it with the regex implementation to evaluate its effectiveness. 

The regex implementation can be found in the regex.py file. To run the program in the terminal follow the instructions below: 

**Run file:**

python regex.py

**Enter input:**

Enter a string composed of 0s, 1s, and 2s: 012

The output will resemble the following:

The input string '012' conforms to the language's syntax.

**To exit the program write ‘exit’:**

Enter a string composed of 0s, 1s, and 2s: exit

## Tests

### DFA
The file test_automata.pl contains all the cases tested for the DFA. To run the program in the terminal follow the instructions below: 

**Initiate Prolog:**
swipl

**Load file:**
["test_automata"].
true.

**Execute Function :**

run_tests.

The output will resemble the following:

[1,1,1]: Rejected
[2,2,0]: Accepted

### Regular Expression
The file test_regex.py contains all the cases tested for the Regular Expression. To run the program in the terminal follow the instructions below: 

**Run file:**
python test_regex.py

The output will resemble the following indicating all tests are successful:


...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK


## Analysis



## References
Sipser, M. (2013). Introduction to the Theory of Computation. En SIGACT news (Vol. 3, pp. 35-37, 64-66). Cengage Learning. http://debracollege.dspaces.org/bitstream/123456789/671/1/Introduction%20to%20the%20Theory%20of%20Computation_2013%20Sipser.pdf

GeeksforGeeks. (2021). Python Regex Lookahead. https://www.geeksforgeeks.org/python-regex-lookahead/
