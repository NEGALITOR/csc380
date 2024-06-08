#include <iostream>
#include <string>
using namespace std;

enum Player {
	Human = -1,
	Blank = 0,
	Computer = 1
};

/*
 *
 *    In your playGame method, you will set up a loop like this :
 *    while (true)
 *    {
 *    		Human makes move & check for winner
 *    		Machine makes best move & check for winner
 *    		Exit when winner found
 *    }
 *
 *    When human selects, remember to input-- to be in range on your array.
 *
 *    HINT when human moves:
 *                    Player human = Human;
 *                    board[input] = human;
 *    HINT when computer moves:
 *                    Player computer = Computer;
 *                    board[input] = computer;
 *

 *
 * */

void printBoard(Player board[]);
void playGame(Player board[]);
bool isWin(Player board[]);
bool isBlank(Player board[]);
int hEval(Player board[]);

int main() {
	char play = 'Y';

	while(play == 'Y') {
		Player board[9] = {Blank,Blank,Blank,Blank,Blank,Blank,Blank,Blank,Blank};
		printBoard(board);
		playGame(board);
		cout << "Do you want to play again? (Y/N) ";
		cin >> play;
		cout << endl;
	}
	return 0;
}

void printBoard(Player board[]) {
	
	for(int i = 0; i < 9; i++) {
		if((i == 2) || (i == 5) || (i == 8)) {
			if(board[i] == -1)
				cout << " X";
			else if (board[i] == 1)
				cout << " O";
			else
				cout << "  ";
		} else {
			if(board[i] == -1)
                                cout << "  X |";
                        else if (board[i] == 1)
                                cout << "  O |";
                        else
                                cout << "    |";
		}
		if(((i+1)%3 == 0) && (i != 8)) {
			cout << endl << "----|----|----" << endl;
		}
		if(i == 8)
			cout << endl;
	}

}

void playGame(Player board[])
{
	Player human = Human;
	Player walle = Computer;
	int chosenSlot;

	while (true)
	{
		cout << "Where do you want to play? ";
		cin >> chosenSlot;

		chosenSlot--;

		while (board[chosenSlot] != Blank || chosenSlot > 8 || chosenSlot < 0)
		{
			cout << "Invalid input, try again" << endl;
			cout << "Where do you want to play? ";

			cin >> chosenSlot;
			chosenSlot--;
		}

		board[chosenSlot] = human;
		printBoard(board);
		cout << endl;

		if (isWin(board))
		{
			cout << "You Won!...somehow? Don't do that..." << endl;
			break;
		}
		if (!isBlank(board))
		{
			cout << "Draw!" << endl;
			break;
		}
		
		chosenSlot = hEval(board);
		board[chosenSlot] = walle;

		printBoard(board);
		cout << endl;

		if (isWin(board))
		{
			cout << "You Lost! Boohoo. Now try again." << endl;
			break;
		}

	}
}

bool isWin(Player board[])
{
	int possibleCombos[8][3] = {
		{0, 1, 2},
		{0, 3, 6},
		{0, 4, 8},
		{1, 4, 7},
		{2, 4, 6},
		{2, 5, 8},
		{3, 4, 5},
		{6, 7, 8}
	};

	for (int i = 0; i < 8; i++)
	{
		if (board[possibleCombos[i][0]] != Blank && board[possibleCombos[i][0]] == board[possibleCombos[i][1]] && board[possibleCombos[i][1]] == board[possibleCombos[i][2]])
			return true;
	}
	return false;
}

bool isBlank(Player board[])
{
	for (int i = 0; i <= 8; i++)
	{
		if (board[i] == Blank)
			return true;
	}
	return false;
}

int hEval(Player board[])
{
	int possibleCombos[8][3] = {
		{0, 1, 2},
		{0, 3, 6},
		{0, 4, 8},
		{1, 4, 7},
		{2, 4, 6},
		{2, 5, 8},
		{3, 4, 5},
		{6, 7, 8}
	};

	// If you or your opponent has two in a row, play on the remaining square.
	for (int i = 0; i < 8; i++)
	{
		// Check B | X | X
		if ((board[possibleCombos[i][0]] == Blank && board[possibleCombos[i][1]] == Human && board[possibleCombos[i][2]] == Human) || 
			board[possibleCombos[i][0]] == Blank && board[possibleCombos[i][1]] == Computer && board[possibleCombos[i][2]] == Computer)
				return possibleCombos[i][0];

		// Check X | B | X
		if ((board[possibleCombos[i][0]] == Human && board[possibleCombos[i][1]] == Blank && board[possibleCombos[i][2]] == Human) ||
			board[possibleCombos[i][0]] == Computer && board[possibleCombos[i][1]] == Blank && board[possibleCombos[i][2]] == Computer)
				return possibleCombos[i][1];

		// Check X | X | B
		if ((board[possibleCombos[i][0]] == Human && board[possibleCombos[i][1]] == Human && board[possibleCombos[i][2]] == Blank) ||
			board[possibleCombos[i][0]] == Computer && board[possibleCombos[i][1]] == Computer && board[possibleCombos[i][2]] == Blank)
				return possibleCombos[i][2];
	}

	// If the center square is free, play there.
	if (board[4] == Blank) return 4;

	// If your opponent has played in a corner, play in the opposite corner.
	if (board[0] == Human && board[8] == Blank) return 8;
	if (board[8] == Human && board[0] == Blank) return 0;
	if (board[2] == Human && board[6] == Blank) return 6;
	if (board[6] == Human && board[2] == Blank) return 2;

	// If there’s an empty corner, play there.
	if(board[0] == Blank) return 0;
	if(board[2] == Blank) return 2;
	if(board[6] == Blank) return 6;
	if(board[8] == Blank) return 8;

	// After all else, play on an empty square.
	if(board[1] == Blank) return 1;
	if(board[3] == Blank) return 3;
	if(board[5] == Blank) return 5;
	if(board[7] == Blank) return 7;

	// Failed
	return -1;

}