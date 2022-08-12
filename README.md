# ContactList
Contact List made with pysimplegui

When you first run the script you must put in your first contact.
This will create the pickle file that is required in the program.
If you try to do anything before submitting your first contact the code will error out and close the program.

The find and findAll button were given there own separate window, if you wish to put the find and findall button on the main window simply follow these steps
 1. Untag subframe and the first frame2 and then tag the second frame2
 3. Go down to event == 'Submit' and untag values.pop[_FIND_']
 4. If you scroll down, you will eventually find 2 separate event == 'Find', tag the first one and then untag the second one.
 5. Finally to event == 'FindAll' and untag it
