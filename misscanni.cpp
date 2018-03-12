
#include <iostream>
#include <vector>
#include "misscanni.h"
using namespace std;


State::State(int b, int cL, int mL, int cR, int mR) {
    //boat - 0 on left side, boat - 1 on right side
    boat = b;
    cannLeft = cL;
    missLeft = mL;
    cannRight = cR;
    missRight = mR;
}

bool State::isGoalState(State *state) {
    if(state->cannLeft == 0 && state->missLeft == 0)
        return true;
    else
        return false;
}

bool State::isValidState(State *state) {
    if(state->missLeft >= 0 and state->missRight >= 0 && state->cannLeft >= 0 && state->cannRight >= 0
        && (state->missLeft == 0 || state->missLeft >= state->cannLeft) && (state->missRight == 0 || 
        state->missRight >= state->cannRight))
        return true;
    else
        return false;
}

vector<State>* State::BFS() {
    
}

void State::print() {
    
}

int main() {
    State *initialShit = new State(0, 3, 3, 0, 0);
    vector<State> *answer = initialShit->BFS();
    
    //State initialShit(0, 3, 3, 0, 0);
    
    return 0;
}