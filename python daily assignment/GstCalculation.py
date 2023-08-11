class Company:
    CompanyName = "ABC"
    CompanyRegistration = "PVTLTD"
    CompanyAddress = "XYZ"
    CompanySize = 100
    CompanyLocation = "ABCDEFGH"

    def __init__(self, cmpName, cmpRegd, cmpAddress, cmpSize, cmpLocation):
        self.companyName = cmpName
        self.companyRegistration = cmpRegd
        self.companySize = cmpSize
        self.companyAddress = cmpAddress
        self.companyLocation = cmpLocation

    def DisplayCompanyDetails(self):
        print("The Company Details are:")
        print("Name:", self.companyName)
        print("Registration:", self.companyRegistration)
        print("Address:", self.companyAddress)
        print("Size:", self.companySize)
        print("Location:", self.companyLocation)

    def UpdateCompanyName(self):
        self.companyName = input("Enter the new Company Name: ")
        print("The new Company name is:", self.companyName)

    def UpdateCompanyAddress(self):
        self.companyAddress = input("Enter the new Company Address: ")
        print("The new Company address is:", self.companyAddress)

    def UpdateCompanySize(self):
        self.companySize = input("Enter the new Company Size: ")
        print("The number of Employees in the Company is:", self.companySize)

    def UpdateCompanyLocation(self):
        self.companyLocation = input("Enter the new Company Location: ")
        print("The new Company Location is:", self.companyLocation)

# Create an instance of the Company class
companyObj = Company("EKIPIT", "MCA Registration", "Madhapur, Hyderabad", "150", "Some Location")

# Test the methods
companyObj.DisplayCompanyDetails()
companyObj.UpdateCompanyName()
companyObj.UpdateCompanyAddress()
companyObj.UpdateCompanySize()
companyObj.UpdateCompanyLocation()