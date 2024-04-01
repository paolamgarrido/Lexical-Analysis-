# Description

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
