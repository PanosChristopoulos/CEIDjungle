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
	pid_t pid[i];
	time_t start_t,end_t,mo_t;
	double diff;
	start_t=time(NULL);
	printf("arxise na na metrei to roloi %ld\n",start_t);
	while(i<100)
	{	i=i+1;
		if ((pid[i]=fork())) {
			foo();
			printf("%d/100 done\n",i);
			exit(i+1);
			i++;
		}
	}
	while (i<100){
		if (pid> 0) {
        while (pid[100] = waitpid (-1, NULL, 0)) {
                if (errno == ECHILD)
                    break;
        }
			printf (" Parent: All children have exited.\n");
		}i++;
	}
	end_t=time(NULL);
	diff=difftime(end_t,start_t);
	printf("oi diergasies piran %lf seconds to run \n",diff);
	printf("o mesos oros xronou ektelesis twn diergasiwn einai %lf seconds\n",diff/100);
	return 0;
	}
	
	
	
	

