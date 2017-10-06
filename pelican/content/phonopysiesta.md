Title: Phononpy siesta interface
Date: 2015-12-5 15:20
Category: Materials science

Recently I gave a small contribution to the fantastic phonopy package:
an interface to use the forces calculates with the Siesta code.

This interface allows the user to generate a set of supercells with some
atomic displacements.
After executing Siesta to obtain the force constants, 
the interface is able to read them onto phonopy.
Using phonopy instead of the vibra package provided with
Siesta might save you some computational time. 
This is because the vibra package does not use symmetries to
reduce the number of displaced supercells while the phonopy package does.

You can then visualize the phonons in the phononwebsite:
http://henriquemiranda.github.io/phononwebsite/

You can obtain the phonopy package from: 
<http://phonopy.sourceforge.net>

Siesta website:  
<http://departments.icmab.es/leem/siesta/>

Check it out and tell me how it works for you!
