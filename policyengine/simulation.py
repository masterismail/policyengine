from policyengine_us import Microsimulation as USMicrosimulation
from policyengine_uk import Microsimulation as UKMicrosimulation
from policyengine_us import IndividualSim as USIndividualSim
from policyengine_uk import IndividualSim as UKIndividualSim

def get_microsimulation(country='us'):
    """Factory function to instantiate a Microsimulation instance for the given country."""
    if country == 'us':
        return USMicrosimulation()
    elif country == 'uk':
        return UKMicrosimulation()
    else:
        raise ValueError(f"Unsupported country: {country}")

def get_individual_sim(country='us'):
    """Factory function to instantiate an IndividualSim instance for the given country."""
    if country == 'us':
        return USIndividualSim()
    elif country == 'uk':
        return UKIndividualSim()
    else:
        raise ValueError(f"Unsupported country: {country}")
