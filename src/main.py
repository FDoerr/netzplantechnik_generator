from netzplanknoten import Netzplanknoten as knoten



def main():
    knoten_1 = knoten('knoten_1', 1, ['knoten_2', 'knoten_3'])
    knoten_2 = knoten('knoten_2', 2, ['knoten_4'])
    knoten_3 = knoten('knoten_3', 3, ['knoten_4'])
    knoten_4 = knoten('knoten_4', 3, None)
    ...


if __name__=='__main__':
    main()