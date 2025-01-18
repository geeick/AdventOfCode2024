//
// Created by Georgia Eick on 09/01/25.
//

#ifndef ROBOT_H
#define ROBOT_H

class Grid;

class Robot {
  public:
        // Constructor
    Robot(Grid *m_grid, int r, int c);

        // Accessors
    int  row() const;
    int  col() const;

        // Mutators
    void move(int dir);
    void newPos(int row, int col);

  private:
    int   m_row;
    int   m_col;
    Grid *m_grid;
};



#endif //ROBOT_H
