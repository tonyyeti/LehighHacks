# project, Calculate the best portfolio with 50 stocks, 30 period
# Fix Variance
# model

from pyomo.environ import *
import matplotlib.pyplot as plt
from pyomo.opt import *
from TongYe_PS4_1_estimate_mean_with_black import mean_dict
import numpy as np


model = AbstractModel()

model.assets = Set()
model.T = Set(initialize = range(1, 20))
model.max_risk = Param(mutable = True, initialize = .00305)
model.R = Param(model.T, model.assets)

def mean_init(model, j):
    return sum(model.R[i, j] for i in model.T)/len(model.T) 
model.mean = Param(model.assets, initialize = mean_init)

def Q_init(model, i, j):
    return sum((model.R[k, i] - model.mean[i])*(model.R[k, j] - model.mean[j]) for k in model.T)
model.Q = Param(model.assets, model.assets, initialize = Q_init)

model.alloc = Var(model.assets, within=NonNegativeReals)

def risk_bound_rule(model):
    return (
        sum(sum(model.Q[i, j] * model.alloc[i] * model.alloc[j] for i in model.assets)
            for j in model.assets) <= model.max_risk)
model.risk_bound = Constraint(rule=risk_bound_rule)

def tot_mass_rule(model):
    return (sum(model.alloc[j] for j in model.assets) == 1)
model.tot_mass = Constraint(rule=tot_mass_rule)

def objective_rule(model):
    return summation(model.mean, model.alloc)
model.objective = Objective(sense=maximize, rule=objective_rule)

epsilon = .0001

print 'Creating model...'

instance = model.create('project.dat')
opt = SolverFactory("ipopt")
#risk_values = [1]
risk_values = [float(i)/100 for i in range(30, 150)]
returns = []
for risk in risk_values:
    instance.max_risk = risk
    
    print 'Optimizing with maximum risk', risk

    results = opt.solve(instance)
    instance.load(results)

    print 'Optimal purchase amounts:'
    for i in instance.assets:
        if instance.alloc[i].value > epsilon:
            print '%-15s %-3.3f' % (i, instance.alloc[i].value)
        
    print 'Optimal return: %.3f' % (value(instance.objective))
    returns.append(value(instance.objective))
    
plt.plot(risk_values, returns, 'bs')
plt.show()