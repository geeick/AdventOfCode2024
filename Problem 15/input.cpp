#include "input.h"
#include <iostream>
#include <fstream>

using namespace std;

Input::Input(const std::vector<std::vector<char>>& g, const std::string& cmds)
    : grid(g), movements(cmds) {}

void Input::printGrid() const {
    for (const auto& row : grid) {
        for (const auto& ch : row) {
            cout << ch;
        }
        cout << endl;
    }
}

std:: string Input::getCommands(){
    return movements;
}

std::vector<std::vector<char>> Input::getGrid() {
    std::vector<std::vector<char>> newGrid;

    // Assuming `grid` is the original grid you're working with
    for (const auto& row : grid) {
        std::vector<char> newRow;  // Create a new row for the new grid
        for (const auto& ch : row) {
            newRow.push_back(ch);  // Add each character to the new row
        }
        newGrid.push_back(newRow);  // Add the row to the new grid
    }

    return newGrid;  // Return the new 2D vector
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
