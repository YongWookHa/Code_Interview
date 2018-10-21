// Problems from : https://www.acmicpc.net/problem/14891
// Samsung SW 역량 테스트

#include <stdio.h>

int tw[4][8]; // toothed_wheel
int pw[4] = {0, 0, 0, 0}; // 12 o'clock direction of wheels
int K;
int** R; // rotate

int get_input() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 8; j++) {
			scanf("%1d", &tw[i][j]);
		}
	}
	scanf("%d", &K);
	R = new int*[K];
	for (int i = 0; i < K; i++) {
		R[i] = new int[2];
		scanf("%d", &R[i][0]);
		scanf("%d", &R[i][1]);
	}
	return 1;
}

int score() {
	int s = 0;
	int point = 1;
	for (int i = 0; i < 4; i++) {
		if (tw[i][pw[i]] == 1)
			s += point;
		point *= 2;
	}
	return s;
}

void rotate(int t, int d, int* ready) { // rotate target toward the direction
	pw[t-1] = (pw[t-1] - d + 8) % 8; // renew 12 o'clock point of an wheel
	if (ready[t - 1]) {
		ready[t - 1] = 0;
		rotate(t - 1, -d, ready);
	}
	if (ready[t]) {
		ready[t] = 0;
		rotate(t + 1, -d, ready);
	}
}

int solution() {
	int target, direction, a, b;
	for (int i = 0; i < K; i++) {
		int ready[5] = { 0,0,0,0,0 };
		for (int j = 0; j < 3; j++) {
			a = tw[j][(pw[j] + 2) % 8]; // 3 o'clock
			b = tw[j + 1][(pw[j+1] - 2 + 8) % 8]; // 9 o'clock
			ready[j+1] = (a != b) ? 1 : 0; // wheel can be rotated
		}
		target = R[i][0]; 
		direction = R[i][1]; // direction to rotate
		rotate(target, direction, ready); // bfs
	}

	return score();
}

int main(void) {
	get_input();
	printf("%d", solution());
	return 0;
}