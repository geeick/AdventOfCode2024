//
// Created by Georgia Eick on 09/01/25.
//

#include "Box.h"
#include "Grid.h"

// Constructor
Box::Box(Grid *grid, const int r, const int c){
    m_grid = grid;
    m_row = r;
    m_col = c;
}

// Accessors
int  Box::row() const{
    return m_row;
}

int  Box::col() const{
    return m_col;
}

// Mutators
void Box::move(int dir){

}

void Box::newPos(int row, int col){

}
