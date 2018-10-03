#include <stdio.h>


typedef int bool;
#define true 1
#define false 0

int(*get_map(int N, int M))[] {
	int **map = (int**)malloc(sizeof(int*)*N);
	int i, j;
	for (i = 0; i < N; i++) {
		map[i] = (int*)malloc(sizeof(int)*M);
		map[i][0] = 1;
		for (j = 1; j < M - 1; j++) {
			if (i == 0 || i == N - 1) {
				map[i][j] = 1;
				continue;
			}
			scanf("%d", &map[i][j]);
		}
		map[i][M - 1] = 1;
	}

	return map;
}

int score_safe_zone(int** map, int N, int M) {
	int score = 0;
	int i, j;
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			if (map[i][j] != 1 && map[i][j] != 2) // 벽도 아니고, 바이러스도 없으면
				score++;
		}
	}

	return score;
}

int floodAndScore(int** inp_map, int N, int M) {
	int i, j, score;
	bool flag = false;
	int **this_map = (int**)malloc(sizeof(int*)*N);
	for (i = 0; i < N; i++) {
		this_map[i] = (int*)malloc(sizeof(int)*M);
		for (j = 0; j < M; j++) {
			this_map[i][j] = inp_map[i][j];
		}
	}

	while (1) { // bfs방식이 아니라 단순 반복으로 
		flag = false;
		for (i = 0; i < N; i++) {
			for (j = 0; j < M; j++) {
				if (this_map[i][j] == 2) {
					if (this_map[i - 1][j] != 1 && this_map[i - 1][j] != 2) {
						this_map[i - 1][j] = 2;
						flag = true;
					}
					if (this_map[i + 1][j] != 1 && this_map[i + 1][j] != 2) {
						this_map[i + 1][j] = 2;
						flag = true;
					}
					if (this_map[i][j - 1] != 1 && this_map[i][j - 1] != 2) {
						this_map[i][j - 1] = 2;
						flag = true;
					}
					if (this_map[i][j + 1] != 1 && this_map[i][j + 1] != 2) {
						this_map[i][j + 1] = 2;
						flag = true;
					}
				}
			}
		}
		if (flag == false) {
			break;
		}
	}
	score = score_safe_zone(this_map, N, M);
	for (i = 0; i < N; i++) free(this_map[i]);
	free(this_map);
	return score;
}

int chk_8neighbor(int** map, int a, int b) {
	int point = 0;
	int i, j;

	for (i = a - 1; i < a + 2; i++) {
		for (j = b - 1; j < b + 2; j++) {
			if (map[i][j] == 1)
				point++;
		}
	}
	if (point > 0) { // 8 neighbor에 벽이 하나라도 있으면
		return true;
	}
	else {
		return false;
	}
}

int set_wall(int** map, int N, int M, int num_wall) {
	int i, j;
	int maximum = 0;
	int score = 0;
	int **this_map = (int**)malloc(sizeof(int*)*N);
	for (i = 0; i < N; i++) {
		this_map[i] = (int*)malloc(sizeof(int)*M);
		for (j = 0; j < M; j++) {
			this_map[i][j] = map[i][j];
		}
	}

	for (i = 1; i < N - 1; i++) {
		for (j = 1; j < M - 1; j++) {
			if (this_map[i][j] == 0 && chk_8neighbor(this_map, i, j)) { // 벽 세울 후보지 선정
				this_map[i][j] = 1;

				if (num_wall == 0) {
					score = set_wall(this_map, N, M, num_wall + 1);
					this_map[i][j] = 3; // 0에서 지나간 곳 for 중복 방지

				}
				else if (num_wall == 1) {
					score = set_wall(this_map, N, M, num_wall + 1);
					this_map[i][j] = 4; // 1에서 지나간 곳
				}
				else if (num_wall == 2) {
					score = floodAndScore(this_map, N, M);
					if (maximum < score) {
						maximum = score;
					}
					this_map[i][j] = 5; // 2에서 지나간 곳
					continue;
				}
				if (maximum < score) {
					maximum = score;
				}
			}
		}
	}
	for (i = 0; i < N; i++) free(this_map[i]);
	free(this_map);
	return maximum;
}

int main(void) {
	int** map;
	int i, N, M, result;
	scanf("%d %d", &N, &M);
	N += 2; M += 2; // for padding
	map = get_map(N, M);

	result = set_wall(map, N, M, 0);
	printf("%d", result);

	for (i = 0; i < N; i++) free(map[i]);
	free(map);

	return 0;
}