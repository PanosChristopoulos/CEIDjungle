#include<stdint.h>
#include<inttypes.h>
#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<semaphore.h>

void sfreader(void * id) ;
 
void sfwriter(void * id);
   
sem_t cr_mut,readc_mut ; 
 
int noreaders=0 ;  

FILE *filep;

void sfreader(void * id)  
{  
	int c=(int)id ;  
	sleep(2);  
	sem_wait(&readc_mut);
	noreaders++; 
	if(noreaders==1) 
		sem_wait(&cr_mut) ; 
	printf("Ο Reader #%d ξεκινάει\n",noreaders);	
	sem_post(&readc_mut) ;  
	sleep(2) ;  
	filep = fopen("shared_file.txt","r");	  
	if(filep == NULL)
	{
	      printf("!!Σφάλμα στο άνοιγμα του διαμοιραζόμενου αρχείου!!");   
	      exit(1); 
	}    	  
	fscanf(filep,"%d",&c);
	printf("\n Ο reader διαβάζει την τιμή %d από το διαμοιραζόμενο αρχείο. \n",c);
	fclose(filep);
	sem_wait(&readc_mut); 
	noreaders-- ; 
	if(noreaders==0)
		sem_post(&cr_mut) ;  
	sem_post(&readc_mut) ;  
}  

void sfwriter(void * id)  
{  
	int c=(int)id ;  
	sleep(1);  
	sem_wait(&cr_mut) ;  
	printf("\n Ο Writer αποθηκεύει την τιμή %d στο διαμοιραζόμενο αρχείο.\n",c);  	  
	filep = fopen("shared_file.txt","w");   
	if(filep == NULL)
	{
	      printf("Σφάλμα!");   
	      exit(1); 
	}     
	fprintf(filep,"%d",c);
  	fclose(filep);	
	sleep(1);  
	printf("\nΟ Writer ολοκλήρωσε την εγγραφή \n",c);  
	sem_post(&cr_mut) ; 
}

main()  
{  
	int readerCounter=1,writers_num=1;  
	system("clear");  
	sem_init(&cr_mut,1,1) ;  
	sem_init(&readc_mut,1,1) ;  	
	pthread_t singlewriter,readr0,readr1,readr2,readr3,readr4;  
	pthread_create(&singlewriter,NULL,sfwriter,(void *)writers_num);  
	writers_num++;  
	pthread_create(&readr0,NULL,sfreader,(void *)readerCounter);  
	readerCounter++;  
	pthread_create(&readr1,NULL,sfreader,(void *)readerCounter);  
	readerCounter++;
	pthread_create(&readr2,NULL,sfreader,(void *)readerCounter);  	
	readerCounter++;	
	pthread_create(&readr3,NULL,sfreader,(void *)readerCounter);  	
	readerCounter++;
	pthread_create(&readr4,NULL,sfreader,(void *)readerCounter);  	
	readerCounter++;
	pthread_join(singlewriter,NULL);  
	pthread_join(readr0,NULL);  
	pthread_join(readr1,NULL);  
	pthread_join(readr2,NULL); 
	pthread_join(readr3,NULL) ;  
	pthread_join(readr4,NULL) ; 
	printf("\nMain terminated\n");  
 }  



