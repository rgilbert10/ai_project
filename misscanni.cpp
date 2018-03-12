
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
vector<State>* State::Successor(State* state) {
  if(boat == 0) {
    //Two Missionaries Cross
    State* new_state = new State(state->boat+1, state->cannLeft, state->missLeft-2, state->cannRight, state->missRight+2);
    if(isValidState(new_state)) {
      new_state->parent = state;
      state->addChild(new_state);
    }
    delete new_state;
    //Two Cannibals Cross
    new_state = new State(state->boat+1, state->cannLeft-2, state->missLeft, state->cannRight+2, state->missRight);
    if(isValidState(new_state)) {
      new_state->parent = state;
      state->addChild(new_state);
    }
    delete new_state;
    //Missionary and Cannibal Cross
    new_state = new State(state->boat+1, state->cannLeft-1, state->missLeft-1, state->cannRight+1, state->missRight+1);
    if(isValidState(new_state)) {
      new_state->parent = state;
      state->addChild(new_state);
    }
    delete new_state;
    //Single Missionary Crosses
    new_state = new State(state->boat+1, state->cannLeft, state->missLeft-1, state->cannRight, state->missRight+1);
    if(isValidState(new_state)) {
      new_state->parent = state;
      state->addChild(new_state);
    }
    delete new_state;
    //Single Cannibal Crosses
    new_state = new State(state->boat+1, state->cannLeft-1, state->missLeft, state->cannRight+1, state->missRight);
    if(isValidState(new_state)) {
      new_state->parent = state;
      state->addChild(new_state);
    }
    delete new_state;
  } else {
    //Two Missionaries return
    State* new_state = new State(state->boat-1, state->cannLeft, state->missLeft+2, state->cannRight, state->missRight-2);
    if(isValidState(new_state)) {
      new_state->parent = state;
      state->addChild(new_state);
    }
    delete new_state;
    //Two Cannibals Return
    new_state = new State(state->boat-1, state->cannLeft+2, state->missLeft, state->cannRight-2, state->missRight);
    if(isValidState(new_state)) {
      new_state->parent = state;
      state->addChild(new_state);
    }
    delete new_state;
    //Missionary and Cannibal Return
    new_state = new State(state->boat-1, state->cannLeft-1, state->missLeft+1, state->cannRight-1, state->missRight+1);
    if(isValidState(new_state)) {
      new_state->parent = state;
      state->addChild(new_state);
    }
    delete new_state;
    //Single Missionary Returns
    new_state = new State(state->boat-1, state->cannLeft, state->missLeft+1, state->cannRight, state->missRight-1);
    if(isValidState(new_state)) {
      new_state->parent = state;
      state->addChild(new_state);
    }
    delete new_state;
    //Single Cannibal Returns
    new_state = new State(state->boat-1, state->cannLeft+1, state->missLeft, state->cannRight-1, state->missRight);
    if(isValidState(new_state)) {
      new_state->parent = state;
      state->addChild(new_state);
    }
    delete new_state;
  }
}
void State::addChild(State* state) {
  children.push_back(state);
}

int main() {
    State *initialShit = new State(0, 3, 3, 0, 0);
    initialShit->Successor(initialShit);
    vector<State> *answer = initialShit->BFS();

    //State initialShit(0, 3, 3, 0, 0);

    return 0;
}
