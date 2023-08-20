from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import mysql.connector
 
class StoreDataInDatabase(Action):

    def name(self) -> Text:
        return "action_store_data_in_database"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get the values of the slots from the tracker
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")

        # connect to the database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="dcpproject"
        )

        # create a cursor object
        cursor = db.cursor()

        # execute the SQL query to insert the data
        query = "INSERT INTO equinix (name, email) VALUES (%s, %s)"
        values = (name, email)
        cursor.execute(query, values)

        # commit the changes to the database
        db.commit()

        # close the cursor and database connection
        cursor.close()
        db.close()

        # send a message to the user confirming the data was stored
        dispatcher.utter_message(text="We saved your profile!")

        return []
class UpdateDatabase(Action):

    def name(self) -> Text:
        return "action_dataupdate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get the values of the slots from the tracker
        newname = tracker.get_slot("newname")
        newemail = tracker.get_slot("newemail")

        # connect to the database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="dcpproject"
        )

        # create a cursor object
        cursor = db.cursor()

        # execute the SQL query to update the data
        
        query = "UPDATE equinix SET email= %s WHERE name= %s;"
        values = (newemail, newname)
        cursor.execute(query, values)

        # commit the changes to the database
        db.commit()

        # close the cursor and database connection
        cursor.close()
        db.close()

        # send a message to the user confirming the data was stored
        dispatcher.utter_message(text="We changed your profile!")

        return []
