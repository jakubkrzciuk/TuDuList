#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys,time
with open('zadania.txt','r') as file:
    tudu = file.read().splitlines()
p=("[ ]")
l=("[x]")

def start():
        while True:
            opt = input("Please specify a command [list, add, mark, archive, exit]: ")
            if opt == 'list':
                list_opt()
            elif opt == 'add':
                add_opt()
            elif opt == 'mark':
                mark_opt()
            elif opt == 'archive':
                archive_opt()
            elif opt == 'exit':
                with open('zadania.txt', 'w') as file:
                    for item in tudu:
                        file.write(str(item) + '\n')
                exit()

def add_opt():
    z=input("add an item: ")
    tudu.append(p+z)
    time.sleep(0.5)
    print("item added.")

def list_opt():
    print("You saved following to-do items:")
    if not tudu:
        print('Empty list.')
    else:
        for index,element in enumerate(tudu,1):
            print(str(index)+'.',element)

def archive_opt():
    if tudu:
        for o in range(len(tudu)):
            for i in range(len(tudu)):
                if tudu[i][:3]==l:
                    del tudu[i]
                    print("All completed tasks got deleted.")
                    break

def mark_opt():
    for c,value in enumerate(tudu,1):
        print(c,tudu[c-1])
    p=int(input("Which one you want to mark as completed: "))
    c=tudu[p-1]
    c=l+c[3:]
    tudu[p-1]=c
    for c,value in enumerate(tudu,1):
        print(c,tudu[c-1])


def main():
    start()
if __name__ == '__main__':
    main()
