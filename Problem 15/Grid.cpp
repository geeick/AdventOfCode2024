//
// Created by Georgia Eick on 09/01/25.
//

#include "Grid.h"

#include <iostream>

#include "Robot.h"
#include "Box.h"


Grid::Grid(std::vector<std::vector<char>> &map){
   m_map = &map;
   m_nBoxes = 0;
   m_rows = map.size();
   m_cols = map[0].size();
}

Grid::~Grid(){

}
// Accessors
int Grid::rows() const{
   return m_rows;
}

int Grid::cols() const{
  return m_cols;
}

std::vector<std::vector<char>> Grid::map() {
  return *m_map;
}

Robot* Grid::robot() const{
  return m_robot;
}

int Grid::boxCount() const{
  return m_nBoxes;
}

int Grid::numBoxesAt(int r, int c) const{
  if (m_map[r][c] == '#')
    return 1;
  else
    return 0;
}

void Grid::display() const{
	for (const auto &row : grid) {
        // Iterate over elements in each row
        for (const auto &element : row) {
            std:: cout << &element << " ";
        }
    }
}

// Mutators
bool Grid::addBox(int r, int c){
   m_box[m_nBoxes] = new Box(this, r, c);
   m_nBoxes++;
   return true;
}

bool Grid::addRobot(int r, int c){
  m_robot = new Robot(this, r, c);
  return true;
}

bool Grid::moveRobot(const int dir) const {
    m_robot->move(dir);
    return true;
}

bool Grid::moveBox(int dir, int r, int c) const {
  int k = 0;
  for ( ; k < m_nBoxes; k++)
  {
    if (m_box[k]->row() == r  &&  m_box[k]->col() == c){
      break;
    }
  }
  m_box[k]->move(dir);
  return true;
}

void Grid::runCommand(char cmd) const{
    int dir;
  	if (cmd == '^'){
          dir = 1;
  	}
    else if (cmd == '>'){
          dir = 2;
    }
    else if (cmd == 'v'){
      dir = 3;
    }
    else{
      dir = 4;
    }

    switch (dir) {
        default: break;
        case 1:
          moveRobot(1);
          break;
        case 2:
          moveRobot(2);
          break;
        case 3:
          moveRobot(3);
          break;
        case 4:
          moveRobot(4);
          break;
    }
}