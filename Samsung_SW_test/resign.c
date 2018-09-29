#include <stdio.h>

// Problems from : https ://www.acmicpc.net/problem/14501
// Samsung SW 역량 테스트

int *T, *P;
int N;
int maximum = 0;

int calculate(int day, int wage){
	int i, d, w, next;
	if (N < day)
		return -1;
	else if (N == day)
		return wage;
	for (i = day; i < N; i++){
		d = i + T[i];
		w = wage + P[i];
		next = calculate(d, w);
		if (next==-1){
			w = wage;
			if (maximum < wage)
				maximum = wage;
		}
		else {
			w = next;
			if (maximum < next)
				maximum = next;
		}
	}

	return w;
}

int main(void){
	int i, t, p;
	scanf("%d", &N);
	T = (int)malloc(sizeof(int)*N);
	P = (int)malloc(sizeof(int)*N);
	for (i = 0; i < N; i++){
		scanf("%d %d", &t, &p);
		T[i] = t;
		P[i] = p;
	}

	calculate(0, 0);
	printf("%d", maximum);
	return 0;
}
