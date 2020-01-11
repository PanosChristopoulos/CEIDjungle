#include <stdio.h>

#include <stdlib.h>

#include <sys/types.h>

#include <semaphore.h>

#include <fcntl.h>

#include <sys/types.h>

#include <sys/wait.h>

#include <unistd.h>


typedef sem_t Semaphore;

Semaphore *simaforos1;
Semaphore *simaforos2;
Semaphore *simaforos3;
Semaphore *simaforos4;

int main(){
	
	int pd;

	simaforos1 = sem_open ("simafor1", O_CREAT | O_EXCL, 0644, 0);
	simaforos2 = sem_open ("simafor2", O_CREAT | O_EXCL, 0644, 0);
	simaforos3 = sem_open ("simafor3", O_CREAT | O_EXCL, 0644, 0);
	simaforos4 = sem_open ("simafor4", O_CREAT | O_EXCL, 0644, 0);

	pd=fork();

	if (pd!=0)
	{
		printf("Diergasia P1\n");
		system("date");
		sem_post(simaforos1);
		wait(NULL);
	}

	else if (pd==0)
	{
		printf("Diergasia P2\n");
		system("date");
		sem_post(simaforos2);
		exit(0);	
	}

	pd=fork();

	if (pd!=0)
	{
		sem_wait(simaforos1);
		sem_wait(simaforos2);
		printf("Diergasia P3\n");
		system("date");
		sem_post(simaforos3);
		sem_post(simaforos4);
		wait(NULL);
	}

	else if (pd==0)
	{
		sem_wait(simaforos3);
		printf("Diergasia P4\n");
		system("date");
		exit(0);
	}

	pd=fork();

	if (pd!=0)
	{
		sem_wait(simaforos4);
		printf("Diergasia P5\n");
		system("date");
		wait(NULL);

		sem_unlink("simaforos1");
		sem_close(simaforos1);

		sem_unlink("simaforos2");
		sem_close(simaforos2);

		sem_unlink("simaforos3");
		sem_close(simaforos3);

		sem_unlink("simaforos4");
		sem_close(simaforos4);
	} 

	return 0;

}

//gedit erwtima_d_a.c
//gcc erwtima_d_a.c -o marios -lpthread
