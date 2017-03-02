import sys, getopt, datetime

from tabulate import tabulate

from bitmovin import Bitmovin
from bitmovin.errors import BitmovinApiError


def print_usage():
    print('pull_infrastructure_status.py -k <apiKey> -i <infrastructureId>')


def main(argv):

    apiKey = ''
    infrastructureId = ''

    try:
        opts, args = getopt.getopt(argv, "hk:i:", ['apikey=', 'infrastructureid='])
    except getopt.GetoptError as error:
        print(error)
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if (opt == '-h'):
            print_usage()
            sys.exit()
        if (opt in ('-k', '--apikey')):
            apiKey = arg
        if (opt in ('-i', '--infrastructureid')):
            infrastructureId = arg

    if (apiKey == '' or infrastructureId == ''):
        print_usage()
        sys.exit(3)

    bitmovin = Bitmovin(api_key=apiKey)

    try:
        infrastructure_detail_response = bitmovin.infrastructures.Kubernetes.retrieve(id_=infrastructureId)
        k8s = infrastructure_detail_response.resource
        headers = ['Name', 'Online', 'Connected']
        table = [[k8s.name, k8s.online, k8s.connected]]
        print('\n{}'.format(datetime.datetime.now()))
        print(tabulate(table, headers=headers, tablefmt='fancy_grid'))
        print('\nAgent run command:\n------------------\n{}\n'.format(k8s.agentRunCommand))
    except BitmovinApiError as e:
        print('An error occured: ', vars(e))
        sys.exit(5)

if __name__ == '__main__':
    main(sys.argv[1:])
