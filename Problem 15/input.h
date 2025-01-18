#ifndef UTILITIES_H
#define UTILITIES_H

#include <string>
#include <vector>

class Input {
  	public:
    Input(const std::vector<std::vector<char>>& g, const std::string& cmds);

    void printGrid() const;
    void printMovements() const;
    std::vector<std::vector<char>> getGrid();
    std:: string getCommands();

    private:
    std::vector<std::vector<char>> grid;
    std::string movements;
};

Input readFile(const std::string& path);

#endif // UTILITIES_H


