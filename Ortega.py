



#Author : Prabhat

#Description : This is an interactive research assistant, for computational purposes;

#Note : Although, Knowledge/Information gathering can be done using the tool, you're not suggested to totally relay on the tool (*sigh* or, you'll face some bugs and glitches) '''



import os

import time

import pyttsx3

import colorama

import wolframalpha

import speech_recognition as sr

import random

import sys

import wikipedia

from colorama import Fore,Back,Style

import base64

os.system("cls")

#初期化

r = sr.Recognizer()

engine = pyttsx3.init()

rate = engine.getProperty('rate')                           

engine.setProperty('rate', 150)

engine = pyttsx3.init()



os.system("cls")

print(Style.RESET_ALL)



#定義

engine.say("What do you want the input method to be?")

print("\n\n\nWhat do you want the input method to be?\n\n   [1] Type\n   [2] Speech")

engine.runAndWait()

mode = input()





os.system("cls")

print(Fore.GREEN+Style.BRIGHT)

print( '\t'*7+'                     .                          ')

print( '\t'*7+'     Legalize        M                          ')

print( '\t'*7+'          Cannabis  dM                          ')

print( '\t'*7+'                    MMr                         ')

print( '\t'*7+'                   4MMML                  .     ')

print( '\t'*7+'                   MMMMM.                xf     ')

print( '\t'*7+'   .              "MMMMM               .MM-     ')

print( '\t'*7+'    Mh..          +MMMMMM            .MMMM      ')

print( '\t'*7+'    .MMM.         .MMMMML.          MMMMMh      ')

print( '\t'*7+'     )MMMh.        MMMMMM         MMMMMMM       ')

print( '\t'*7+'      3MMMMx.     \'MMMMMMf      xnMMMMMM"       ')

print( '\t'*7+'      \'*MMMMM      MMMMMM.     nMMMMMMP"        ')

print( '\t'*7+'        *MMMMMx    "MMMMM\\    .MMMMMMM=        ') 

print( '\t'*7+'         *MMMMMh   "MMMMM"   JMMMMMMP           ')

print( '\t'*7+'           MMMMMM   3MMMM.  dMMMMMM            .')

print( '\t'*7+'            MMMMMM  "MMMM  .MMMMM(        .nnMP"')

print( '\t'*7+'=..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*  ')

print( '\t'*7+'  "MMn...     \'MMMMr \'MM   MMM"   .nMMMMMMM*"   ')

print( '\t'*7+'   "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""     ')

print( '\t'*7+'     ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"        ')

print( '\t'*7+'        *PMMMMMMhn. *x > M  .MMMM**""           ')

print( '\t'*7+'           ""**MMMMhx/.h/ .=*"                  ')

print( '\t'*7+'                    .3P"%....                   ')

print( '\t'*7+'                  nP"     "*MMnx         Prabhat')

time.sleep(3)

print(Style.RESET_ALL)



#あいさつ



def exit():

	os.system('cls')

	engine.say("Alright .. Exiting!")

	engine.runAndWait()



def say(var):

	engine.say(var)

	engine.runAndWait()



def name():

	say("My name is Ortega, atleast that's what \"he\" (my creator) calls me!")

	print("My name is Ortega")

	print("Atleast that's what \"He\" (My Creator) calls me.")

	print("\n\t\t\t\t\t :)")

	time.sleep(2)



def creator():

	say("Prabhat is my creator.")

	print("Prabhat is my creator.")

	rate = engine.getProperty('rate')                           

	engine.setProperty('rate', 205)     

	say("Waahi haai saarva shaakti shaaali bhaagwaaan, aasvaatthhaaamaa.")

	print("Wahi hai saarva shakti-shaali bhagwaan, Asvathama!")

	time.sleep(2)

	say("He also is my doctor, whenever I get a bug, he solves it with ease. caring he is.! ")



def god():

	say("Praabhaaat. Wahi haai saarva shaakti shaaali bhaagwaaan, aasvaatthhaaamaa!")

	print("Prabhat")

	print("Wahi hai saarva shakti-shaali bhagwaan, Asvathama!")



def wait():

	os.system("cls")

	say("Alright .. Waiting ... Press any key to End.")

	print("\n\n\nAlright \n..Waiting \n...Press any key to End")

	for i in range(10):

		for cursor in '\\|/-':

			time.sleep(0.1)

			sys.stdout.write('\r{}'.format(cursor))

			sys.stdout.flush()

	os.system("cls")

	input("\n\n\nAlright \n..Waiting \n...Press any key to End")

def wiki():
	
	exec(base64.b64decode("ZW5naW5lLnNheSgibGV0IG1lIGFzayBXaWNoaXNoaWtpIikKCnByaW50KCJMZXQgbWUgYXNrIFdpY2hpc2hpa2kgOikiKQoKZW5naW5lLnJ1bkFuZFdhaXQoKQoKZW5naW5lLnNheSgiV2hhdCBkbyB5b3Ugd2FudCB0byBrbm93IGFib3V0PyIpCgpwcmludCgiXG5cblxuXG5cdFx0XHRcdFdoYXQgZG8geW91IHdhbnQgdG8ga25vdyBhYm91dD9cblxuIikKCmVuZ2luZS5ydW5BbmRXYWl0KCkKCnJlcXVlc3QgPSBpbnB1dCgiXG5cdFx0XHRcdD4/PSIpCgpyZXNwb25zZSA9IHdpa2lwZWRpYS5zdW1tYXJ5KHJlcXVlc3QpCgplbmdpbmUuc2F5KHJlc3BvbnNlKQoKcHJpbnQocmVzcG9uc2UpCgplbmdpbmUucnVuQW5kV2FpdCgpIAoKaW5wdXQoKQ=="))

def lyrics():
	
	exec(base64.b64decode("cHJpbnQoIlByYWJoYXQiKQoKcHJpbnQoIi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0iKQoKaW5wPWlucHV0KCJlbnRlciBuYW1lIG9mIGFydGlzdCBhbmQgbmFtZSBvZiBzb25nIHNlcGFyYXRlZCBieSAvIDogICAiKS5sb3dlcigpLnJlcGxhY2UoIiAiLCAnJylvciJlZHNoZWVyYW4vZXJhc2VyIjtpbnA9aW5wLnNwbGl0KCcvJykgaWYgJy8nIGluIGlucCBhbmQgaW5wLmNvdW50KCcvJykgPT0gMSBlbHNlICd5b3UgbmVlZCB0byBzZXBlcmF0ZSB0aGUgYXJ0aXN0IG5hbWUgZnJvbSBoaXMvaGVyIHRpdGxlIHVzaW5nIC8nIGlmIG5vdCAnLycgaW4gaW5wIG9yIGlucC5jb3VudCgnLycpID4gMSBlbHNlICdJbnZhbGlkIGlucHV0Li4uLlxucGxlYXNlIGNoZWNrIHRoZSB0b3AgY29tbWVudCBvZiB0aGlzIGNvZGUnO2FydGlzdCx0aXRsZSA9IGlucFswXSxpbnBbMV0KCnByaW50KCdBcnRpc3Q6IHt9XG5UaXRsZToge31cbnt9Jy5mb3JtYXQoYXJ0aXN0LnRpdGxlKCksdGl0bGUudGl0bGUoKSwnLScqMjUpKQoKaW1wb3J0IHJlCgpmcm9tIHVybGxpYi5yZXF1ZXN0IGltcG9ydCB1cmxvcGVuOyBmcm9tIGh0bWwucGFyc2VyIGltcG9ydCBIVE1MUGFyc2VyCgpsaW5rID0gdXJsb3BlbigiaHR0cHM6Ly93d3cuYXpseXJpY3MuY29tL2x5cmljcy97fS97fS5odG1sIi5mb3JtYXQoYXJ0aXN0LHRpdGxlKSkucmVhZCgpCgpsaW5rID0gc3RyKGxpbmspCgpjbGFzcyBNeUhUTUxQYXJzZXIoSFRNTFBhcnNlcik6CgogICAgZGVmIF9faW5pdF9fKHNlbGYpOgoKICAgICAgICBzdXBlcigpLl9faW5pdF9fKCkKCiAgICAgICAgc2VsZi5wPUZhbHNlCgogICAgICAgIHNlbGYucGJ1Zj1bXQoKICAgIGRlZiBoYW5kbGVfc3RhcnR0YWcoc2VsZiwgdGFnLCBhdHRycyk6CgogICAgICAgIGF0dHJzID0gZGljdChhdHRycykKCiAgICAgICAgaWYgdGFnPT0iZGl2IiBhbmQgbm90IGF0dHJzOgoKICAgICAgICAgICAgc2VsZi5wPVRydWUKCiAgICAgICAgICAgIHNlbGYucGJ1Zj1bXQoKICAgIGRlZiBoYW5kbGVfZW5kdGFnKHNlbGYsIHRhZyk6CgogICAgICAgIGlmIHRhZz09ImRpdiIgYW5kIHNlbGYucDoKCiAgICAgICAgICAgIHNlbGYucD1GYWxzZQoKICAgICAgICAgICAgcHJpbnQoIlxuIi5qb2luKHNlbGYucGJ1ZiksZmx1c2g9MSkKCiAgICAgICAgICAgIHNlbGYucGJ1ZiA9W10KCiAgICBkZWYgaGFuZGxlX2RhdGEoc2VsZiwgZGF0YSk6CgogICAgICAgIGlmKHNlbGYucCk6CgogICAgICAgICAgICBkYXRhPWRhdGEucmVwbGFjZSgiXFxuIiwiXG4iKQoKICAgICAgICAgICAgZGF0YT1kYXRhLnJlcGxhY2UoIlxcIiwiIikKCiAgICAgICAgICAgIGRhdGEgPSByZS5zdWIocidcYnJcYicsICcnLCBkYXRhKQoKICAgICAgICAgICAgc2VsZi5wYnVmLmFwcGVuZChkYXRhLnN0cmlwKCkpCgpwYXJzZXIgPSBNeUhUTUxQYXJzZXIoKQoKcGFyc2VyLmZlZWQobGluaykKCnByaW50KCdcblxuUHJhYmhhdCcp"))

def cmd():
	
	os.system('start')





#知識源
exec(base64.b64decode("d2hpbGUgVHJ1ZToKCglvcy5zeXN0ZW0oImNscyIpCgoJZW5naW5lLnNheSgiV2hhdCdzIHlvdSBRdWVyeT8iKQoKCXByaW50KCJcblxuXG5cbldoYXQncyB5b3VyIFF1ZXJ5PzogIikKCgllbmdpbmUucnVuQW5kV2FpdCgpCgoKCgoKCSNTZXR0aW5nIHRoZSBJbnB1dCBNZXRob2QKCglpZiBpbnQobW9kZSk9PTE6CgoJCWlucHQgPSBpbnB1dCgiIikKCgoKCWVsaWYgaW50KG1vZGUpPT0yOgoKCQl3aXRoIHNyLk1pY3JvcGhvbmUoKSBhcyBzb3VyY2U6CgoJCQkJCWlucHQgPSByLmxpc3Rlbihzb3VyY2UpCgoJCQkJCXRyeToKCgkJCQkJCWlucHQgPSByLnJlY29nbml6ZV9nb29nbGUoaW5wdCkKCgkJCQkJZXhjZXB0OgoKCQkJCQkJZW5naW5lLnNheSgiU29ycnkgY291bGQgbm90IHJlY29nbml6ZSB5b3VyIHZvaWNlLCB0cnkgYWdhaW4iKQoKCQkJCQkJZW5naW5lLnJ1bkFuZFdhaXQoKQoKCQkJCQkJcHJpbnQoIlNvcnJ5IGNvdWxkIG5vdCByZWNvZ25pemUgeW91ciB2b2ljZSA6LyIpCgoJCQkJCQlwcmludCgiVHJ5IGFnYWluIikKCgkJCQkJCWVuZ2luZS5ydW5BbmRXYWl0KCkKCgkJCQkJCXdpdGggc3IuTWljcm9waG9uZSgpIGFzIHNvdXJjZToKCgkJCQkJCQlpbnB0ID0gci5saXN0ZW4oc291cmNlKQoKCQkJCQkJCXRyeToKCgkJCQkJCQkJaW5wdCA9IHIucmVjb2duaXplX2dvb2dsZShpbnB0KQoKCQkJCQkJCWV4Y2VwdDoKCgkJCQkJCQkJZW5naW5lLnNheSgiU29ycnkgY291bGQgbm90IHJlY29nbml6ZSB5b3VyIHZvaWNlLCAuLi4gRXhpdGluZyIpCgoJCQkJCQkJCWVuZ2luZS5ydW5BbmRXYWl0KCkKCgkJCQkJCQkJcHJpbnQoIlNvcnJ5IGNvdWxkIG5vdCByZWNvZ25pemUgeW91ciB2b2ljZTovIikKCgkJCQkJCQkJcHJpbnQoIkV4aXRpbmciKQoKCQkKCgkjQ29tcHV0YXRpb24KCglpZiBpbnB0PT0icXVpdCI6CgoJCWV4aXQoKQoKCQlicmVhawoKCWVsaWYgaW5wdD09ImV4aXQiOgoKCQlleGl0KCkKCgkJYnJlYWsKCgllbGlmIGlucHQ9PSJsZWF2ZSBtZSBhbG9uZSI6CgoJCWV4aXQoKQoKCQlicmVhawoKCWVsaWYgaW5wdD09Imp1c3Qgc2h1dCB0aGUgZnVjayB1cCI6CgoJCWV4aXQoKQoKCQlicmVhawoKCWVsaWYgaW5wdD09InNodXQgdXAiOgoKCQl3YWl0KCkKCgkJYnJlYWsKCgllbGlmIGlucHQ9PSJjbG9zZSI6CgoJCWV4aXQoKQoKCQlicmVhawoKCWVsaWYgaW5wdD09ImhvdyBkbyBpIHF1aXQiOgoKCQlleGl0KCkKCgkJYnJlYWsKCgllbGlmIGlucHQ9PSJ3aGF0IGlzIHlvdXIgbmFtZSI6CgoJCW5hbWUoKQoKCQljb250aW51ZQoKCWVsaWYgaW5wdD09IndoYXQncyB5b3VyIG5hbWUiOgoKCQluYW1lKCkKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJ5b3VyIG5hbWUiOgoKCQluYW1lKCkKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJ3aG8gYXJlIHlvdSI6CgoJCW5hbWUoKQoKCQljb250aW51ZQoKCWVsaWYgaW5wdD09IndobyBtYWRlIHlvdSI6CgoJCWNyZWF0b3IoKQoKCQljb250aW51ZQoKCWVsaWYgaW5wdD09ImNoYW5nZSBtb2RlIjoKCgkJbW9kZSgpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0id2hvIGNyZWF0ZWQgeW91IjoKCgkJY3JlYXRvcigpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0ic3RhcnQgc3BlYWtpbmciOgoKCQltb2RlKCkKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJjaGFuZ2UgaW5wdXQgbWV0aG9kIjoKCgkJbW9kZSgpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0iY2hhbmdlIGlucHV0IG1vZGUiOgoKCQltb2RlKCkKCgkJY29udGludWUJCgoJZWxpZiBpbnB0PT0id2hvJ3MgeW91ciBjcmVhdG9yIjoKCgkJY3JlYXRvcigpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0id2hvIGlzIHlvdXIgY3JlYXRvciI6CgoJCWNyZWF0b3IoKQoKCQljb250aW51ZQoKCWVsaWYgaW5wdD09IndobyBpcyB5b3UgZ29kIjoKCgkJZ29kKCkKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJ3aG8ncyB5b3VyIGdvZCI6CgoJCWdvZCgpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0iYmhhZ3dhYW4gbWVpbiBtYWFudGUgaG8iOgoKCQlnb2QoKQoKCQljb250aW51ZQoKCWVsaWYgaW5wdD09IndhaXQiOgoKCQl3YWl0KCkKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJqdXN0IHdhaXQgZm9yIHNvbWUgdGltZSI6CgoJCXdhaXQoKQoKCQljb250aW51ZQoKCWVsaWYgaW5wdD09IndpbGwgeW91IHdhaXQiOgoKCQl3YWl0KCkKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJob2xkIG9uIjoKCgkJd2FpdCgpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0iaGFuZyBvbiI6CgoJCXdhaXQoKQoKCQljb250aW51ZQoKCWVsaWYgaW5wdD09ImhhbHQiOgoKCQl3YWl0KCkKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJzdGF5IjoKCgkJd2FpdCgpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0icGF1c2UiOgoKCQl3YWl0KCkKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJsZXQgbWUgc2VlIjoKCgkJd2FpdCgpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0iYmFyZSB3aXRoIG1lIjoKCgkJd2FpdCgpCgoJCWNvbnRpbnVlCgoJZWxpZiAid2lraSIgaW4gaW5wdDoKCgkJd2lraSgpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0ib3BlbiB3aWtpcGVkaWEiOgoKCQl3aWtpKCkKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJ3aWtpcGVkaWEiOgoKCQl3aWtpKCkKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJzZWFyY2ggd2lraXBlZGlhIjoKCgkJd2lraSgpCgoJCWNvbnRpbnVlCgoJZWxpZiAic2VhcmNoIHdpa2lwZWRpYSBmb3IiIGluIGlucHQ6CgoJCXdpa2koaW5wdC5yZXBsYWNlKCJzZWFyY2ggd2lraXBlZGlhIGZvciIsIiIpKQoKCQljb250aW51ZQoKCWVsaWYgaW5wdD09ImxhdW5jaCB3aWtpcGVkaWEiOgoKCQl3aWtpKCkKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJ3aWNoaXNoaWtpIjoKCgkJd2lraSgpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0ibGF1bmNoIHdpY2hpc2hpa2kiOgoKCQl3aWtpKCkKCgkJY29udGludWUKCgllbGlmICJzZWFyY2ggd2ljaGlzaGlraSIgaW4gaW5wdDoKCgkJd2lraSgpCgoJCWNvbnRpbnVlCgoJZWxpZiAic2VhcmNoIHdpY2hpc2hpa2kgZm9yIiBpbiBpbnB0OgoKCQl3aWtpKGlucHQucmVwbGFjZSgic2VhcmNoIHdpY2hpc2hpa2kgZm9yIiwiIikpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0ibGF1bmNoIGNvbW1hbmQgcHJvbXB0IjoKCgkJY21kKCkKCgkJaW5wdXQoIiIpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0ibGF1bmNoIHRlcm1pbmFsIjoKCgkJY21kKCkKCgkJaW5wdXQoIiIpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0ibGF1bmNoIHNoZWxsIjoKCgkJY21kKCkKCgkJaW5wdXQoIiIpCgoJCWNvbnRpbnVlCgoJZWxpZiBpbnB0PT0ib3BlbiB0ZXJtaW5hbCI6CgoJCWNtZCgpCgoJCWlucHV0KCIiKQoKCQljb250aW51ZQoKCWVsaWYgaW5wdD09Im9wZW4gY29tbWFuZCBwcm9tcHQiOgoKCQljbWQoKQoKCQlpbnB1dCgiIikKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSJvcGVuIHNoZWxsIjoKCgkJY21kKCkKCgkJaW5wdXQoIiIpCgoJCWNvbnRpbnVlCgoJZWxpZiAibHlyaWNzIiBpbiBpbnB0OgoKCQlseXJpY3MoKQoKCQlpbnB1dCgiIikKCgkJY29udGludWUKCgllbGlmIGlucHQ9PSIiOgoKCQllbmdpbmUuc2F5KCJEaWRuJ3QgcmVjaWV2ZSBhbnkgaW5wdXQsIHRyeSBhZ2FpbiIpCgoJCXByaW50KCJEaWRuJ3QgcmVjaWV2ZSBhbnkgaW5wdXQsXHQ6XFxcblx0XHRUcnkgQWdhaW4iKQoKCQllbmdpbmUucnVuQW5kV2FpdCgpCgoJCWNvbnRpbnVlCgoKCgoKCSNTZW5kaW5nIHRoZSBSZXF1ZXN0IHRvIENvbXB1dGF0aW9uYWwgU2VydmljZQoKCWFwcF9pZCA9ICJSNUs1RzYtUVdRNVJUMlZMQSIKCgljbGllbnQgPSB3b2xmcmFtYWxwaGEuQ2xpZW50KGFwcF9pZCkKCgoKCXJhdGUgPSBlbmdpbmUuZ2V0UHJvcGVydHkoJ3JhdGUnKSAgICAgICAgICAgICAgICAgICAgICAgICAgIAoKCWVuZ2luZS5zZXRQcm9wZXJ0eSgncmF0ZScsIDE2MCkgICAgIAoKCgoJcmVzID0gY2xpZW50LnF1ZXJ5KGlucHQpCgoJdHJ5OgoKCgoJCXRyeToKCgkJCWFuc3dlciA9IG5leHQocmVzLnJlc3VsdHMpLnRleHQKCgkJCQoKCQkJcHJpbnQoIllvdSBzYWlkOiBcblx0IitpbnB0KyJcblxuIikKCgkJCQoKCQkKCgkJZXhjZXB0OgoKCQkJcHJpbnQoIiIpCgoKCgkJZW5naW5lLnNheShhbnN3ZXIpCgoJCXByaW50KGFuc3dlcikKCgkJZW5naW5lLnJ1bkFuZFdhaXQoKQoKCWV4Y2VwdDoKCgkJZW5naW5lLnNheSgiSSdtIGFmcmFpZCBhbiBFcnJvciBvY2N1cmVkLiIpCgoJCXByaW50KCJJJ20gYWZyYWlkLCBhbiBFcnJvciBvY2N1cmVkLlx0XHQ6LyIpCgoJCWVuZ2luZS5ydW5BbmRXYWl0KCkKCgoKCXRpbWUuc2xlZXAoMik="))