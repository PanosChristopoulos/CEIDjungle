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
            printf("Το fork απέτυχε στη διεργασία %d\n", counter);
        }
        else if (pid == 0) {
            printf("Δημιουργήθηκε το %dο παιδί με pid %ld\n",counter, (long)getpid());
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
            printf("To pid μου είναι %ld είμαι ο πατέρας του %ld child, ο πατέρας μου είναι %ld \n", (long)getpid(), var, (long)getppid());
            exit(0);
        }   
    }
}

int main(void) 
{
    pid_t pid;
    pid = fork();
    if (pid < 0) {
        printf("Το fork απέτυχε %d\n", counter);
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
