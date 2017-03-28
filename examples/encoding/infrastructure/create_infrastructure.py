import sys, getopt, datetime

from tabulate import tabulate

from bitmovin import Bitmovin, KubernetesInfrastructure
from bitmovin.errors import BitmovinApiError


def print_usage():
    print('pull_infrastructure_status.py -k <apiKey> -n <name>')


def main(argv):

    apiKey = ''
    infrastructureName = ''

    try:
        opts, args = getopt.getopt(argv, "hk:n:", ['apikey=', 'name='])
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
        if (opt in ('-n', '--name')):
            infrastructureName = arg

    if (apiKey == '' or infrastructureName == ''):
        print_usage()
        sys.exit(3)

    bitmovin = Bitmovin(api_key=apiKey)

    try:
        k8s_infrastructure = KubernetesInfrastructure(name=infrastructureName)
        infrastructure_detail_response = bitmovin.infrastructures.Kubernetes.create(object_=k8s_infrastructure)
        k8s = infrastructure_detail_response.resource
        headers = ['ID', 'Name', 'Online', 'Connected']
        table = [[k8s.id, k8s.name, k8s.online, k8s.connected]]
        print('\n{}'.format(datetime.datetime.now()))
        print(tabulate(table, headers=headers, tablefmt='fancy_grid'))
        print('\nAgent run command:\n------------------\ncurl -X GET -H "X-Api-Key: {}" {} > bitmovin-agent.tar\n'.format(apiKey, k8s.agentRunCommand))
    except BitmovinApiError as e:
        print('An error occured: ', vars(e))
        sys.exit(5)

if __name__ == '__main__':
    main(sys.argv[1:])
