import sys
from bitmovin import Bitmovin, AnalyticsDomain

API_KEY = '<YOUR API KEY>'

def displayDomains(bitmovin, license):
    domains = bitmovin.analytics.Licenses.retrieve(license.id).resource.domains
    print('Domains for {0}'.format(license.name or license.id))
    for domain in domains:
        print('- {0}'.format(domain.url))

def promptAddDomain(bitmovin, license):
    domain = input('Please enter the domain you want to add:\n> ')
    yes_no = input('Please confirm you want to add {0} to {1}: [Yn] '.format(domain, license.name or license.id))
    if yes_no.lower() == 'n':
        print('Ok, bye')
        exit()
    return domain


def main():
    bitmovin = Bitmovin(api_key=API_KEY)
    licenses = bitmovin.analytics.Licenses.list().resource

    print('Select which License you want to add a Domain to:')
    counter = 0
    for license in licenses:
        counter += 1
        name = license.name or license.id
        print('[{0}]: {1}'.format(str(counter), name))
    
    number = input()
    license = licenses[int(number) - 1]
    displayDomains(bitmovin, license)
    add_domain = promptAddDomain(bitmovin, license)
    if add_domain != None:
        domain = AnalyticsDomain(url=add_domain)
        bitmovin.analytics.Licenses.Domains.create(object_=domain, license_id=license.id)

        license = bitmovin.analytics.Licenses.retrieve(license.id).resource
        print('- Domain successfully added')
        displayDomains(bitmovin, license)


if __name__ == '__main__':
    main()
