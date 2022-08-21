import thread_cnblogs
import threading
import time

def single_thread():
    print('single_thread begin')
    for url in thread_cnblogs.urls:
        thread_cnblogs.crawl(url)
    print('single_thread end')

def multi_thread():
    print('multi_thread begin')
    threads = []
    for url in thread_cnblogs.urls:
       threads.append(
           threading.Thread(target=thread_cnblogs.crawl,args=(url,))
       )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print('multi_thread end')

if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print('single_thread cost:',end - start,'seconds')
    start = time.time()
    multi_thread()
    end = time.time()
    print('multi_thread cost:', end - start, 'seconds')