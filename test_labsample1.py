import labsample1


def test_get_longest_workout():
    workouts = labsample1.load_csv()
    result = {}
    result = labsample1.get_longest_workout(workouts)
    test = {'date': "25.01.2022",'activity': "Cycling",'duration':75}
    assert (result == test)
def test_calc_total_duration():
    workouts = labsample1.load_csv()
    result = labsample1.calc_total_duration(workouts)
    test = 853
    assert (result == test)

def test_calc_average_duration():
    workouts = labsample1.load_csv()
    result = labsample1.calc_average_duration(workouts)
    test = 42.65
    assert (result == test )