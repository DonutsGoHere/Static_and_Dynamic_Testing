### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# 
#  line 23 should have '==' instead of the '='
#  line 25 should have a colon ':' after 'else'
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   


# start of line 34 below should start as 'def' NOT 'dif'
# 'card' line 36 below should be 'card1'
# after line 34 the rest of the function needs indented
# 'card1' and 'card2' on line 34 need ',' between them
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  
# method is not indented correctly needs to be within class 'CardGame' 
# 'total' line 45 should have '= 0' after it
# 'return' is indented too mech and need to be inline with 'for' line 46
# 'total' line 48 need to be turned into a new string object 'str()'
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
