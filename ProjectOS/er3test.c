#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int dierg = 10;
int counter = 0;
void child() 
{ //Δημιουργήσαμε την child function για να ελέγχεται ο ακριβής αριθμός των παιδιών και να καλείται η fork αναδρομικά
    pid_t pid;
    if (counter < dierg) {
        counter++;
        pid = fork();
       if (pid < 0) {
            printf("To fork apetyxe sth diergasia = %d\n", counter);
        }
        else if (pid == 0) {
            printf("Dhmiourgithike to %d o paidi me pid %ld\n",counter, (long)getpid());
            sleep(1); //το pid του παιδιού που δημιουργήθηκε
            if (counter == dierg) {
                exit(0);
            }
            else {
                child();
            }
        }
        else { //Παρουσιάζεται το ζητούμενο του ερωτήματος (pid διεργασίας, id παιδιού και id πατέρα)
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
        child();sleep(1);
    }
    else {
        wait(&pid);
    }
    return 0;
}
