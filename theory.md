##Practical 1: A* Algorithm for 8-Puzzle Problem##
Objective
1. To understand informed search techniques.
2. To implement A* algorithm for solving the 8-puzzle problem.
3. To find an optimal path from the initial state to the goal state.
Theory

A* is an informed search algorithm used to find the optimal path from the initial state to the goal state. It uses two values: actual cost (g) and heuristic cost (h).

Evaluation function:
\[
f(n)=g(n)+h(n)
\]

In the 8-puzzle, we use a 3 × 3 board containing 8 numbered tiles and one blank space (0). The heuristic counts the number of misplaced tiles.

Algorithm
1. Start.
2. Define initial state and goal state.
3. Calculate heuristic using misplaced tiles.
4. Set initial g = 0.
5. Calculate f = g + h.
6. Insert initial state into priority queue.
7. Select the state with minimum f-value.
8. Check whether it is the goal state.
9. Generate valid moves by moving the blank tile.
10. Calculate new g, h and f values.
11. Repeat until the goal state is reached.
12. Display the solution path and stop.
Conclusion

The 8-puzzle problem was successfully solved using the A* algorithm. It uses actual cost and heuristic cost to find an optimal solution path.






##Practical 2: Tower of Hanoi Using State Space Search
Objective
1. To understand state-space search in AI.
2. To represent Tower of Hanoi using states and operators.
3. To generate legal moves and find the solution path.
Theory

State-space search is a problem-solving technique in which all possible configurations are represented as states. Operators are applied to generate new states until the goal state is reached.

In Tower of Hanoi, there are three pegs and disks of different sizes. The objective is to move all disks from the source peg to the destination peg by following legal movement rules.

The minimum number of moves required is:
\[
2^n-1
\]

Algorithm
1. Start.
2. Read the number of disks.
3. Define the initial and goal states.
4. Insert the initial state into a queue.
5. Remove the next state from the queue.
6. Check whether it is the goal state.
7. Generate all possible legal moves.
8. Create new successor states.
9. Check visited states to avoid repetition.
10. Store parent information for each new state.
11. Repeat until the goal state is reached.
12. Display the solution path and total moves.
13. Stop.
Conclusion

The Tower of Hanoi problem was successfully solved using state-space search. Legal moves, visited-state checking and BFS were used to find the shortest solution path.






##Practical: Implement BFS for Solving the 8-Puzzle Problem
Objective
1. To understand uninformed (blind) search techniques.
2. To understand Breadth First Search (BFS).
3. To implement BFS to solve the 8-puzzle problem and find the solution path.
Theory
Breadth First Search (BFS) is an uninformed search algorithm that explores states level by level. It uses a Queue (FIFO – First In, First Out) to store states waiting to be explored.

In the 8-puzzle problem, a 3 × 3 board contains 8 numbered tiles and one blank space (0). The blank tile can move up, down, left or right. Each valid movement generates a new state.

BFS uses a visited set to avoid repeated states and parent pointers to reconstruct the solution path. It finds the shortest solution when every move has equal cost.
Algorithm
1. Start.
2. Define the initial state and goal state.
3. Create an empty queue and visited set.
4. Insert the initial state into the queue.
5. Remove the front state from the queue.
6. Check whether it is the goal state.
7. Generate all valid successor states.
8. Check whether the states are already visited.
9. Insert new states into the queue and store their parent.
10. Repeat until the goal is reached or the queue becomes empty.
11. Display the solution path.
12. Stop.
Conclusion
The 8-puzzle problem was successfully implemented using Breadth First Search. BFS explores states level by level using a queue and finds the shortest solution path when all moves have equal cost.









Aim
To implement Depth First Search (DFS) algorithm to solve the Water Jug Problem using state-space search.
Objectives
1. To understand the concept of uninformed (blind) search techniques.
2. To understand Depth First Search (DFS) for solving problems.
3. To implement DFS using a stack.
4. To generate successor states using valid water jug operations.
5. To find the solution path from the initial state to the goal state.
Theory
Depth First Search (DFS):

DFS is an uninformed search technique that explores one branch as deeply as possible before backtracking and exploring another branch.

DFS uses a Stack (LIFO – Last In, First Out) or recursion to explore states. A visited set is used to avoid repeatedly exploring the same states.

Water Jug Problem:

Consider two water jugs:
- Jug A has a capacity of 4 litres.
- Jug B has a capacity of 3 litres.
- Initially, both jugs are empty.
- The objective is to obtain exactly 2 litres of water in either jug.
State Representation: (x, y)

Where:
- x = Amount of water in the 4-litre jug.
- y = Amount of water in the 3-litre jug.
Initial State: (0, 0)

Goal State: (2, 0) or (0, 2)

Possible Operations:
1. Fill the 4-litre jug.
2. Fill the 3-litre jug.
3. Empty the 4-litre jug.
4. Empty the 3-litre jug.
5. Pour water from the 4-litre jug into the 3-litre jug.
6. Pour water from the 3-litre jug into the 4-litre jug.
DFS explores possible states until the goal is reached. If a branch cannot reach the goal, it backtracks and explores another branch.
Algorithm
1. Start.
2. Define the initial state (0, 0) and goal state (2, 0) or (0, 2).
3. Create an empty stack, visited set and parent dictionary.
4. Push the initial state onto the stack and mark it as visited.
5. Pop the top state from the stack.
6. Check whether the current state satisfies the goal condition.
7. If the goal is reached, reconstruct and display the solution path.
8. Otherwise, generate all possible successor states using valid water jug operations.
9. Check whether each successor state is already visited.
10. If it is not visited, add it to the visited set, store its parent and push it onto the stack.
11. Continue until the goal is reached or the stack becomes empty.
12. If the stack becomes empty without finding the goal, display "No solution found".
13. Stop.
Conclusion
DFS was successfully studied and implemented for solving the Water Jug Problem using state-space search. The algorithm explores one branch deeply before backtracking to other branches. It uses a stack, visited set and parent dictionary to find and display the solution path.








Practical: Implement Backtracking Search to Solve the 8-Queens Constraint Satisfaction Problem
Aim
To implement the Backtracking Search algorithm to solve the 8-Queens problem by placing eight queens on an 8 × 8 chessboard such that no two queens attack each other.
Objectives
1. To understand the concept of Constraint Satisfaction Problems (CSPs).
2. To understand the Backtracking Search technique.
3. To represent the 8-Queens problem using variables, domains and constraints.
4. To implement backtracking to place eight queens safely on a chessboard.
5. To obtain a valid solution without violating any constraints.
Theory
1. Constraint Satisfaction Problem (CSP):

A Constraint Satisfaction Problem is a problem in which values are assigned to variables from their respective domains while satisfying a set of constraints.

A CSP consists of three components:
- Variables: The elements whose values need to be assigned.
- Domains: The possible values that can be assigned to variables.
- Constraints: The rules that must be satisfied.
2. 8-Queens Problem:

The 8-Queens problem requires placing eight queens on an 8 × 8 chessboard such that no two queens attack each other.

A queen can attack another queen if they are in the same row, same column or same diagonal.

CSP Representation:
- Variables: Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8.
- Domain: 8.
- Initial State: Empty chessboard.
- Goal State: Eight queens placed without attacking each other.
Constraints:
1. No two queens should be in the same column.
2. No two queens should be on the same diagonal.
3. Only one queen is placed in each row.
3. Backtracking Search:

Backtracking is a search technique that builds a solution step by step. If a selected position violates any constraint, the algorithm rejects that position and tries another option.

In the 8-Queens problem, queens are placed row by row. If no safe position is available in a row, the algorithm goes back to the previous row, removes the queen and tries another column.

The diagonal constraint is:
\[
|Column_1-Column_2| \neq |Row_1-Row_2|
\]

Algorithm
1. Start.
2. Initialize an empty board of size 8 × 8.
3. Create an array to store queen positions and initialize it with -1.
4. Start placing queens from row 0.
5. Try each column from 0 to 7 in the current row.
6. Check whether the selected position is safe.
7. If the position is safe, place the queen in that position.
8. Call the recursive function to place a queen in the next row.
9. If all eight queens are placed successfully, return true.
10. If no safe position is available, remove the previously placed queen and try another column.
11. Continue the process until a valid solution is found or all possibilities are exhausted.
12. Display the chessboard and queen positions.
13. Stop.
Conclusion
The 8-Queens problem was successfully implemented using the Backtracking Search technique. The problem was formulated as a Constraint Satisfaction Problem using variables, domains and constraints. Queens were placed row by row while checking column and diagonal constraints. Whenever an invalid arrangement occurred, the algorithm backtracked and tried another position. Thus, a valid arrangement of eight non-attacking queens was obtained.








Practical: Simple Chatbot Using Predefined Rules and Pattern Matching
1. Aim
To develop a simple chatbot that interacts with users using predefined rules and pattern matching.
2. Objectives
1. To understand the basic concept of chatbots in Artificial Intelligence.
2. To understand rule-based conversation systems.
3. To implement pattern matching using predefined keywords.
4. To generate appropriate responses based on user input.
3. Theory
A chatbot is a computer program that interacts with users through text or voice.

A rule-based chatbot works using predefined rules and conditions. It does not learn automatically from data. It checks the user's input and provides a response according to the matching rule.

Pattern Matching: It is a technique used to identify specific keywords or phrases in user input.

Working:
1. The chatbot accepts input from the user.
2. It converts the input into lowercase.
3. It checks for predefined keywords.
4. If a keyword matches, it displays the corresponding response.
5. If no keyword matches, it displays a default response.
6. The chatbot continues until the user enters bye, exit, or quit.
Advantages:
- Easy to develop and understand.
- Does not require training data.
- Gives quick and predictable responses.
Limitations:
- Understands only predefined keywords.
- Cannot understand complex sentences.
- Cannot learn from previous conversations.
4. Algorithm
1. Start the program.
2. Define predefined keywords and their responses.
3. Display a welcome message.
4. Accept input from the user.
5. Convert the input into lowercase.
6. Check whether the input contains bye, exit, or quit.
7. If yes, display a goodbye message and terminate the program.
8. Otherwise, compare the input with predefined patterns.
9. If a pattern matches, display its corresponding response.
10. If no pattern matches, display the default response.
11. Repeat the process until the user exits.
12. Stop.
5. Conclusion
We successfully developed a simple rule-based chatbot using predefined rules and pattern matching. The chatbot identifies keywords from user input and generates appropriate responses. Thus, we understood the basic working of rule-based conversational systems in Artificial Intelligence.






Practical No. 1: Simple Reflex Agent for Vacuum Cleaner World
1. Aim
To design and implement a Simple Reflex Agent for the Vacuum Cleaner World and analyze its rational behavior based on the current percept of the environment.
2. Objectives
1. To understand the concept of an intelligent agent.
2. To understand the working of a Simple Reflex Agent.
3. To implement a Vacuum Cleaner Agent using Python.
4. To analyze the agent's actions for different environmental conditions.
5. To understand rational behavior in an AI agent.
3. Theory
Intelligent Agent:

An intelligent agent is a system that perceives its environment through sensors and performs actions through actuators to achieve a specific goal.

Basic Structure:

Environment → Sensors → Agent → Actuators → Environment

Vacuum Cleaner World:

The Vacuum Cleaner World consists of two locations, A and B. Each location can be either Clean or Dirty.

The vacuum cleaner performs three actions:
- Suck: Cleans the current location.
- Move Right: Moves from A to B.
- Move Left: Moves from B to A.
Simple Reflex Agent:

A Simple Reflex Agent selects an action based only on the current percept. It uses predefined condition-action rules.

Examples:
- IF the current location is Dirty → Suck.
- IF the current location is Clean and the agent is at A → Move Right.
- IF the current location is Clean and the agent is at B → Move Left.
It does not remember previous states or actions.

PEAS Description:

PEAS stands for Performance Measure, Environment, Actuators and Sensors.
Component	Description
Performance Measure	Maximum cleanliness, minimum time and energy
Environment	Two rooms A and B
Actuators	Suck, Move Left, Move Right
Sensors	Current location and cleanliness status

Rational Behavior:

Rational behavior means selecting the best possible action based on the current percept to achieve the desired goal, such as cleaning dirty rooms while minimizing unnecessary movements.
4. Algorithm
1. Start the program.
2. Define the environment with two locations A and B.
3. Set the initial position of the vacuum cleaner.
4. Read the current location and its cleanliness status.
5. If the current location is dirty, perform the Suck action.
6. If the current location is clean:
   - If the agent is at A, move right to B.
   - If the agent is at B, move left to A.
7. Update the environment after every action.
8. Repeat the process for a specified number of steps.
9. Display the actions performed and the final environment.
10. Stop the program.
5. Conclusion
We successfully designed and implemented a Simple Reflex Agent for the Vacuum Cleaner World using Python. The agent selects actions based on the current location and cleanliness status. It successfully cleans both rooms using predefined condition-action rules. Thus, we understood intelligent agents, PEAS representation and rational behavior in Artificial Intelligence.