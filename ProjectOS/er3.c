#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int dierg = 10;

int counter = 0;

void child_func() 
{
    pid_t pid;
    if (counter < dierg) {
        counter++;
        pid = fork();
       if (pid < 0) {
            printf("To fork apetyxe sth diergasia = %d\n", counter);
        }
        else if (pid == 0) {
            printf("Dhmiourgithike paidi me pid %ld\n", (long)getpid());
            if (counter == dierg) {
                exit(0);
            }
            else {
                child_func();
            }
        }
        else {
            long var  = pid;
            int  ppid;
            wait(&pid);
            printf("To pid mou einai %ld eimai o pateras tou %ld child, o pateras mou einai %ld \n", (long)getpid(), var, (long)getppid());
            exit(0);
        }   
    }
}

int main(void) 
{
    pid_t pid;
    pid = fork();
    if (pid < 0) {
        printf("To fork apetyxe %d\n", counter);
        return -1;
    }
    if (pid == 0) {
        child_func();
    }
    else {
        wait(&pid);
    }
    return 0;
}