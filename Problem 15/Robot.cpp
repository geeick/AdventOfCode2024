//
// Created by Georgia Eick on 09/01/25.
//

#include "Robot.h"
#include "Grid.h"

Robot::Robot(Grid *m_grid, int r, int c){

}
// Accessors
int  Robot::row() const{
  return m_row;
}

int  Robot::col() const{
  return m_col;
}
// Mutators
void Robot::move(int dir){
  switch (dir) {
    case 1:
      if (row() > 0)
        m_row = m_row - 1;
      if (m_grid->grid[(row() -1)][(col())] == '#') {
        m_grid->moveBox(dir, (row() -1), col());
      }
      break;

    case 2:
      if (col() > 0)
        m_row = m_col + 1;
        if (m_grid->grid[(row())][(col()+1)] == '#') {
          m_grid->moveBox(dir, (row()), col()+1);
        }
      break;

    case 3:
       m_row = m_row + 1;
       if (m_grid->grid[(row() +1)][(col())] == '#') {
         m_grid->moveBox(dir, (row() +1), col());
       }
      break;

    case 4:
       m_row = m_col - 1;
       if (m_grid->grid[(row())][(col()-1)] == '#') {
         m_grid->moveBox(dir, (row()), col()-1);
       }
      break;

    default: break;
  }
}
void Robot::newPos(int row, int col){
  m_row = row;
  m_col = col;
}