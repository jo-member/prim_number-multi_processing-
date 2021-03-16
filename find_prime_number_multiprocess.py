import time
from math import sqrt
import csv
import argparse
from multiprocessing import Process,Manager

def isprime(n):
    '''
    :param n(int): number that you want to know whether it's prime number
    :return(bool)
    '''
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if not n%i:
            return False
    return True

def return_prime(start,end,prime_list):
    '''
    :param start: start number
    :param end: end number
    :param prime_list: list which has a prime number
    '''
    for i in range(start,end+1):
        if isprime(i):
            prime_list.append(i)


if __name__ == "__main__":
    manager = Manager()
    prime_list = manager.list()
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--process_number', type=int,
                        help='number of processor that you want to use')
    parser.add_argument('--number', type=int,
                        help='number that you want to find prime number')
    process_number = parser.parse_args().process_number
    number = parser.parse_args().number
    
    proc_list = []
    start_time = time.time()
    
    start = 1
    end =number // process_number
    
    for i in range(process_number):
        proc = Process(target=return_prime,args=(start,end,prime_list))
        proc_list.append(proc)
        proc.start()
        start = end+1
        end = end+1000//process_number
        
    for proc in proc_list:
        proc.join()
        
    t = time.time()-start_time
    
    file_name = 'primelist'+str(number)+'_and_time('+str(process_number)+'_process).csv'
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(prime_list)
        writer.writerow([t])

