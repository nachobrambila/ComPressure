# Let's make a quick conversion function for PSI to atoms and vice versa. This can be used later on.
class Convert:
    def __init__(self, psi, atoms):
        psi = float(psi)
        atoms = float(atoms)

    def psi2atoms(psi):
        atoms = psi * 65536.000
        return atoms
    
    def atoms2psi(atoms):
        psi =  atoms / 65536.000
        return psi

# Let's make a function for relating the source, vent, and resulting pressure.
class Component:
    def __init__(self, source, vent):
        self.source = float(source)
        self.vent = float(vent)

    def pressure(source, vent):
        '''
        Equation is only used for standard valves.
        '''
        S = source
        V = vent
        P = S / (S + V)

        return P
    
    def pressure2(source, vent):
        '''
        Equation is general.
        '''
        S = source
        V = vent
        P = (8/V + 1.5) / (8/V + 8/S + 3)

        return P       


class Pipe(Component):
    pass

class Inlet(Component):
    pass

class Valve(Component):
    pass
