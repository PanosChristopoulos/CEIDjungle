#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
 
int main(void) {
  for(int i = 1; i <= 10; i++) {
    int pid = fork();
 //mono se periptwsh pou h diergasia einai child(pid=0) energopoietai
    if(pid == 0) {
        printf("Για το child process no %d ",i);
      printf("parent process id:%d child process id:%d\n", getppid(), getpid());
      sleep(1);
      exit(0);
    }//afou ginei to exit tou child, me to wait synexizei h ektelesh tou parent
    else  {
      sleep(1);
      wait(NULL);
    }
  }
 
  return EXIT_SUCCESS;
}