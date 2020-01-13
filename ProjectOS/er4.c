#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/wait.h>

#define N 5000

int foo(){
	int x = 0;
	x++;
	return x;
}

int main(void){
	time_t  begin,end;
	time(&begin);
	clock_t start_t,end_t;
	start_t = clock();
	pid_t pid[N],wpid;
	int status;
	printf("Έναρξη χρόνου %d \n",begin);
	int i = 0;
	while(i <= N){
		pid[i] = fork();
		if(pid[i] == 0){
			foo();		
			exit(0);		 		
		}
	i++;
	}
	
	
	while((wpid = wait(&status))>0);
	time(&end);
	end_t = clock();

	
	double total = (double)(end_t-start_t)/CLOCKS_PER_SEC;
	printf("Τελική ένδειξη ρολογιού %d\n",end_t);
	printf("Χρόνος εκτέλεσης %d διεργασιών =%.20f \n",N,total);
	return(0);
}
