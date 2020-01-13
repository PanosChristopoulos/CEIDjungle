#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <semaphore.h>
#include <fcntl.h>    
#include <unistd.h> 
#include <errno.h>  
#include <sys/shm.h> 
#include <sys/types.h>   
 
 int heap[100];
 int count=0;
 sem_t *sim1;


int getIdxGonea(int index){
  return index/2;
 }

int getIdxArPaidiou(int index){
  return index*2;
}

int getIdxDexPaidiou (int index){
  return index*2+1;
}

void upheapmin(int index){
    if (index<=1) return;
    int parentIdx = getIdxGonea(index);
    if(heap[index] < heap[parentIdx]){
      int temp = heap[index];
      heap[index] = heap[parentIdx0];
      heap[parentIdx] = temp;
      upheapmin(parentIdx);
    }
}

void push(int value){
  count++
  heap[count] = value;
  upheapmin(count);
}

void downheapmin(int index){
  if(index*2 > count) return;
  int left = getIdxArPaidiou(index);
  int right = getIdxDexPaidiou(index);

  int smallest = index;
  if(left <= count && heap[left] < heap[smallest]){
    smallest = left;
  }
  if(right <= count && heap[right] < heap[smallest]){
    smallest = right;
  }

  if(smallest == index) return;

  int temp = heap[index];
  heap[index] = heap[smallest];
  heap[smallest] = temp;

  downheapmin(smallest)
}



void pop(){
  if(count == 0){
    return;
  }
  heap[1] = heap[count];
  count--;
  downheapmin(1);

}



void view(){
  int i;
  for (i=1; i<=count; i++){
    printf("%2d ", heap[i]);
  }
  printf("\n");
}

void eisagwghprocess(){
  sem_wait(sim1);
  push(getpid());
  sem_post(sim1);

}

int main() {

  Sem1 = sem_open ("Sem1", O_CREAT | O_EXCL, 0644, 1);
  for(int i = 1; i <= 100; i++) {
    int pid = fork();

 if(pid == 0) {
      printf("Για το child process no %d ",i);
      printf("parent process id:%d child process id:%d\n", getppid(), getpid());
      eisagwghprocess();
      sleep(1);
      exit(0);
    }
    else  {
      sleep(1);
      wait(NULL);
    }
  }
 
   sem_unlink ("sim1");sem_close(Sim1);
   view(heap);
   munmap(heap, NO_OF_PROCESSES*sizeof(index));
   munmap(heap, sizeof(heap));
   exit(0);
}