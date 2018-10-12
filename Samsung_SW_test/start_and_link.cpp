// Problems from : https://www.acmicpc.net/problem/14889
// Samsung SW 역량 테스트

#include <iostream>
#include <algorithm>
#define ABS(n) (n>0)?n:-n

// get inputs
int N; // num of people
int** arr;
int* team_idx;

using namespace std;

int is_team(int a, int b){ 
	for (int i = 0; i < N; i++){
		if (team_idx[a] + team_idx[b] == 2){
			return 1;  // team start
		}
		else if (team_idx[a] + team_idx[b] == 0){
			return 2;  // team link
		}
	}
	return 0;
}

int calculate(){
	int team_A = 0;
	for (int i = 0; i < N; i++){  // search all the map
		for (int j = 0; j < N; j++){
			if (i != j){
				int is_team_result = is_team(i, j);
				if (is_team_result  == 1){
					team_A += arr[i][j];  // team start
				}
				else if (is_team_result == 2){
					team_A -= arr[i][j]; // team link
				}
			}
		}
	}
	return abs(team_A);
}

int start_and_link(){
	int score, mini = 1e8;
	do{
		score = calculate();
		mini = min(score, mini);
		if (score == 0)
			break;
	} while (next_permutation(team_idx, team_idx + N)); // permutation 

	return mini;
}


int main(void){
	int result = 0;

	scanf("%d", &N);
	arr = new int*[N];
	team_idx = new int[N];
	for (int i = 0; i < N; i++){
		team_idx[i] = (i < N / 2) ? 0 : 1;
		arr[i] = new int[N];
		for (int j = 0; j < N; j++){
			scanf("%d", &arr[i][j]);
		}
	}

	result = start_and_link();
	cout << result;

	return 0;
}