#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>


int main()
{
int pid1;
int pid2;
pid1 = fork();
if (pid1 < 0)
 printf("Could not create any child\n");
else
{

 pid2 = fork();
 printf("To pid μου είναι %ld  ο πατέρας μου είναι %ld \n", (long)getpid(), (long)getppid());

 if (pid2 < 0)
 printf("Could not create any child\n");
 else if ( (pid1 < 0) && (pid2 < 0) ) {kill(pid1,9);}

;
}

sleep(20);
return (0);
}
