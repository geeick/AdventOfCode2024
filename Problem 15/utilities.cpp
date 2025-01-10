#include "globals.h"

#ifndef UTILITIES_H
#define UTILITIES_H

struct Input {
    vector<vector<char>> grid;  // 2D grid
    string movements;           // Command string

    Input (const vector<vector<char>>& g, const string& cmds)
        : grid(g), movements(cmds) {}

    void printGrid() {
        for (const auto& row : grid) {
            for (const auto& ch : row) {
                cout << ch;  // Print each character of the row
            }
            cout << endl;  // Print a newline after each row
        }
    }

    void printMovements() {
        cout << "Commands: " << movements << endl;
    }
};

Input readFile(const string& file)
{
    ifstream inputFile(file);

    if (!inputFile) {
        cerr << "Error opening file!" << endl;
        exit (1) ;
    }

    vector<vector<char>> grid;
    string line;

    while (getline(inputFile, line) && line[0] == '#') {
        vector<char> row(line.begin(), line.end());
        grid.push_back(row);
    }

    string commands;
    getline(inputFile, commands);

    inputFile.close();

    return Input(grid, commands);
}

#endif //UTILITIES_H
