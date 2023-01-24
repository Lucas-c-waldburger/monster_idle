
master_cell_dict = {
    'c0xr0': {'xy': (0, 0), 'column': 0, 'row': 0},
    'c0xr1': {'xy': (0, 100), 'column': 0, 'row': 1},
    'c0xr2': {'xy': (0, 200), 'column': 0, 'row': 2},
    'c0xr3': {'xy': (0, 300), 'column': 0, 'row': 3},
    'c0xr4': {'xy': (0, 400), 'column': 0, 'row': 4},
    'c0xr5': {'xy': (0, 500), 'column': 0, 'row': 5},
    'c1xr0': {'xy': (100, 0), 'column': 1, 'row': 0},
    'c1xr1': {'xy': (100, 100), 'column': 1, 'row': 1},
    'c1xr2': {'xy': (100, 200), 'column': 1, 'row': 2},
    'c1xr3': {'xy': (100, 300), 'column': 1, 'row': 3},
    'c1xr4': {'xy': (100, 400), 'column': 1, 'row': 4},
    'c1xr5': {'xy': (100, 500), 'column': 1, 'row': 5},
    'c2xr0': {'xy': (200, 0), 'column': 2, 'row': 0},
    'c2xr1': {'xy': (200, 100), 'column': 2, 'row': 1},
    'c2xr2': {'xy': (200, 200), 'column': 2, 'row': 2},
    'c2xr3': {'xy': (200, 300), 'column': 2, 'row': 3},
    'c2xr4': {'xy': (200, 400), 'column': 2, 'row': 4},
    'c2xr5': {'xy': (200, 500), 'column': 2, 'row': 5},
    'c3xr0': {'xy': (300, 0), 'column': 3, 'row': 0},
    'c3xr1': {'xy': (300, 100), 'column': 3, 'row': 1},
    'c3xr2': {'xy': (300, 200), 'column': 3, 'row': 2},
    'c3xr3': {'xy': (300, 300), 'column': 3, 'row': 3},
    'c3xr4': {'xy': (300, 400), 'column': 3, 'row': 4},
    'c3xr5': {'xy': (300, 500), 'column': 3, 'row': 5},
    'c4xr0': {'xy': (400, 0), 'column': 4, 'row': 0},
    'c4xr1': {'xy': (400, 100), 'column': 4, 'row': 1},
    'c4xr2': {'xy': (400, 200), 'column': 4, 'row': 2},
    'c4xr3': {'xy': (400, 300), 'column': 4, 'row': 3},
    'c4xr4': {'xy': (400, 400), 'column': 4, 'row': 4},
    'c4xr5': {'xy': (400, 500), 'column': 4, 'row': 5},
    'c5xr0': {'xy': (500, 0), 'column': 5, 'row': 0},
    'c5xr1': {'xy': (500, 100), 'column': 5, 'row': 1},
    'c5xr2': {'xy': (500, 200), 'column': 5, 'row': 2},
    'c5xr3': {'xy': (500, 300), 'column': 5, 'row': 3},
    'c5xr4': {'xy': (500, 400), 'column': 5, 'row': 4},
    'c5xr5': {'xy': (500, 500), 'column': 5, 'row': 5}
}


master_column_dict = {
    'xy_column_0': {key: (value['xy']) for key, value in master_cell_dict.items() if value['column'] == 0},
    'xy_column_1': {key: (value['xy']) for key, value in master_cell_dict.items() if value['column'] == 1},
    'xy_column_2': {key: (value['xy']) for key, value in master_cell_dict.items() if value['column'] == 2},
    'xy_column_3': {key: (value['xy']) for key, value in master_cell_dict.items() if value['column'] == 3},
    'xy_column_4': {key: (value['xy']) for key, value in master_cell_dict.items() if value['column'] == 4},
    'xy_column_5': {key: (value['xy']) for key, value in master_cell_dict.items() if value['column'] == 5}
}
