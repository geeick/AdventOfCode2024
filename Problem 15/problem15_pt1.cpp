#include "globals.h"
#include <vector>

int translateCommand(char command);
bool moveObject(char dir, int row, int col);

Input instructions = readFile(file_path_example);

std::string commands = instructions.getCommands(); //commands is a string with the commands
std::vector<std::vector<char>> map = instructions.getGrid(); //grid is a grid object that takes in a 2d vector


int main() {
    int total = 0;

    for (int cmd = 0; cmd < commands.size(); cmd++) {

        bool objectMoved = false;
        char command = commands[cmd];

        for (int i = 0; i < map.size(); i++) {
            if (objectMoved) break;
            for (int j = 0; j < map[0].size(); j++) {
                if (map[i][j] == '@') {
                    objectMoved = true;
                    moveObject(command, i, j);
                    break;
                }
            }
        }

    }
    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[0].size(); j++) {
            if (map[i][j]== 'O') {
                total += ((100*i)+j);
            }
        }
    }
    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[0].size(); j++) {
            std::cout<<map[i][j];
        }
        std::cout<<std::endl;

    }

    std::cout << total << std::endl;

    return 0;
}

bool moveObject(char dir, int row, int col) {
    int command = translateCommand(dir);
    char temp =  map[row][col];

    switch (command) {
        default: break;
        case 1:
            if (map[row -1][col] == '#') {
                return false;
            }

            if (map[row -1][col] == 'O') {
                moveObject(dir, row - 1, col);
            }

            if (map[row -1][col] == '.') {
                map[row-1][col] = temp;
                map[row][col] = '.';
                return true;
            }

            return true;

        case 2:
            if (map[row][col +1] == '#') {
                return false;
            }

            if (map[row][col +1] == 'O') {
                moveObject(dir, row, col + 1);
            }

            if (map[row][col+1] == '.') {
                map[row][col + 1] = temp;
                map[row][col] = '.';
            }

            return true;

        case 3:
            if (map[row +1][col] == '#') {
                    return false;
                }

            if (map[row +1][col] == 'O') {
                moveObject(dir, row + 1, col);
            }

            if (map[row +1][col] == '.') {
                map[row+1][col] = temp;
                map[row][col] = '.';
            }

            return true;

        case 4:
            if (map[row][col -1] == '#') {
                return false;
            }

            if (map[row][col -1] == 'O') {
                moveObject(dir, row, col - 1);
            }

            if (map[row][col -1] == '.') {
                map[row][col - 1] = temp;
                map[row][col] = '.';
            }

        return true;
    }

    return true;
}

int translateCommand(char command) {
    if (command == '^')
        return 1;
    if (command == '>')
        return 2;
    if (command == 'v')
        return 3;
    if (command == '<')
        return 4;

    return 0;
}

