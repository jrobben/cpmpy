from ..model import *
from ..expressions import *
from ..variables import *

def cnf_to_pysat(constraints, output=None):
    py_cnf = []

    for ci in constraints:
        print("ci",ci)
        formula = []
        # single lit
        if isinstance(ci, Comparison):
            # only of the form 'b == 0'
            if isinstance(ci.args[0], BoolVarImpl) and isinstance(ci.args[1], int) and ci.args[1] == 0:
                formula.append(- (ci.args[0].name + 1))
            else:
                raise Exception("cnf_to_pysat: Comparison '"+ci.name+"' not yet supported")
        elif isinstance(ci, BoolVarImpl):
            formula.append(ci.name + 1)
        elif isinstance(ci, bool) and ci is True:
            # no need to create a clause for constant 'true'
            continue
        elif isinstance(ci, Operator) and ci.name == 'or':
            for lit in ci.args:
                if isinstance(lit, Comparison) and isinstance(lit.args[0], BoolVarImpl) and isinstance(lit.args[1], int) and lit.args[1] == 0:
                    formula.append(-(lit.args[0].name + 1))
                elif isinstance(lit, BoolVarImpl):
                    formula.append(lit.name + 1)
                else:
                    raise Exception(f"lit: {lit}, in '{ci}' not handled")
        else:
            raise Exception(f"ci: '{ci}' not handled")
        py_cnf.append(formula)

    cnf_sets = [set(clause) for clause in py_cnf]
    return cnf_sets

