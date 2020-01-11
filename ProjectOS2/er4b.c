#include <stdio.h>

#include <stdlib.h>

#include <sys/types.h>

#include <semaphore.h>

#include <fcntl.h>

#include <time.h>

#include <sys/wait.h>

#include <unistd.h>

typedef sem_t Semaphore;

Semaphore *simaforos1;
Semaphore *simaforos2;
Semaphore *simaforos3;
Semaphore *simaforos4;
Semaphore *simaforos5;
Semaphore *simaforos6;

int main(){
	int pd;

	simaforos1 = sem_open ("simafor1", O_CREAT | O_EXCL, 0644, 0);
	simaforos2 = sem_open ("simafor2", O_CREAT | O_EXCL, 0644, 0);
	simaforos3 = sem_open ("simafor3", O_CREAT | O_EXCL, 0644, 0);
	simaforos4 = sem_open ("simafor4", O_CREAT | O_EXCL, 0644, 0);
	simaforos5 = sem_open ("simafor5", O_CREAT | O_EXCL, 0644, 0);
	simaforos6 = sem_open ("simafor6", O_CREAT | O_EXCL, 0644, 0);

	pd=fork();

	if (pd!=0)
	{
		sleep(2);
		printf("Diergasia D1 me ID:%d \n",getpid());
		system("date");
		sem_post(simaforos1);
		sem_post(simaforos2);
		wait(NULL);
	}
	else if (pd==0)
	{
		sleep(3);
		sem_wait(simaforos1);
		printf("\nDiergasia D2 me ID: %d\n",getpid());
		system("date");
		sem_post(simaforos3);
		sem_post(simaforos4);
		exit(0);
	}
	pd=fork();

	if (pd!=0)
	{
		sleep(4);
		sem_wait(simaforos2);
		printf("\nDiergasia D3 me ID:%d\n",getpid());
		system("date");
		sem_post(simaforos5);
		sem_post(simaforos6);
		wait(NULL);
	}

	else if (pd==0)
	{
		sleep(5);
		sem_wait(simaforos3);
		printf("\nDiergasia D4 me ID: %d\n",getpid());
		system("date");
		exit(0);
	}

	pd=fork();

	if (pd!=0)
	{
		sleep(6);
		sem_wait(simaforos4);
		sem_wait(simaforos5);
		printf("\nDiergasia D5 me ID:%d\n",getpid());
		system("date");
		wait(NULL);

		sem_unlink("simafor1");
		sem_close(simaforos1);
		sem_unlink("simafor2");
		sem_close(simaforos2);

		sem_unlink("simafor3");
		sem_close(simaforos3);

		sem_unlink("simafor4");
		sem_close(simaforos4);

		sem_unlink("simafor5");
		sem_close(simaforos5);

		sem_unlink("simafor6");
		sem_close(simaforos6);
	}
	else if (pd==0)
	{
		sleep(7);
		sem_wait(simaforos6);
		printf("\nDiergasia D6 me ID:%d\n",getpid());
		system("date");
		exit(0);
	}
	return 0;
}
