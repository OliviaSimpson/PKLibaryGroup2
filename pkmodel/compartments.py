#
#A class for specifying the compartments
#

class Compartments:
    """Pharmokinetic model: specifies the number of compartments used in
    the model - this is limited to 1 or 2, but can be extended to many more
    quite easily
    
    Parameters
    -------------
    
    compartment: integer, necessary
                defaults to two compartments, but can be set to one.
                
    """
    
    def __init__(self, compartments=2):
        self.compartments = compartments