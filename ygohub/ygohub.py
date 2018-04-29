import requests


class YGOhub:
    """A simple wrapper for ygohub api"""

    def __init__(self):
        self.url = 'https://www.ygohub.com/api'

    def __make_request(self, url):
        response = requests.get(url)

        if response.status_code != 200:
            status_code = response.status_code
            reason = response.reason
            raise Exception(f'Status code: {status_code} Reason: {reason}')

        return response.json()

    def make_request(self, url):
        """Repass a url to __make_request"""
        return self.__make_request(url)

    def get_all_cards(self):
        """Retrieves a list of all card names in the database"""
        return self.make_request(f'{self.url}/all_cards')

    def get_card_info(self, card_name):
        """Grabs all information on a single card"""
        return self.make_request(f'{self.url}/card_info?name={card_name}')

    def get_card_from_passcode(self, passcode):  # TODO
        """
        Gets a card's information from a cards passcode/number.
        If the card does not have a passcode, the YGOPro ID will work
        """
        return self.make_request(
            f'{self.url}/get_card_from_passcode?passcode={passcode}'
        )

    def get_new_cards(self, num_cards):
        """Grabs the newest cards in the database"""
        if num_cards in range(1, 21):
            return self.make_request(
                f'{self.url}/new_cards?num_cards={num_cards}'
            )
        raise Exception(f'{num_cards} is not between 1 and 20')

    def get_all_sets(self):
        """Retrieves a list of all set names in the database"""
        return self.make_request(f'{self.url}/all_sets')

    def get_set_info(self, set_name):
        """Grabs all information on a single set"""
        return self.make_request(f'{self.url}/set_info?name={set_name}')

    def get_card_set_abbreviations(self):
        """Grabs all abbreviations for all the sets in the database"""
        return self.make_request(f'{self.url}/get_card_set_abbreviations')

    def get_all_banlists(self):
        """Get a list of all banlists"""
        return self.make_request(f'{self.url}/all_banlists')

    def get_banlists_info(self, region, start_date, game_type):
        """Grabs information on a single banlist"""
        return self.make_request(
            f'{self.url}/banlist_info?region={region}&start_date={start_date}&game_type={game_type}'
        )
