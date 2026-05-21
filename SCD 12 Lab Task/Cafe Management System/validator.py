class Validator:

    @staticmethod
    def validate_item(
        item_name,
        quantity,
        price
    ):

        if item_name == "":
            raise ValueError(
                "Item name required"
            )

        if int(quantity) <= 0:
            raise ValueError(
                "Invalid quantity"
            )

        if float(price) <= 0:
            raise ValueError(
                "Invalid price"
            )