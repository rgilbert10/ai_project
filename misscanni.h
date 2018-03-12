#include <vector>
using namespace std;
#ifndef MISSCANNI_H
#define MISSCANNI_H

class State {
    private:
        int boat = 0;
        int cannLeft = 0;
        int missLeft = 0;
        int cannRight = 0; 
        int missRight = 0;
    public:
        State(int b, int cL, int mL, int cR, int mR);
        bool isGoalState(State *state);
        bool isValidState(State *state);
        vector<State>* BFS();
        void print();
};


#endif