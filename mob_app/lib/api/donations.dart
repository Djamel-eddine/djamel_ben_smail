Object getDonationById(String token, String id) {
  return {};
}

List<Object> getAllDonations(String token) {
  return [];
}

List<Object> getPersonDonationsByCompaign(
    String token, String userID, String compaignID) {
  return [];
}

List<Object> getPersonDonations(String token, String userID) {
  return [];
}

List<Object> getCompaignDonations(String token, String compaignID) {
  return [];
}

List<Object> getAssociationDonations(String token, String associationID) {
  return [];
}

List<Object> getCompaignNeedDonations(String token, String compaignID) {
  return [];
}

Object addNewDonation(
    String token, String compaign, String need, int qteDonated) {
  return {};
}

Object updateDonation(String id, String token, int qteDonated) {
  return {};
}

Object acceptDonation(String id, String token, int qteAccepted) {
  return {};
}

Object refuseDonation(String id, String token) {
  return {};
}

Object setDelivered(String id, String token, int qteDonated) {
  return {};
}

Object updateDonationAcceptedQte(String id, String token, int qteAccepted) {
  return {};
}

Object updateDonationDeliverdQte(String id, String token, int qteDeliverd) {
  return {};
}

Object deleteDonation(String id, String token) {
  return {};
}
