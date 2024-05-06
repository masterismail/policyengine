from abc import ABC, abstractmethod

class Microsimulation(MicrosimulationInterface):
    def __init__(self, country):
        self.sim = get_microsimulation(country)
        
    def calculate(self, variable, map_to=None):
        return self.sim.calculate(variable, map_to)
    
    # Add other methods as proxies...

class IndividualSim(IndividualSimInterface):
    def __init__(self, country):
        self.sim = get_individual_sim(country)
        
    def calculate_outcome(self, household):
        return self.sim.calculate_outcome(household)
    
    # Add other methods as proxies...
