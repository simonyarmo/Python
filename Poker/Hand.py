# File: Hand.py
# Student: Simon Yarmowich
# UT EID: Sy22637
# Course Name: CS303E
# Unique Number: XXXXX
# 
# Date Created: 11/6/2023
# Description of Program: The program can create a deck of cards and deals out five cards to a player. The program then can evaluate your hand and can tell you what hand in poker you have. 
""" This file includes a class Hand which implements a hand of five playing
    cards, where cards are defined in the Card class.   

    The Hand class defines the following methods:

    Hand( source, fromDeck ):  creates a new hand object of 5 Cards. This happens
         in one of two ways depending on the value of fromDeck: 
         (1) if fromDeck is True, deal 5 cards from an existing deck
             passed as source, 
         (2) if fromDeck is not True, create the cards from a list of 5 card 
             specifiers passed as source, e.g., ("2S", "9S", "TC", "AH", "4D") 
             will create a hand containing the 2 of Spades, 9 of Spades, 10 of Clubs, 
             Ace of Hearts, and 4 of Diamonds.  Generating a single card from a 
             spec is implemented in the Card class.  You need to check that this
             list is legal (contains exactly 5 legal card specifiers, all distinct).
    h.__str__(): generate the print representation of Hand h, using the
         str function on each of the individual Cards it contains (see the Deck
         class for a model for this);
    h.getCard( i ): recall that h is a hand of 5 Cards.  This provides a 
         way of getting the ith card from the hand, for example, to iterate 
         through the hand in a loop. 

    This file also contains a number of other functions (outside the class), mainly
    to allow evaluating a hand in the sense of playing Poker.  You can have as many
    functions as you need, but you must have the function evaluateHand( hand ). 
    Given a hand, it prints the hand and then the "evaluation" of the hand in 
    the sense of a Poker hand.  This is described in detail in the assignment description.   

"""

################################################################################
#                                                                              #
#                                 Hand Class                                   #
#                                                                              #
################################################################################

# I don't need to import Card, since Deck already does.
from Deck import *

def isLegalCardList( l ):
    """ Check that list l contains 5 legal card specifiers, 
        all distinct. You can assume that it's a list. """
    size = len(l)
    for x in range(size-1):
        if(x+1 == size-1):
            return True
        if(l[x]==l[x+1]):
            return False
    pass  

class Hand:

    def __init__(self, source, fromDeck = True):
        """ A hand is simply a list of 5 cards, dealt from the deck
            or given as a list of five card specifiers.  If fromDeck
            is True, expect to deal from a deck passed as source. 
            If False, expect source to be a list of five Card specifiers.
            Create the hand from the specified cards.
        """
        self.fromDeck =fromDeck
        if fromDeck:
            if ( len(source) < 5 ):
                print ( "Not enough cards left!" )
                return None
            self.__cards = []
            for i in range(5):
                card = source.deal()              # deal next card
                self.__cards.append(card)         # append it to the hand
        elif not isLegalCardList( source ):
            print("Illegal card list provided.")
        else:
            if(isLegalCardList(source)):
                self.__cards=source
            else:
                print("Illegal card list provided")
            pass

    def __str__(self):
        """ Generates the print image of the Hand. """
        pass

    def getCard( self, i ):
        if 0<= i <=4:
            return self.__cards[i]
        else:
            return "Not valid"
        pass
    def getFromDeck(self):
        return self.fromDeck
            
################################################################################
#                                                                              #
#                                Evaluate Hand                                 #
#                                                                              #
################################################################################

def processHand( hand ):
    """ Given a poker hand, create and return two lists which
        record the ranks and suits in the hand. """
    
    myRanks = [0]*13
    mySuits = [0]*4
    for x in range(0,5):
        card = hand.getCard(x)
        
        
        if hand.getFromDeck():
            print(card)
            rank = card.getRank()
            suit = card.getSuit()
        else:
            newCard = Card(card)
            print(newCard)
            
            rank = card[0].upper()
            suit = card[1].upper()
        
        if rank =='2':
            myRanks[0]+=1
        elif rank =='3':
            myRanks[1]+=1
        elif rank =='4':
            myRanks[2]+=1
        elif rank=='5':
            myRanks[3]+=1
        elif rank =='6':
            myRanks[4]+=1
        elif rank =='7':
            myRanks[5]+=1
        elif rank =='8':
            myRanks[6]+=1
        elif rank =='9':
            myRanks[7]+=1
        elif rank =="T":
            myRanks[8]+=1
        elif rank =="J":
            myRanks[9]+=1
        elif rank =="Q":
            myRanks[10]+=1
        elif rank =="K":
            myRanks[11]+=1
        elif rank =="A":
            myRanks[12]+=1
        if suit =="S":
            mySuits[0]+=1
        elif suit =="D":
            mySuits[1]+=1
        elif suit =="H":
            mySuits[2]+=1
        elif suit =="C":
            mySuits[3]+=1
    return myRanks, mySuits
    

# You'll need to define all of the auxiliary functions called by
# evaluateHand.  Notice that these auxiliary functions don't all
# need both myRanks and mySuits, but I decided to pass them both
# just to make the interface more uniform.  You can change that 
# if you want to.

def hasPair( myRanks, mySuits ):
    for x in myRanks:
        if x ==2:
            return True
    return False
    

def hasTwoPair( myRanks, mySuits ):
    count =0
    for x in myRanks:
        if x ==2:
            count +=1
    if count ==2:
        return True
    else:
        return False

def hasThreeOfAKind( myRanks, mySuits ):
    for x in myRanks:
        if x ==3:
            return True
    return False
    pass

def hasStraight( myRanks, mySuits ):
    straight =0
    count =0
    for x in myRanks:
        count +=1
        if x ==1:
            straight +=1
        else:
            if straight>0:
                straight -=1
        if straight==5:
            return True
        if count == 4 and straight == 4 and myRanks[12] ==1:
            return True
    return False

def hasFlush( myRanks, mySuits ):
    for x in mySuits:
        if x ==5:
            return True
    return False

def hasFourOfAKind( myRanks, mySuits ):
    for x in myRanks:
        if x ==4:
            return True
    return False

def hasFullHouse( myRanks, mySuits ):
    three =0
    two =0
    for x in myRanks:
        if x ==3:
            three =1
        if x == 2:
            two =1
    if three ==1 and two ==1:
        return True
    else:
        return False
    

def hasStraightFlush( myRanks, mySuits ):
    if(hasFlush(myRanks, mySuits) and hasStraight(myRanks, mySuits) and myRanks[12]==0):
        return True
    return False

def hasRoyalFlush( myRanks, mySuits ):
    if(hasFlush(myRanks, mySuits) and hasStraight(myRanks, mySuits) and myRanks[12]==1):
        return True
    return False

    

# Add other recognizers here; evaluateHand tells you which ones you
# need.  I suggest doing them in "reverse order" so you define the 
# lowest hands first. Hopefully, you'll see why as you code them!

def evaluateHand( hand ):
    myRanks, mySuits = processHand( hand )
    if hasRoyalFlush( myRanks, mySuits ):
        print( "\nRoyal Flush" )
    elif hasStraightFlush( myRanks, mySuits ):
        print( "\nStraight Flush" )
    elif hasFourOfAKind( myRanks, mySuits ):
        print( "\nFour of a kind" )
    elif hasFullHouse( myRanks, mySuits ):
        print( "\nFull House" )
    elif hasFlush( myRanks, mySuits ):
        print( "\nFlush" )
    elif hasStraight( myRanks, mySuits ):
        print( "\nStraight" )
    elif hasThreeOfAKind( myRanks, mySuits ):
        print( "\nThree of a kind" )
    elif hasTwoPair( myRanks, mySuits ):
        print( "\nTwo pair" )
    elif hasPair( myRanks, mySuits ):
        print( "\nPair" )
    else:
        print( "\nNothing" )

# This is some test code.  You can modify this or write your
# own.  You certainly should test additional hands. You can run 
# this in interactive mode with:
# 
# from Hand import *
# TestCode()
#
# You can also run this in batch mode by uncommenting the call to:
# TestCode()
#
# and running:
# 
# python3 Hand.py              # or whatever the python command is
#                              # is on your system. 

def TestCode():
    print("\nGenerating and printing deck")
    d = Deck()
    print(d)
    print("\nShuffling deck and printing deck")
    d.shuffle()
    print(d)

    print("\nGenerating hand from deck")
    h = Hand(d, True)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["7S", "8S", "6S", "9S", "5S"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["as", "ad", "ah", "ac", "2d"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["AS", "2S", "3C", "4H", "5D"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["2s", "9S", "tc", "AH", "4d"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

TestCode()
