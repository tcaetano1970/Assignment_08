#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Tcaetano, 20211205, began adding code 
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
objFile = None  # file object
strID = '' 

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    CD_id = int()
    CD_title = ''
    CD_artist = ''
    
    # TODO Add Code to the CD class
    
    ''' CONSTRUCTOR '''
    
    def __init__(self, pos, tit, art):
        
        ''' ATTRIBUTES '''    
        
        self.__CD_id = pos
        self.__CD_title = tit
        self.__CD_artist = art
    

    def CD_id(self):
        return self.__CD_id
    
    @CD_id.setter
    def CD_id(self, pos):
        if str(pos).isnumeric():
            self.__CD_id
        else:
            raise Exception('The ID must be a number')
            
    #Define properties for CD_ti
    @property
    def CD_title(self):
        return self.__CD_title
    
    @CD_title.setter
    def CD_title(self, tit):
        if str(tit).isnumeric():
            raise Exception('Title has to be a string') 
        else:
            self.__CD_title = tit
        
    # Define properties for CD_length
    @property 
    def CD_artist(self):
        return self.__CD_artist
    
    @CD_artist.setter 
    def CD_artist(self, art):
        if str(art).isnumeric():
            raise Exception('Artist has to be a string')
        else:
            self.CD_artist = art


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODO Add code to process data from a file - CHECK 
    # TODO Add code to process data to a file - CHECK
    
    @staticmethod
    def object_saver(): 
        objFile = open(strFileName, 'w')
        for row in lstTbl:            
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()

    @staticmethod    
    def delete_CD(intIDDel):
        ''' function to delete CD '''    
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')



# -- PRESENTATION (Input/Output) -- #
class IO:
     """Handling Input / Output"""

     @staticmethod
     def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

     @staticmethod
     def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

     @staticmethod
     def show_inventory(table):
        """Displays current inventory table

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

     @staticmethod
     def user_input():
        '''Added new function input_data() with code from below '''
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, stArtist
    
 
    
 
    # TODO add docstring - CHECK
    # TODO add code to show menu to user - CHECK
    # TODO add code to captures user's choice - CHECK
    # TODO add code to display the current data on screen - CHECK
    # TODO add code to get CD data from user - CHECK
     

# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file - CHECK
    # let user load inventory from file - CHECK
    # let user exit program

