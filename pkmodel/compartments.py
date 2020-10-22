#
#A class for specifying the compartments
#

class Central_Compartment:
    """Pharmokinetic model: specifies the parameters of the central compartment used in
    the model - 
    Parameters
    -------------
    
    compartment: integer, necessary
                defaults to two compartments, but can be set to one.
                
    """
    
    def __init__(self, compartments=2):
        self.compartments = compartments