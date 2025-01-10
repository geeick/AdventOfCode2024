#ifndef GLOBALS_H
#define GLOBALS_H

#include <iostream>
#include <fstream>
#include <_stdio.h>

using namespace std;

const string file_path = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem15.txt";
const string file_path_example = "/Users/georgiaeick/Library/Mobile Documents/com~apple~TextEdit/Documents/AdventOfCode_Problem15Ex.txt";

struct Input;
Input readFile(const string& file);

#endif //GLOBALS_H
