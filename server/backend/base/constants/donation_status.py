from enum import Enum


class DonationStatus(Enum):
    wait = 0
    accepted = 1
    delivered = 2
    refused = 3
