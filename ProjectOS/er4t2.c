#include<unistd.h>
#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<sys/wait.h>
#include <sys/wait.h>
#include <errno.h>

void foo(){
int x;
x=x+1;
}
int main()
{
	int i=0,status;
	time_t start_t,end_t,mo_t;
	double diff;
	start_t=time(NULL);
	printf("arxise na metraei to roloi %ld\n",start_t);
  while(i <100) {
  	i=i+1;
    int pid[] = [fork();]
    if(pid[i] == 0) {
        printf("Child process no %d generated\n",i);
    }//afou ginei to exit tou child, me to wait synexizei h ektelesh tou parent
    else  {
      wait(NULL);
    }
  }
	end_t=time(NULL);
	diff=difftime(end_t,start_t);
	printf("oi diergasies piran %lf seconds na ektelestoun \n",diff);
	printf("o mesos oros xronou ektelesis twn diergasiwn einai %lf seconds\n",diff/100);
	return 0;
	}
	
	
	
	

