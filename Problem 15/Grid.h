

#ifndef GRID_H
#define GRID_H

#include <vector>

class Box;
class Robot;

class Grid {
  public:
        // Constructor/destructor
    explicit Grid(std::vector<std::vector<char>> &map);
    ~Grid();

        // Accessors
    int     rows() const;
    int     cols() const;
    std::vector<std::vector<char>> map();
    Robot* robot() const;
    int     boxCount() const;
    int     numBoxesAt(int r, int c) const;
    void    display() const;

        // Mutators
    bool addBox(int r, int c);
    bool addRobot(int r, int c);
    bool moveRobot(int dir) const;
    bool moveBox(int dir, int r, int c) const;
    void runCommand(char dir) const;

  private:
    int     m_rows;
    int     m_cols;
    Robot* m_robot;
    std::vector<Box*> m_box;
    int     m_nBoxes;
    std::vector<std::vector<char>> *m_map;
};

#endif //GRID_H
