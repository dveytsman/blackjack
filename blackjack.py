from art import logo
from random import choice

print(logo)

## Game Play
# 2 cards are dealt to user and computer
# user can see their cards and one of the computers cards
# user is asked if they want another card
    # yes => they are dealt another card
    # no => if computers cards are better
        # computer wins
        #if not and computers cards are below 17, computer gets another card
        # this loops till the computer's card value is 17 or above
        # compare cards and print win or lose
    # if the users card value is below 21
        # user is asked if they want another card
        # loop back to line 8
game_on = True
# Step 1. Ask user if they'd like to play
while game_on:
    play = input("Would you like to play a round of blackjack? y or n\n")
    if play == "y":
        game_on = True
    else:
        game_on = False
        break
    # Step 2. Set up the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # simplified deck
    # Step 3. Deal the cards
    user_cards = [choice(cards) for card in range(2)]
    computer_cards = [choice(cards) for card in range(2)]
    computer_display = [computer_cards[0], "?"]
    # Step 4. Display the users cards and the first computer card
    print(f"your cards are {user_cards}")
    print(f"the computer's cards are {computer_display}")
    # Step 5. Ask user if theyd like another card (this might be a loop)
    can_hit = True
    while can_hit:
        should_hit = input("Would you like another card? y or n\n")
        if should_hit == "y":
            should_hit = True
        else:
            should_hit = False
            can_hit = False
        # add a new card to the users hand
        if should_hit:
            user_cards.append(choice(cards))
        # calculate new total
        users_total = sum(user_cards)
        if users_total > 21 and 11 in user_cards:
            ace = user_cards.index(11)
            user_cards[ace] -= 10
            users_total = sum(user_cards)
        # display new hands
        print(f"your cards are {user_cards} with a value of {users_total}")
        print(f"computers cards are {computer_display}")
        if users_total > 21 and 11 not in user_cards:
            print("bust")
            can_hit = False

        ## after either bust or user doesn't want to hit
        # computer's turn
        # if computers hand is less than 17 computer hits
    computers_total = sum(computer_cards)
    # ## following for testing
    # user_cards = [2, 3]
    # computer_cards = [2, 11]
    # users_total = sum(user_cards)
    # user_busted = False
    # computer_display = [2, "?"]
    # computers_total = sum(computer_cards)
    # print(f"your cards are {user_cards}")
    # print(f"the computer's cards are {computer_display}")
    # ## previous for testing
    while computers_total < 17:
        computer_cards.append(choice(cards))
        computer_display.append(computer_cards[-1])
        computers_total = sum(computer_cards)
        if computers_total > 21 and 11 in computer_cards:
            ace = computer_cards.index(11)
            computer_cards[ace] -= 10
            if 11 in computer_display:
                ace = computer_display.index(11)
                computer_display[ace] -= 1
        computers_total = sum(computer_cards)

    # at this point the computer is done with its turn
    # show cards
    print(f"your hand is {user_cards} with a total of {users_total}")
    print(f"computer's hand is {computer_cards} with a total of {computers_total}")
    user_busted = users_total > 21
    computer_busted = computers_total > 21
    if (users_total > computers_total and not user_busted) or (computer_busted and not user_busted):
        print("you win")
    elif users_total == computers_total:
        print("Draw")
    elif (users_total < computers_total and not computer_busted) or (user_busted and not computer_busted):
        print("you've lost")