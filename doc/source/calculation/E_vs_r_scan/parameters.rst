Input script parameters
-----------------------

This is a list of the input parameter names recognized by the
calculation script.

Command lines for LAMMPS and MPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides the external commands for running LAMMPS and MPI.

-  **lammps\_command**: the path to the executable for running LAMMPS on
   your system. Don't include command line options.

-  **mpi\_command**: the path to the MPI executable and any command line
   options to use for calling LAMMPS to run in parallel on your system.
   Default value is None (run LAMMPS as a serial process).

Potential definition and directory containing associated files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides the information associated with an interatomic potential
implemented for LAMMPS.

-  **potential\_file**: the path to the potential\_LAMMPS data model
   used by atomman to generate the proper LAMMPS commands for an
   interatomic potential.

-  **potential\_dir**: the path to the directory containing any
   potential artifacts (eg. eam.alloy setfl files) that are used. If not
   given, then any required files are expected to be in the working
   directory where the calculation is executed.

Initial system configuration to load
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides the information associated with loading an atomic
configuration.

-  **load\_file**: the path to the initial configuration file being read
   in.

-  **load\_style**: the style/format for the load\_file. The style can
   be any file type supported by atomman.load()

-  **load\_options**: a list of key-value pairs for the optional
   style-dependent arguments used by atomman.load().

-  **family**: specifies the configuration family to associate with the
   loaded file. This is typically a crystal structure/prototype
   identifier that helps with linking calculations on the same material
   together. If not given and the load\_style is system\_model, then the
   family will be taken from the file if included. Otherwise, the family
   will be taken as load\_file stripped of path and extension.

-  **symbols**: a space-delimited list of the potential's atom-model
   symbols to associate with the loaded system's atom types. Required if
   load\_file does not contain this information.

-  **box\_parameters**: *Note that this parameter has no influence on
   this calculation.* allows for the specification of new box parameters
   to scale the loaded configuration by. This is useful for running
   calculations based on prototype configurations that do not contain
   material-specific dimensions. Can be given either as a list of three
   or six numbers, with an optional unit of length at the end. If the
   unit of length is not given, the specified length\_unit (below) will
   be used.

-  a b c (unit): for orthogonal boxes.

-  a b c alpha beta gamma (unit): for triclinic boxes. The angles are
   taken in degrees.

System manipulations
~~~~~~~~~~~~~~~~~~~~

Performs simple manipulations on the loaded initial system.

-  **a\_uvw, b\_uvw, c\_uvw**: are crystallographic Miller vectors to
   rotate the system by such that the rotated system's a, b, c box
   vectors correspond to the specified Miller vectors of the loaded
   configuration. Using crystallographic vectors for rotating ensures
   that if the initial configuration is periodic in all three
   directions, the resulting rotated configuration can be as well with
   no boundary incompatibilities. Default values are '1 0 0', '0 1 0',
   and '0 0 1', respectively (i.e. no rotation).

-  **atomshift**: a vector positional shift to apply to all atoms. The
   shift is relative to the size of the system after rotating, but
   before sizemults have been applied. This allows for the same relative
   shift regardless of box\_parameters and sizemults. Default value is
   '0.0 0.0 0.0' (i.e. no shift).

-  **sizemults**: multiplication parameters for making a supercell of
   the loaded system. This may either be a list of three or six integer
   numbers. Default value is '3 3 3'.

-  ma mb mc: multipliers for each box axis. Values can be positive or
   negative indicating the direction relative to the original box's
   origin for shifting/multiplying the system.

-  na pa nb pb nc pc: negative, positive multiplier pairs for each box
   axis. The n terms must be less than or equal to zero, and the p terms
   greater than or equal to zero. This allows for expanding the system
   in both directions relative to the original box's origin.

Units for input/output values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specifies the units for various physical quantities to use when saving
values to the results record file. Also used as the default units for
parameters in this input parameter file.

-  **length\_unit**: defines the unit of length for results, and input
   parameters if not directly specified. Default value is 'angstrom'.

-  **energy\_unit**: defines the unit of energy for results, and input
   parameters if not directly specified. Default value is 'eV'.

-  **pressure\_unit**: defines the unit of pressure for results, and
   input parameters if not directly specified. Default value is 'GPa'.

-  **force\_unit**: defines the unit of pressure for results, and input
   parameters if not directly specified. Default value is 'eV/angstrom'.

Run Parameters
~~~~~~~~~~~~~~

Provides parameters specific to the calculation at hand.

-  **minimum\_r**: specifies the minimum interatomic spacing, r, for the
   scan. Default value is '2.0 angstrom'.

-  **maximum\_r**: specifies the maximum interatomic spacing, r, for the
   scan. Default value is '6.0 angstrom'.

-  **number\_of\_steps\_r**: specifies the number of interatomic spacing
   values, r, to use. Default value is 200.
