from requests import get


class MacAddressIO:
	def __init__(self, api_key: str, mac_address: str):
		self.api = "https://api.macaddress.io"
		self.api_key = api_key
		self.mac_address = mac_address
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
			"x-authentication-token": self.api_key
		}
		self.response = get(
			f"{self.api}/v1?output=json&search={self.mac_address}",
			headers=self.headers).json()

	def get_vendor_details(self):
		return self.response["vendorDetails"]

	def get_company_name(self):
		return self.response["vendorDetails"]["companyName"]

	def get_company_address(self):
		return self.response["vendorDetails"]["companyAddress"]

	def get_mac_address_oui(self):
		return self.response["vendorDetails"]["oui"]

	def get_country_code(self):
		return self.response["vendorDetails"]["countryCode"]

	def get_block_details(self):
		return self.response["blockDetails"]

	def get_border_left(self):
		return self.response["blockDetails"]["borderLeft"]

	def get_border_right(self):
		return self.response["blockDetails"]["borderRight"]

	def get_block_size(self):
		return self.response["blockDetails"]["blockSize"]

	def get_block_size_assignment(self):
		return self.response["blockDetails"]["assignmentBlockSize"]

	def get_created_date(self):
		return self.response["blockDetails"]["dateCreated"]

	def get_updated_date(self):
		return self.response["blockDetails"]["dateUpdated"]

	def get_mac_address_details(self):
		return self.response["macAddressDetails"]

	def get_search_term(self):
		return self.response["macAddressDetails"]["searchTerm"]

	def get_virtual_machine(self):
		return self.response["macAddressDetails"]["virtualMachine"]

	def get_applications(self):
		return self.response["macAddressDetails"]["applications"]

	def get_transmission_type(self):
		return self.response["macAddressDetails"]["transmissionType"]

	def get_administration_type(self):
		return self.response["macAddressDetails"]["administrationType"]

	def get_wireshark_notes(self):
		return self.response["macAddressDetails"]["wiresharkNotes"]

	def get_comment(self):
		return self.response["macAddressDetails"]["comment"]
