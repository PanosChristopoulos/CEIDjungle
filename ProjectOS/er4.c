#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/wait.h>

#define N 5000

int nothing(){
	int x = 0;
	x++;
	return x;
}

int main(void){
	time_t  begin,end;
	time(&begin);
	//clock_t start_t,end_t;
	//start_t = clock();
	pid_t pid[N],wpid;
	int status;
	//printf("Initial Seconds: %d \n",start_t);
	printf("Initial Seconds: %d \n",begin);
	int i = 0;
	while(i <= N){
		pid[i] = fork();
		if(pid[i] == 0){
			nothing();		
			exit(0);		 		
		}
	i++;
	}
	
	
	while((wpid = wait(&status))>0);
	time(&end);
	//end_t = clock();
	/*
	for(i=0;i<N;i++){
			
		if(WIFEXITED(status)){
			printf("Child %d terminated with exit status %d\n",wpid,WEXITSTATUS(status));
		}else{
			printf("Child %d terminated abnormally\n",wpid);	
		}
	}
	*/
	double total = (double)(end-begin)/(double)(N);
	//double total = (double)(end_t-start_t)/CLOCKS_PER_SEC;
	//printf("Final seconds value: %d\n",end_t);
	printf("(end-start)/%d=%.20f \n",N,total);
	return(0);
}
