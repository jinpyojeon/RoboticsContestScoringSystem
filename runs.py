import registry as r
from initialize_registry import load_registry


def add_run(robot_id, params_d):
    robot = r.get_registry()['ROBOTS'].get_robot(robot_id)
    score = get_score(robot, params_d)
    params_t = convert_to_tuple(params_d, robot_id, score)
    r.get_registry()['RUNS'].record_run(*params_t)


# convert dict values to tuple to prepare to insert to DB
def convert_to_tuple(dic, robot_id, score):
    # convert the dictionary values to tuples, order matters
    l = []

    l.append(dic['level'])
    l.append(dic['run_disqualified'])
    l.append((to_float(dic['seconds_to_put_out_candle_1']) +
              to_float(dic['seconds_to_put_out_candle_2'])) / 2.0)
    # average times by the 2 judges
    l.append(dic['non_air'])
    l.append(dic['furniture'])
    l.append(dic['arbitrary_start'])
    l.append(dic['return_trip'])
    l.append(dic['no_candle_circle'])
    l.append(dic['stopped_within_30'])
    l.append(dic['candle_detected'])
    l.append(to_int(dic['number_of_rooms_searched']))
    l.append(dic['kicked_dog'])
    l.append(to_int(dic['touched_candle']))
    l.append(to_int(dic['wall_contact_cms']))
    l.append(dic['ramp_used'])
    l.append(dic['baby_relocated'])
    l.append(dic['all_candles'])
    l.append(dic['versa_valve_used'])
    l.append(score)
    l.append(robot_id)
    return tuple(l)


# convert string to float
def to_float(input_s):
    if input_s:
        return float(input_s)
    # only true when run is disqualified
    return 0


# convert string to float
def to_int(input_s):
    if input_s:
        return int(input_s)
    # only true when run is disqualified
    return 0


# calculate and return score of current run
def get_score(robot, data):
    return r.get_registry()['RUNS'].calculate_run_score(
        robot['division'],
        robot['level'],
        data['run_disqualified'],
        (to_float(data['seconds_to_put_out_candle_1']) +
         to_float(data['seconds_to_put_out_candle_2'])) / 2.0,
        data['non_air'],
        data['furniture'],
        data['arbitrary_start'],
        data['return_trip'],
        data['no_candle_circle'],
        data['stopped_within_30'],
        data['candle_detected'],
        to_int(data['number_of_rooms_searched']),
        data['kicked_dog'],
        to_int(data['touched_candle']),
        to_int(data['wall_contact_cms']),
        data['ramp_used'],
        data['baby_relocated'],
        data['all_candles'])

runs = [{
    'robot_id': 'h_21',
    'name': '',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '96',
    'seconds_to_put_out_candle_2': '96',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': False,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '1',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'h_12',
    'name': "Kegy the Fire-bot",
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '150.59',
    'seconds_to_put_out_candle_2': '148.41',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': False,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '2',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_6',
    'name': "",
    'wall_contact_cms': '2',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '138',
    'seconds_to_put_out_candle_2': '139',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': True,
    'run_disqualified': False,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '1',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_6',
    'name': "",
    'wall_contact_cms': '3',
    'level': 2L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '38.19',
    'seconds_to_put_out_candle_2': '38.68',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': True,
    'run_disqualified': False,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '1',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_29',
    'name': "",
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '3',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '96',
    'seconds_to_put_out_candle_2': '96',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': True,
    'run_disqualified': False,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '2',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_29',
    'name': "",
    'wall_contact_cms': '0',
    'level': 2L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '109.44',
    'seconds_to_put_out_candle_2': '109.78',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': True,
    'run_disqualified': False,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '3',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'h_11',
    'name': 'Sami the fireman',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '64',
    'seconds_to_put_out_candle_2': '64',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': False,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '2',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'j_1',
    'name': 'Fluff',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': True,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '16',
    'seconds_to_put_out_candle_2': '16',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': False,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '1',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_34',
    'name': "",
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': True,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '72.41',
    'seconds_to_put_out_candle_2': '73.13',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': True,
    'run_disqualified': False,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '4',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'h_5',
    'name': "",
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '58.7',
    'seconds_to_put_out_candle_2': '58',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': True,
    'non_air': True,
    'run_disqualified': False,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '2',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'j_1',
    'name': 'Fluff',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': True,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '4',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_42',
    'name': 'Astrid',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': True,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '1',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_11',
    'name': 'The Procrastinator',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': True,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '1',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_7',
    'name': 'Tower Of Shower',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': True,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '0',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'h_1',
    'name': 'Phlogiston',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': True,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '1',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'h_11',
    'name': 'Sami the fireman',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': True,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '2',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'h_21',
    'name': 'Big Red',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '1',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'j_5',
    'name': '',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '3',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'h_19',
    'name': '',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '0',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '3',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'j_1',
    'name': 'Goat Bot',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '1',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_29',
    'name': 'BantBot',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '3',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'h_1',
    'name': 'BantBot',
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '0',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'j_3',
    'name': "It's not rocket science",
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '0',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'j_4',
    'name': "Goat Bot",
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '2',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_11',
    'name': "The Procrastinator",
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '0',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_42',
    'name': "Astrid",
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '0',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_42',
    'name': "Astrid",
    'wall_contact_cms': '0',
    'level': 1L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '0',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 'h_5',
    'name': "",
    'wall_contact_cms': '0',
    'level': 2L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': False,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': False,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '4',
    'stopped_within_30': False,
    'furniture': False
}, {
    'robot_id': 's_34',
    'name': "",
    'wall_contact_cms': '0',
    'level': 2L,
    'arbitrary_start': False,
    'touched_candle': '1',
    'no_candle_circle': True,
    'return_trip': False,
    'baby_relocated': False,
    'seconds_to_put_out_candle_1': '600',
    'seconds_to_put_out_candle_2': '600',
    'all_candles': False,
    'versa_valve_used': False,
    'kicked_dog': False,
    'non_air': True,
    'run_disqualified': True,
    'ramp_used': False,
    'candle_detected': False,
    'number_of_rooms_searched': '4',
    'stopped_within_30': False,
    'furniture': False
}]

if __name__ == '__main__':
    load_registry()
    for run in runs:
        add_run(run['robot_id'], run)
