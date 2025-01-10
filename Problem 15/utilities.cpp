#include "utilities.h"
#include <iostream>
#include <fstream>

using namespace std;

Input::Input(const vector<vector<char>>& g, const string& cmds)
    : grid(g), movements(cmds) {}

void Input::printGrid() const {
    for (const auto& row : grid) {
        for (const auto& ch : row) {
            cout << ch;
        }
        cout << endl;
    }
}

void Input::printMovements() const {
    cout << "Commands: " << movements << endl;
}

Input readFile(const string& file) {
    ifstream inputFile(file);

    if (!inputFile) {
        cerr << "Error opening file!" << endl;
        exit(1);
    }

    vector<vector<char>> grid;
    string line;

    while (getline(inputFile, line) && !line.empty() && line[0] == '#') {
        vector<char> row(line.begin(), line.end());
        grid.push_back(row);
    }

    string commands;
    getline(inputFile, commands);

    inputFile.close();

    return Input(grid, commands);
}
