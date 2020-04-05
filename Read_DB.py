import pickle

def read_info():
    f = open("statics/DB/CoronaDB.dat", "rb")
    Coronavirus_Cases = pickle.load(f)
    Death = pickle.load(f)
    Recovered = pickle.load(f)
    Table_Info = pickle.load(f)
    f.close()

    Info_dict = {
        "Coronavirus_Cases" : Coronavirus_Cases,
        "Death" : Death,
        "Recovered" : Recovered,
        "Table_Info" : Table_Info
    }

    return Info_dict