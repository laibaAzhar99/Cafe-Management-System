from database import Database
from validator import Validator

class Controller:

    def __init__(self):

        self.db = Database()

    def add_item(
        self,
        item_name,
        quantity,
        price
    ):

        Validator.validate_item(
            item_name,
            quantity,
            price
        )

        self.db.insert_item(
            item_name,
            quantity,
            price
        )

    def get_items(self):

        return self.db.fetch_items()

    def remove_item(
        self,
        item_id
    ):

        self.db.delete_item(
            item_id
        )

    def edit_item(
        self,
        item_id,
        item_name,
        quantity,
        price
    ):

        Validator.validate_item(
            item_name,
            quantity,
            price
        )

        self.db.update_item(
            item_id,
            item_name,
            quantity,
            price
        )