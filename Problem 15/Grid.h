//
// Created by Georgia Eick on 09/01/25.
//

#ifndef GRID_H
#define GRID_H



class Grid {
  public:
        // Constructor/destructor
    Room(int nRows, int nCols);
    ~Room();

        // Accessors
    int     rows() const;
    int     cols() const;
    Player* player() const;
    int     beeCount() const;
    int     numBeesAt(int r, int c) const;
    bool    determineNewPosition(int& r, int& c, int dir) const;
    void    display() const;

        // Mutators
    bool addBee(int r, int c);
    bool addPlayer(int r, int c);
    bool swatBeeAt(int r, int c, int dir);
    bool moveBees();

  private:
    int     m_rows;
    int     m_cols;
    Player* m_player;
    Bee*    m_bees[MAXBEES];
    int     m_nBees;
};



#endif //GRID_H
