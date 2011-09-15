from traits.api import Instance

from .toggle_control import ToggleControl, IToggleControlImpl


class IRadioButtonImpl(IToggleControlImpl):
    pass


class RadioButton(ToggleControl):
    """ A radio button widget derived from IToggleElement 
    
    Use a radio button to toggle the value of a boolean field. For a 
    group of radio buttons with the same widget parent, only one radio 
    button may be selected at a time. This makes groups of radio buttons 
    useful for selecting amongst a discrete set of values. For multiple 
    groups of independent radio buttons, place them in their own Panel.

    See Also
    --------
    IToggleElement
    
    """
    #---------------------------------------------------------------------------
    # Overridden parent class traits
    #---------------------------------------------------------------------------
    toolkit_impl = Instance(IRadioButtonImpl)
