# Standard Python libraries
from __future__ import (absolute_import, print_function,
                        division, unicode_literals)

# https://github.com/usnistgov/DataModelDict
from DataModelDict import DataModelDict as DM

__all__ = ['stackingfaultpart1']

def stackingfaultpart1(input_dict, **kwargs):
    """
    Interprets calculation parameters associated with a stacking-fault record.
    This function should be called before iprPy.input.systemmanupulate.
    
    The input_dict keys used by this function (which can be renamed using the
    function's keyword arguments):
    
    - **'stackingfault_file'** a stacking-fault record to load.
    - **'stackingfault_content'** alternate file or content to load instead of
      specified stackingfault_file.  This is used by prepare functions.
    - **'stackingfault_model'** the open DataModelDict of file/content.
    - **'x_axis, y_axis, z_axis'** the orientation axes.  This function only
      reads in values from the stackingfault_model.
    - **'atomshift'** the atomic shift to apply to all atoms.  This function
      only reads in values from the stackingfault_model.
    - **'stackingfault_cutboxvector'** the cutboxvector parameter for the
      stackingfault model.  Default value is 'c' if neither
      stackingfault_model nor stackingfault_cutboxvector are given.
    - **'stackingfault_faultpos'** the relative position within a unit cell
      where the stackingfault is to be placed.
    - **'stackingfault_shiftvector1'** one of the two fault shifting vectors
      as a crystallographic vector.
    - **'stackingfault_shiftvector2'** one of the two fault shifting vectors
      as a crystallographic vector.
       
    Parameters
    ----------
    input_dict : dict
        Dictionary containing input parameter key-value pairs.
    stackingfault_file : str
        Replacement parameter key name for 'stackingfault_file'.
    stackingfault_content : str
        Replacement parameter key name for 'stackingfault_content'.
    stackingfault_model : str
        Replacement parameter key name for 'stackingfault_model'.
    x_axis : str
        Replacement parameter key name for 'x_axis'.
    y_axis : str
        Replacement parameter key name for 'y_axis'.
    z_axis : str
        Replacement parameter key name for 'z_axis'.
    atomshift : str
        Replacement parameter key name for 'atomshift'.
    stackingfault_cutboxvector : str
        Replacement parameter key name for 'stackingfault_cutboxvector'.
    stackingfault_faultpos : str
        Replacement parameter key name for 'stackingfault_faultpos'.
    stackingfault_shiftvector1 : str
        Replacement parameter key name for 'stackingfault_shiftvector1'.
    stackingfault_shiftvector2 : str
        Replacement parameter key name for 'stackingfault_shiftvector2'.
    """
    
    # Set default keynames
    keynames = ['stackingfault_file', 'stackingfault_content',
                'stackingfault_model', 'x_axis', 'y_axis', 'z_axis',
                'atomshift', 'stackingfault_cutboxvector',
                'stackingfault_faultpos', 'stackingfault_shiftvector1',
                'stackingfault_shiftvector2']
    for keyname in keynames:
        kwargs[keyname] = kwargs.get(keyname, keyname)
    
    # Extract input values and assign default values
    stackingfault_file = input_dict.get(kwargs['stackingfault_file'], None)
    stackingfault_content = input_dict.get(kwargs['stackingfault_content'],
                                           None)
    
    # Replace defect model with defect content if given
    if stackingfault_content is not None:
        stackingfault_file = stackingfault_content
    
    # If defect model is given
    if stackingfault_file is not None:
        
        # Verify competing parameters are not defined
        for key in ('atomshift', 'x_axis', 'y_axis', 'z_axis',
                    'stackingfault_cutboxvector', 'stackingfault_faultpos',
                    'stackingfault_shiftvector1',
                    'stackingfault_shiftvector2'):
            assert kwargs[key] not in input_dict, (kwargs[key] + ' and '
                                                   + kwargs['dislocation_model']
                                                   + ' cannot both be supplied')
        
        # Load defect model
        stackingfault_model = DM(stackingfault_file).find('stacking-fault')
            
        # Extract parameter values from defect model
        input_dict[kwargs['x_axis']] = stackingfault_model['calculation-parameter']['x_axis']
        input_dict[kwargs['y_axis']] = stackingfault_model['calculation-parameter']['y_axis']
        input_dict[kwargs['z_axis']] = stackingfault_model['calculation-parameter']['z_axis']
        input_dict[kwargs['atomshift']] = stackingfault_model['calculation-parameter']['atomshift']
        input_dict[kwargs['stackingfault_cutboxvector']] = stackingfault_model['calculation-parameter']['cutboxvector']
        input_dict[kwargs['stackingfault_faultpos']] = float(stackingfault_model['calculation-parameter']['faultpos'])
        input_dict[kwargs['stackingfault_shiftvector1']] = stackingfault_model['calculation-parameter']['shiftvector1']
        input_dict[kwargs['stackingfault_shiftvector2']] = stackingfault_model['calculation-parameter']['shiftvector2']
    
    # Set default parameter values if defect model not given
    else:
        input_dict[kwargs['stackingfault_cutboxvector']] = input_dict.get(kwargs['stackingfault_cutboxvector'], 'c')
        input_dict[kwargs['stackingfault_faultpos']] = float(input_dict.get(kwargs['stackingfault_faultpos'], 0.5))
        assert input_dict[kwargs['stackingfault_cutboxvector']] in ['a', 'b', 'c'], 'invalid stackingfault_cutboxvector'
        
    # Save processed terms
    input_dict[kwargs['stackingfault_model']] = stackingfault_model