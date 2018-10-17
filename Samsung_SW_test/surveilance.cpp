// Problems from : https ://www.acmicpc.net/problem/15683
// Samsung SW 역량 테스트

#include <stdio.h>

#define MIN(X, Y) ((X) < (Y) ? (X): (Y))
int N, M;
int** map;

int* r; // coordinate of cctv
int* c;
int cnt = 0; // num of cctv

// {east, north, west, south}
int di[4][4][4] = { { { 1, 0, 0, 0 }, { 0, 1, 0, 0 }, { 0, 0, 1, 0 }, { 0, 0, 0, 1 } }, // 1번
			  { { 1, 0, 1, 0 }, { 0, 1, 0, 1 }, { 0, 0, 0, 0 }, { 0, 0, 0, 0 } }, // 2번
			  { { 1, 1, 0, 0 }, { 0, 1, 1, 0 }, { 0, 0, 1, 1 }, { 1, 0, 0, 1 } }, // 3번
			  { { 1, 1, 1, 0 }, { 1, 1, 0, 1 }, { 1, 0, 1, 1 }, { 0, 1, 1, 1 } } // 4번
			};

int get_input(void){
	scanf_s("%d %d", &N, &M);
	map = new int*[N];
	for (int i = 0; i < N; i++){
		map[i] = new int[M];
		for (int j = 0; j < M; j++){
			scanf_s("%d", &map[i][j]);
			if (map[i][j] != 0 && map[i][j] != 6){
				if (map[i][j] != 5)
					cnt++;
			}
		}
	}
	r = new int[cnt];
	c = new int[cnt];

	int idx = 0;
	for (int i = 0; i < N; i++){
		for (int j = 0; j < M; j++){
			if (map[i][j] == 5){ // if type 5 cctv, then watch all directions
				for (int a = i; a < N; a++){
					if (map[a][j] != 6){
						if (map[a][j] == 0)
							map[a][j] = 7; // being surveilled
					}
					else{
						break;
					}
				}
				for (int a = i; a >= 0; a--){
					if (map[a][j] != 6){
						if (map[a][j] == 0)
							map[a][j] = 7;
					}
					else{
						break;
					}
				}
				for (int a = j; a < M; a++){
					if (map[i][a] != 6){
						if (map[i][a] == 0)
							map[i][a] = 7; // being surveilled
					}
					else{
						break;
					}
				}
				for (int a = j; a >= 0; a--){
					if (map[i][a] != 6){
						if (map[i][a] == 0)
							map[i][a] = 7;
					}
					else{
						break;
					}
				}
			}
			else if (map[i][j] != 0 && map[i][j] != 6 && map[i][j] != 7){ // not type 5
				r[idx] = i;
				c[idx] = j;
				idx++;
			}
		}
	}

	return 1;
}

int** copy(int** arr){
	int** result;
	result = new int*[N];
	for (int i = 0; i < N; i++){
		result[i] = new int[M];
		for (int j = 0; j < M; j++){
			result[i][j] = arr[i][j];
		}
	}
	return result;
}

int score(int **m){
	int s = 0;
	for (int i = 0; i < N; i++){
		for (int j = 0; j < M; j++){
			if (m[i][j] == 0)
				s++;
		}
	}
	return s;
}

int surveil(int **m, int num){
	int min = 64;
	if (num == cnt){
		return score(m);
	}

	int tr = r[num]; // this_x
	int tc = c[num]; // this_y
	int type = map[tr][tc]; // type of cctv
	int n = (type == 2) ? 2 : 4; // num of possible case
	int cr[64], cc[64]; // changed row and col
	int ccnt = 0; // counter for changed spot

	for (int i = 0; i < n; i++){
		// {east, north, west, south}
		if (di[type-1][i][0]){ // east
			for (int a = tc; a < M; a++){
				if (m[tr][a] != 6){
					if (m[tr][a] == 0){
						m[tr][a] = 7; // being surveilled
						cr[ccnt] = tr;
						cc[ccnt] = a;
						ccnt++;
					}
				}
				else{
					break;
				}
			}
		}
		if (di[type - 1][i][1]){ // north
			for (int a = tr; a >= 0; a--){
				if (m[a][tc] != 6){
					if (m[a][tc] == 0){
						m[a][tc] = 7; // being surveilled
						cr[ccnt] = a;
						cc[ccnt] = tc;
						ccnt++;
					}
				}
				else{
					break;
				}
			}
		}
		if (di[type - 1][i][2]){ // west
			for (int a = tc; a >= 0; a--){
				if (m[tr][a] != 6){
					if (m[tr][a] == 0){
						m[tr][a] = 7; // being surveilled
						cr[ccnt] = tr;
						cc[ccnt] = a;
						ccnt++;
					}
				}
				else{
					break;
				}
			}
		}
		if (di[type - 1][i][3]){ // south
			for (int a = tr; a < N; a++){
				if (m[a][tc] != 6){
					if (m[a][tc] == 0){
						m[a][tc] = 7; // being surveilled
						cr[ccnt] = a;
						cc[ccnt] = tc;
						ccnt++;
					}
				}
				else{
					break;
				}
			}
		}
		int temp = surveil(m, num + 1);
		min = MIN(temp, min);
		for (int k = 0; k < ccnt; k++){
			m[cr[k]][cc[k]] = 0;
		}
	}
	return min;
}

int main(void){
	get_input();
	printf("%d", surveil(map, 0));
}