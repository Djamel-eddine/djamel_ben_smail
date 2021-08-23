from enum import Enum


class DonationStatus(Enum):
    wait = 1
    accepted = 2
    delivered = 3
    refused = 4
