#include "globals.h"

int main() {
    Input instructions = readFile(file_path_example);

    instructions.printGrid();
    instructions.printMovements();

    return 0;
}

