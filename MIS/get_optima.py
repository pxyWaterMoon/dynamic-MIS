import matplotlib.pyplot as plt
from ortools.linear_solver import pywraplp
from tqdm import tqdm
import sys
import csv
import recursive_tree
import model
import networkx as nx
import numpy as np
import time
from utils import load_benchmark_data

from heuristic_optimal_solvers import local_search
from heuristic_optimal_solvers import solve_mis_ilp


def test_dataset(dataset_name, dataset_path, mode):

    idx0,idx1 = get_indeces_dataset(dataset_name)
    
    list_G = load_benchmark_data(dataset_name, idxs=(idx0, idx1),dataset_path=dataset_path)

    # gur_solver = pywraplp.Solver.CreateSolver('gurobi')

    mis_opt = []

    print("Start solving")
    
    pbar = tqdm(enumerate(list_G))
    for i, G in pbar:
        pbar.set_description(f'|V|={G.number_of_nodes()}, |E|={G.number_of_edges()}')
        
        # MIS FOR OR AND GUROBI SEARCH (FIX TIME)
        or_1h, _ = solve_mis_ilp(G, time_limit_milliseconds=3600000, mode=mode)
        mis_opt.append(or_1h)
    
    return mis_opt


def get_indeces_dataset(dataset_name):
    if dataset_name == 'COLLAB':
        idx0 = 4000
        idx1 = 5000
    elif dataset_name == 'TWITTER_SNAP':
        idx0 = 778
        idx1 = 973
    elif dataset_name == 'RB':
        idx0 = 1600
        idx1 = 2000
    elif dataset_name == 'SPECIAL':
        idx0 = 160
        idx1 = 200
    else:
        sys.exit('The provided dataset_name is not allowed')

    return idx0,idx1


if __name__ == '__main__':
    dataset_name = 'COLLAB'
    mode = 'SCIP'
    opt_list = test_dataset(dataset_name, 'MIS/dataset_buffer', mode)
    # store the opt list into csv file
    with open('MIS/dataset_scip/'+dataset_name+'_'+mode+'.csv', mode='w') as f:
        writer = csv.writer(f)
        for opt in opt_list:
            writer.writerow([opt])