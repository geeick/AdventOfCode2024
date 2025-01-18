//
// Created by Georgia Eick on 09/01/25.
//

#ifndef BOX_H
#define BOX_H
#include "Grid.h"

class Grid;

class Box   {

public:

    // Constructor
    Box(Grid *grid, int r, int c);

    // Accessors
    int  row() const;
    int  col() const;

    // Mutators
    void move(int dir);
    void newPos(int row, int col);

private:
    int m_row;
    int m_col;
    Grid *m_grid;
};



#endif //BOX_H
