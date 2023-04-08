#! /usr/bin/env python3
# encoding:utf-8

import time
import cv2
import pymongo
from pyzbar.pyzbar import decode
from pymongo import MongoClient


def get_database():
    """ Connect to mongodb database """
    
    # Provide the mongodb atlas url to connect python to mongodb
    CONNECTION_STRING = input("mongoDB connection string: ")
    
    # Create a connection using MongoClient.
    client = MongoClient(CONNECTION_STRING)
    database = input("Database name: ")
    
    return client[database]
  

def input_book_info(barcode):
    """ input book item

    Args: barcode
    Returns:
        book information
    """

    title = input("Enter book title: ")
    author = input("Enter author(first): ")
    category = input("Enter category: ")
    language = input("Enter language: ")

    book_info = {
        "_id" : barcode,
        "title" : title,
        "author" : author,
        "language" : language,
        "category" : category
    }

    print(book_info)

    return book_info

def retrieve_record(collection, book_id):
    """ retrieve book item
    
    Args: 
        collection
        book_id
    Returns:
        book information
    """
    
    book_info = collection.find_one({"_id": book_id})
    print(book_info)

    return book_info


def config_camera(width, height):
    """ camera configuration """

    capture = cv2.VideoCapture(0)
    capture.set(3, width)
    capture.set(4, height)

    return capture


def main():

    # connect to database
    dbname = get_database()
    collection_name = dbname["books"]

    while True:
        print("Input 1 for retrieving items, 2 for inserting items.")
        mode = input("Selected mode: ")
        if mode not in ['1','2']:
            print("Invalid Mode!")
        else:
            break
        
    
    # configurate camera
    cap = config_camera(640, 480)
    camera = True

    while (camera == True):

        success, frame = cap.read()
        for code in decode(frame):

            # read barcode
            barcode = code.data.decode('utf-8')
            print(barcode)
            time.sleep(1)

            # retrieve record from database
            if mode == '1':
                book = retrieve_record(collection_name, barcode)

            # insert record to database
            if mode == '2':
                book = input_book_info(barcode)
                try:
                    collection_name.insert_one(book)
                except pymongo.errors.DuplicateKeyError:
                    print("ID exists!")
                    continue

        cv2.imshow('Code-scanner',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()