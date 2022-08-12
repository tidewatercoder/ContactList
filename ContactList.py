### Contact list with a simplegui. Names, address, email, and phone numbers can be added
# into there own separate inputs.


import PySimpleGUI as sg
import pickle
import time
import os

class Contact():
    def __init__(self,name,address,phone,email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

def delistm(): ### Allows the user to delete contacts that are no longer desired.
    delist = []
    with open('contactlist.pickle', 'rb') as g:
        contactlist = pickle.load(g)
    ### Pickle file is opened again to make sure all current information is up to date.
    for i in contactlist:
        delist.append(i.name)
    layout = [[sg.Combo(delist,key="_DELETE_"),sg.Button("Delete")]]
    window = sg.Window('Data Purge',layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "Delete":
            x = values["_DELETE_"]
            for i in contactlist:
                if i.name == x:
                    contactlist.remove(i)
            ### The user chooses the name that is associated with the contact and then the code refers the name
                # to the actual contact object and deletes the entire object.
                else:
                    pass
            with open('contactlist.pickle','wb') as g:
                pickle.dump(contactlist,g,protocol=pickle.HIGHEST_PROTOCOL)
            ### The updated contact list is then dumped to update the pickle file.
            window.close()
            delistm()

def FindMe(): ## Creates a separate window for the find and findall function.
    # If you wish for the find functions to be on the main window you can tag and untag certain parts of the code.
    layout = [[sg.Input(key='_FIND_')],
              [sg.Button("Find"),sg.Button("FindAll")]]
    window = sg.Window("Find Me",layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == 'Find':
            while True:
                x = values['_FIND_']
                if x == '': ### If the find button is pressed without a value, it will pull all the contacts
                    # from the file and creates a separate popup for each contact.
                    # This part of the code helps prevent that.
                    break
                with open('contactlist.pickle', 'rb') as g:
                    contactlist = pickle.load(g)
                ### The code opens the pickle file to check for any newly submitted contacts that might match the value
                for i in contactlist:
                    if x == i.name:
                        sg.Popup('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
                                '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
                    elif x == i.address:
                        sg.Popup('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
                                '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
                    elif x == i.phone:
                        sg.Popup('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
                                '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
                    elif x == i.email:
                        sg.Popup('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
                                '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
                break
        ### The code will search through the all the data for a specific match, once found
        # a popup message will display all of the information pertaining to the specific value
        elif event == 'FindAll':
            Findallist = []
            ### Finds all data that has something in common with the given value
            # i.e. gmail will find all of gmail, john will find all names that have john in it 'johnny,john,johnathon'.
            while True:
                y = values['_FIND_']
                if y == '': ### Pressing FindAll with no values will return with all addresses appearing. y == '' prevents that.
                    break
                with open('contactlist.pickle', 'rb') as g:
                    contactlist = pickle.load(g)
                for i in contactlist:
                    if y in i.name:
                        x = ('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
                                '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
                        Findallist.append(x)
                    elif y in i.address:
                        x = ('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
                                '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
                        Findallist.append(x)
                    elif y in i.phone:
                        x = ('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
                                '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
                        Findallist.append(x)
                    elif y in i.email:
                        x = ('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
                                '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
                        Findallist.append(x)
                xg = ''
                break
            window.close()
            return Findallist
        ### Findall will take the found data return it to the mkcontact() and then
        # the window will be updated with the findall data



def mkcontact():
    contactlist = []  ### Holds all the contacts that have been made and loaded into the program.
    xg = ''
    viewlist = [] ### After the contacts have been called and assigned their name, address, email,phone.
    # The information is stored here temporarily before being added to the gui window.
    sorty = 0  ### When the sort button is pressed for the first time, sorty will be assigned 1 and it will sort
    # the data by name alphabetically, the second time the sort button is presssed it will be assigned 2 and
    # will reverse sort by name alphabetically, and after it sorts in reverse it is assigned 0 and
    # starts the pattern over again

    # subframe = [[sg.Button("Find"),sg.Button("FindAll")],[sg.Input(key='_FIND_',do_not_clear=False)]]
    # frame2 = [[sg.Frame('',subframe)],
    #           [sg.Multiline(xg,key='_MULTI_',size=(70,30))]]
    ### if you wish for the find buttons and input to be on the main screen
    # 1. untag the above subframe and frame2
    # 2. tag the frame2 below
    # 3. Go down to event == 'Submit' and untag values.pop[_FIND_']
    # 4. If you scroll down, you will eventually find 2 event == 'Find', tag the first one and then untag the second one.
    # 5. Go down to event == 'FindAll' and untag it
    frame2 = [[sg.Multiline(xg, key='_MULTI_', size=(70, 30))]]
    frame = [[sg.Text("First      "),sg.Input(key='_NAME_',size=(20,20),do_not_clear=False)],
             [sg.Text("Address "),sg.Input(key='_ADD_',size=(20,20),do_not_clear=False)],
             [sg.Text('Phone   '),sg.Input(key='_PHONE_',size=(20,20),do_not_clear=False)],
             [sg.Text('Email    '),sg.Input(key='_EMAIL_',size=(20,20),do_not_clear=False)],
             [sg.Button("Submit")]]

    layout = [[sg.MenubarCustom([['Edit',['Load','Delete','Sort','Purge']],['View',['Find']]])],
              [sg.Column(frame),sg.VerticalSeparator(),sg.Column(frame2)]]

    window = sg.Window("Contacts",layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == 'Submit':
            values.pop('_MULTI_')
            # values.pop("_FIND_")
            while True:
                direct = os.listdir()
                if 'contactlist.pickle' in direct:
                    with open('contactlist.pickle','rb') as g:
                        contactlist = pickle.load(g)
                    if contactlist == "":
                        contactlist = []
                na,ad,ph,em = values ### The keys Name, address,phone, and email are divided up between 4
                # different variables.
                na = values[na]
                ad = values[ad]
                ph = values[ph]
                em = values[em] ### Each key is then passed back into the variable values to retrieve the key
                # assigned value, which are then assigned to a variable
                na = Contact(na,ad,ph,em) ### Combines all the given information into an object (contact)
                contactlist.append(na)
                with open('contactlist.pickle','wb') as g:
                    pickle.dump(contactlist,g,protocol=pickle.HIGHEST_PROTOCOL)
                ## Pickle is used because pickle files can save lists and objects, without turning them into a string.
                ## Thus keeping the integrity of the object (contact) whole.
                fullinfo = ('Name       '+na.name+'\n'+'Address    '+na.address+'\n'+'Phone   '
                '    '+na.phone+'\n'+'Email        '+na.email+'\n'+'\n')
                xg = ''
                viewlist.append(fullinfo)
                for i in viewlist:
                    xg += i
                window.find_element("_MULTI_").Update(xg)
                print(viewlist)
                break
        elif event == "Load":
            viewlist *= 0
            with open('contactlist.pickle', 'rb') as g:
                contactlist = pickle.load(g)
            for i in contactlist:
                x = ('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
                                '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
                viewlist.append(x)
            xg = ''
            for i in viewlist:
                xg += i
            window.find_element("_MULTI_").Update('')
            window.find_element("_MULTI_").Update(xg)
        elif event == 'Delete':
            delistm()
        elif event == 'Sort':
            viewlist *= 0
            sorty += 1
            for i in contactlist:
                x = ('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
                                '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
                viewlist.append(x)
            xg = ''
            if sorty == 1:
                viewlist.sort()
                for i in viewlist:
                    xg += i
            elif sorty == 2:
                viewlist.sort(reverse=True)
                for i in viewlist:
                    xg += i
                sorty = 0
            ### Sorts the data both alphabetically by name and reverse alphabetically by name.
            window.find_element("_MULTI_").Update(xg)
        elif event == "Purge":
            x = sg.popup_yes_no('This will Delete all contacts!\nAre you sure you want to purge?')
            if x == "Yes":
                contactlist *= 0
                with open('contactlist.pickle','wb') as g:
                    pickle.dump('',g,protocol=pickle.HIGHEST_PROTOCOL)
                window.find_element("_MULTI_").Update('')
            else:
                pass
        elif event == 'Find':
            while True:
                x = FindMe()
                if x == None:
                    break
                elif x != []:
                    xg = ''
                    for i in x:
                        xg += i
                    window.find_element("_MULTI_").Update(xg)

        # elif event == "Find":
        #     ## Will find exactly what you type john == john and nothing else, so john != john@email.com,
        #     while True:
        #         x = values["_FIND_"]
        #         if x == '': ### If the find button is pressed without a value, it will pull all the contacts
        #             # from the file and creates a separate popup for each contact.
        #             # This part of the code helps prevent that.
        #             break
        #         with open('contactlist.pickle', 'rb') as g:
        #             contactlist = pickle.load(g)
        #         ### The code opens the pickle file to check for any newly submitted contacts that might match the value
        #         for i in contactlist:
        #             if x == i.name:
        #                 sg.Popup('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
        #                         '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
        #             elif x == i.address:
        #                 sg.Popup('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
        #                         '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
        #             elif x == i.phone:
        #                 sg.Popup('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
        #                         '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
        #             elif x == i.email:
        #                 sg.Popup('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
        #                         '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
        #         break
        #     ## The code will search through the all the data for a specific match, once found
        #     # a popup message will display all of the information pertaining to the specific value
        # elif event == 'FindAll':
        #     Findallist = []
        #     ### Finds all data that has something in common with the given value
        #     # i.e. gmail will find all of gmail, john will find all names that have john in it 'johnny,john,johnathon'.
        #     while True:
        #         y = values['_FIND_']
        #         if y == '': ### Pressing FindAll with no values will return with all addresses appearing. y == '' prevents that.
        #             break
        #         with open('contactlist.pickle', 'rb') as g:
        #             contactlist = pickle.load(g)
        #         for i in contactlist:
        #             if y in i.name:
        #                 x = ('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
        #                         '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
        #                 Findallist.append(x)
        #             elif y in i.address:
        #                 x = ('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
        #                         '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
        #                 Findallist.append(x)
        #             elif y in i.phone:
        #                 x = ('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
        #                         '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
        #                 Findallist.append(x)
        #             elif y in i.email:
        #                 x = ('Name       '+i.name+'\n'+'Address    '+i.address+'\n'+'Phone   '
        #                         '    '+i.phone+'\n'+'Email        '+i.email+'\n'+'\n')
        #                 Findallist.append(x)
        #         ### The code will look through all the data to find a match, if a match is found it will be added to
        #         # the Findallist list
        #         xg = ''
        #         for i in Findallist: ### Grabs the information from the list and puts them into a string
        #             # to read the information easier
        #             xg += i
        #         window.find_element("_MULTI_").Update(xg)  ### Updates the MultiLine box with sorted data.
        #         break

if __name__ == '__main__':
    mkcontact()

