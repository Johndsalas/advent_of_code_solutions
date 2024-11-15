''' Contains helper function for reading txt files for puzzle input'''

def get_text_as_list(text, output = list):
    '''opens text file
       returns a list of strings 
       where each string a line of text'''
    
    # open input file
    with open(text, 'r') as reader:

        # return text as string or as list of lines
        if output == 'string':

            return reader.readlines()[0].replace('\n', '')

        if output == 'list':

            #readlines input lines into a list
            return [line.rstrip() for line in reader.readlines()]