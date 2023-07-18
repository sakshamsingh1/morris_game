
Course project for AI course CS 6364 at University of Texas at Dallas

Aim: To implement **Nine Men’s Morris Game**

Problem description is available in the ```project_description``` folder.

Running the code :
```
$ python main.py --input_file <input_file> --output_file <output_file> --depth <depth>
 --visual <visual> --function <function>
```

where, 

"input_file" is the path to the input file 

"output_file" is the path to the output file 

"depth" is the depth of the search tree 

"visual" is the flag to enable visualization 

"function" can be one of the following:
  - MiniMaxOpening 
  - MiniMaxGame 
  - ABOpening 
  - ABGame 
  - MiniMaxOpeningBlack 
  - MiniMaxGameBlack 
  - MiniMaxOpeningImproved 
  - MiniMaxGameImproved

```game.py``` Script to play the game: