from sys import exit
from random import randint
from hippodict import responses 
import Levenshtein 

def geta_response(response_list, tolerance = 2, error_msg = "That doesn't make much sense. Try typing that in again."): 
    while True:
        next = raw_input("> ")
        for response in response_list:
            if Levenshtein.distance(next.lower(), response) <= tolerance:
                return response
        print error_msg

def go(directions):
    response = geta_response(directions.keys(), 2)
    destination = directions[response]
    destination()

def dead():
    death = ["Have a good one.", "Aww, why not? Ok, maybe you'll want to play another day.", 
    "The hippocampus will miss you. I bet you'll miss it.", "You missed out on a damn good game.", 
    "You just missed out on such a good adventure. Bummer.", "Ok, you missed out. But no problem.", 
    "Aww, too bad. Guess you don't *really* want to explore the hippocampus.", "Maybe another time!"]
    print death[randint(0, len(death)-1)]
    exit(1)
 
def entorhinal_cortex():
    print responses['Layer2and3']

    response = geta_response(["2", "3"], 0 , responses['TryAgain'])
    how_much = int(response)

    if how_much == 2:
        print "Welcome! Now you have the option of exploring the dentate gyrus or the hippocampal region CA3. Enter your choice."

        go({"dentate gyrus": dentate_gyrus,"hippocampal region ca3": hippocampal_region_CA3})
        
    elif how_much == 3:
        print "Sweet pick. Since the entorhinal cortex has 2 major projections, you have the option of exploring the hippocampal region CA1 or the subiculum. Enter your choice."

        go({"hippocampal region ca1": hippocampal_region_CA1,"subiculum": subiculum})
            
def dentate_gyrus():
    print responses['DentateGyrus']
    response = geta_response(["yes", "no"], 1 , responses['TryAgain'])
    
    if response == "yes":
        print """The dentate gyrus primarily consists of granule cells, interneurons and pyramidal cells.""" """The dentate gyrus' main projection is to the CA3. So off to there you go!"""
        hippocampal_region_CA3()
    elif response == "no":
        dead()

def hippocampal_region_CA3():
    print responses['HippocampalRegionCA3']
    response = geta_response(["yes", "no"], 1, responses['TryAgain'])
    
    if response == "yes":
        print "The CA3 plays a role in the encoding of new spatial information within short-term memory with a duration of seconds and minutes.""" """The CA3's main projection is to the CA1. So that's where you're headed to next."""
        hippocampal_region_CA1()
    elif response == "no":
        dead()
        
def subiculum():
    print responses['Subiculum']
    response = geta_response(["stay", "leave"], 1, responses['TryAgain'])
    
    go({"stay": dead(), "leave": entorhinal_cortex_2()})

def hippocampal_region_CA1():
    print responses['HippocampalRegionCA1']
    response = geta_response(["subiculum", "entorhinal cortex"], 1, responses['TryAgain'])

    go({"subiculum": subiculum(), "entorhinal cortex": entorhinal_cortex_2()})
    
def entorhinal_cortex_2():
    print responses['EntorhinalCortex2']
    response = geta_response(["yes"], 1, responses['TryAgain'])
    
    if response == "yes":
        entorhinal_cortex()
    else: 
        print "Thanks for playing."

def start():
    print responses['StartHere']     
    response = geta_response(["ready"], 1, responses['TryAgain'])

    go({"ready": entorhinal_cortex()})

start()
