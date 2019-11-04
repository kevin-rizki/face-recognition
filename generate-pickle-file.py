from extract import *
import os
import pickle

def generatePickleFromBatch(pckPath, imgsPath):
    files = [os.path.join(imgsPath, p) for p in sorted(os.listdir(imgsPath))]
    db = dict()
    count = 0
    extracted = 0
    for f in files:
        count += 1
    for f in files:
        print('-> [Entry ' + str(extracted + 1) + '/' + str(count) + ']', 'Extracting', f, end = '               ')
        db[f] = dict()
        db[f] = extractFeatures(f)
        extracted += 1
        print('\r', end='')

    with open(pckPath, 'ab') as fp:
        pickle.dump(db, fp)
    print('Done.')

def generateDB(dbPath, pinsPath):
    if not os.path.exists(dbPath):
        os.makedirs(dbPath)

    if os.path.exists(pinsPath):
        count = 0
        generated = 0
        persons = [os.path.join(pinsPath, p) for p in sorted(os.listdir(pinsPath))]
        for person in persons:
            count += 1
        print('Found', count, 'directories on', pinsPath)
        for person in persons:
            generated += 1
            db = os.path.join(dbPath, person.split('/')[-1])
            print('[' + str(generated) + '/' +  str(count) + ']', 'Generating', db)
            generatePickleFromBatch(db, person)
        print('Extracted', count, 'entries on PINS.')

    else:
        print('Directory  not found')

def joinDB(dirPath, dbPath):
    db = dict()
    print('Joining databases from', dirPath, 'to', dbPath)
    if os.path.exists(dirPath):
        files = [os.path.join(dirPath, p) for p in sorted(os.listdir(dirPath))]
        for f in files:
            a = dict()
            print('->', f)
            with open(f, 'rb') as tempdb:
                a = pickle.load(tempdb)
                db.update(a)
        with open(dbPath, 'ab') as dbfile:
            pickle.dump(db, dbfile)
        print('Done.')
    else:
        print('Directory not found')
if __name__ == '__main__':
    generateDB('db', 'PINS')
    joinDB('db', 'pins.db')
