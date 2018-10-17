#include <stdio.h>
#include <algorithm>

using namespace std;

int N, L;
int** map;

void get_input(){
	scanf("%d %d", &N, &L);
	map = new int*[N];
	for (int i = 0; i < N; i++)
		map[i] = new int[N];

	for (int i = 0; i < N; i++){
		map[i] = new int[N];
		for (int j = 0; j < N; j++){
			scanf("%d", &map[i][j]);
		}
	}
}

bool is_available(int* RoI){
	int toLook = L;
	int diff;
	int* back = new int[L];
	int prev = RoI[0];
	for (int i = 1; i < N; i++){
		diff = prev - RoI[i];
		prev = RoI[i];
		if (diff == 1){  // if lower land,
			if (toLook == 0){ // done?
				toLook = L; // new slope available
			}
			if (toLook == L){ // set slope
				toLook--;
				back[i%L] = 1;
				if (L == 1){ // if L==1 exception handling
					toLook++;
				}
			}
			else // if a slope is on setting
				return false; // unavailable
		}
		else if (diff == 0){   // if no height diff
			if (toLook != L){ // if on setting
				toLook--; // continue it
				back[i%L] = 1;
			}
			if (toLook <= 0){ // done?
				toLook = L; // new slope available
				back[i%L] = 1;
			}
			else if (toLook == L){
				back[i%L] = 0;
			}
		}
		else if (diff == -1){ // if higher land
			if (i >= L){
				for (int j = 1; j <= L; j++){ // check the footprint(back)
					if (back[(i - j) % L] == 1)
						return false;
					else
						back[(i - j) % L] = 1;
				}
				back[i%L] = 0;
			}
			else
				return false;
		}
		else{
			return false;
		}
	}
	if (toLook != L)
		return false;
	else
		return true;
}

int solution(void){
	int available = 0;
	int* col = new int[N];

	for (int i = 0; i < N; i++){ // check row
		if (is_available(map[i])){
			available++;
		}

		for (int j = 0; j < N; j++){ // check col
			col[j] = map[j][i];
		}
		if (is_available(col)){
			available++;
		}
	}
	return available;
}

int main(void){
	get_input();
	printf("%d", solution());
	/*
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			printf("%d ", map[i][j]);
		}
		printf("\n");
	}
	*/
	return 0;
}